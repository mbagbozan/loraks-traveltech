# src/orchestrator.py
"""
LORAKS Master Brain Orchestrator
Tüm motorları (NLP Ajanı, Pathway, Vergi, KVK m.13 POS, QR Check-in, İade) tek noktadan koordine eden orkestratör.
"""
from decimal import Decimal
from typing import Dict, Any

from src.models import (
    Listing, HostProfile, BookingTransaction, PathwayCode, 
    MerchantEntity, BookingStatus, HostTaxProfile
)
from src.ai_audit_agent import scan_listing_for_p2_masking
from src.pathway_engine import PathwayEngine
from src.payment_engine import PaymentEngine
from src.tax_engine import calculate_split_and_withholding
from src.refund_engine import RefundEngine
from src.offline_sync import OfflineQRValidator

class LoraksBrainOrchestrator:
    def __init__(self):
        self.pathway_engine = PathwayEngine()
        self.payment_engine = PaymentEngine()
        self.refund_engine = RefundEngine()

    def onboard_and_audit_listing(self, listing: Listing) -> Dict[str, Any]:
        """
        1. ADIM: Host İlan Açtığında Çalışan Denetim ve Sınıflandırma Mantığı
        """
        # 1. NLP AI Taraması: Gizli tur/ulaşım maskelemesi var mı?
        is_masked_p2 = scan_listing_for_p2_masking(listing.description)
        if is_masked_p2:
            listing.compliance_flags.append("AI_MASKED_P2_DETECTED")
            listing.has_transport = True  # Zorunlu olarak P2'ye çekilir!

        # 2. Pathway ve Gateway Kural Motoru
        listing_dict = {
            "title": listing.title,
            "has_transport": listing.has_transport,
            "has_accommodation": listing.has_accommodation,
            "is_multi_day": listing.is_multi_day,
            "has_guided_tour": listing.has_guided_tour
        }
        gateway_config = self.pathway_engine.determine_payment_gateway(listing_dict)
        listing.pathway_code = PathwayCode(listing_dict['pathway_code'])
        listing.is_approved = True

        return {
            "listing_id": listing.id,
            "assigned_pathway": listing.pathway_code.value,
            "merchant_entity": (
                MerchantEntity.ACENTA_AS.value 
                if listing.pathway_code == PathwayCode.P2 
                else MerchantEntity.TEKNOLOJI_AS.value
            ),
            "gateway_config": gateway_config,
            "compliance_flags": listing.compliance_flags
        }

    def process_booking_checkout(self, booking: BookingTransaction) -> Dict[str, Any]:
        """
        2. ADIM: Satın Alma Anı (Checkout & Zero-Tax Escrow)
        """
        # 1. KVK m.13 POS Ayrımını Denetle
        pos_allocation = self.payment_engine.process_pos_fee_allocation(booking)
        booking.pos_fee_amount = pos_allocation['amount']
        
        # 2. Fonu Havuzda Tut (Henüz vergi ve komisyon tetiklenmez)
        booking.status = BookingStatus.IN_ESCROW

        return {
            "booking_id": booking.booking_id,
            "status": booking.status.value,
            "merchant_entity": booking.merchant_entity.value,
            "pos_fee_allocated_to": pos_allocation['company'],
            "pos_fee_amount": booking.pos_fee_amount,
            "escrow_amount": booking.gross_amount
        }

    def trigger_qr_checkin_settlement(self, booking: BookingTransaction, host: HostProfile) -> Dict[str, Any]:
        """
        3. ADIM: Hizmet İfası (Check-in / QR Doğrulaması) -> Vergi ve Hakediş Tetiklenir
        """
        # 1. Durumu CHECKED_IN ve SETTLED'a al
        booking.status = BookingStatus.SETTLED

        # 2. Decimal Hassasiyetli 7524 S.K. Stopaj ve Hak Ediş Hesapla
        split_result = calculate_split_and_withholding(
            gross_amount=booking.gross_amount,
            host_tax_profile=host.tax_profile.value
        )

        return {
            "booking_id": booking.booking_id,
            "status": booking.status.value,
            "gross_amount": split_result['gross_amount'],
            "loraks_net_revenue": split_result['loraks_net_revenue'],
            "loraks_vat_391": split_result['loraks_vat'],
            "withholding_tax_360": split_result['withholding_tax_360'],
            "host_net_payout": split_result['host_payout'],
            "host_tax_profile": host.tax_profile.value
        }

    def process_cancellation_refund(self, booking: BookingTransaction, is_checked_in: bool = False) -> Dict[str, Any]:
        """
        4. ADIM: İptal / İade (Check-in öncesi ve sonrası ayrımı)
        """
        return self.refund_engine.process_refund_allocation(booking, is_checkin_completed=is_checked_in)
