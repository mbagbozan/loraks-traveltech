# tests/test_full_brain.py
"""
LORAKS Tüm Arka Plan Beyin Fonksiyonlarının Entegre Doğrulama Testi
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from decimal import Decimal

from src.models import (
    Listing, HostProfile, BookingTransaction, PathwayCode, 
    MerchantEntity, BookingStatus, HostTaxProfile
)
from src.orchestrator import LoraksBrainOrchestrator
from src.offline_sync import OfflineQRValidator
from src.exceptions import ComplianceViolationException

class TestLoraksFullBrainIntegration(unittest.TestCase):
    def setUp(self):
        self.orchestrator = LoraksBrainOrchestrator()

    def test_end_to_end_workshop_flow(self):
        """P0 Seramik Atölyesi: İlan Açılışı -> Rezervasyon -> QR Check-in -> Vergi ve Hak Ediş"""
        # 1. Host ve İlan
        host = HostProfile(
            id="HOST_001",
            full_name="Zeynep Seramik",
            tax_profile=HostTaxProfile.INDIVIDUAL_EXEMPT,
            tc_or_vkn="12345678901",
            iban="TR330006100511122233344455",
            has_esnaf_muafiyeti_doc=True
        )
        listing = Listing(
            id="LIST_001",
            host_id=host.id,
            title="Kadıköy Çamur ve Seramik Atölyesi",
            description="Kendi atölyemizde 2 saat çamur tornasında vazo ve fincan üreteceğiz.",
            gross_price=Decimal('1000.00'),
            has_transport=False
        )
        
        # İlan Onayı ve Sınıflandırma
        audit_res = self.orchestrator.onboard_and_audit_listing(listing)
        self.assertEqual(audit_res['assigned_pathway'], "P0")
        self.assertEqual(audit_res['merchant_entity'], "LORAKS_TEKNOLOJI_AS")
        
        # 2. Bilet Satın Alma (Checkout)
        booking = BookingTransaction(
            booking_id="BOK_101",
            listing_id=listing.id,
            guest_id="GUEST_501",
            gross_amount=listing.gross_price,
            pathway_code=PathwayCode.P0,
            merchant_entity=MerchantEntity.TEKNOLOJI_AS
        )
        checkout_res = self.orchestrator.process_booking_checkout(booking)
        self.assertEqual(checkout_res['status'], "IN_ESCROW")
        self.assertEqual(checkout_res['pos_fee_allocated_to'], "LORAKS_TEKNOLOJI_AS")
        self.assertEqual(checkout_res['pos_fee_amount'], Decimal('28.00'))  # 1000 * 0.028

        # 3. Hizmet İfası (QR Check-in & Settlement)
        settle_res = self.orchestrator.trigger_qr_checkin_settlement(booking, host)
        self.assertEqual(settle_res['status'], "SETTLED")
        self.assertEqual(settle_res['loraks_net_revenue'], Decimal('125.00'))  # Net 150 / 1.20
        self.assertEqual(settle_res['loraks_vat_391'], Decimal('25.00'))       # %20 KDV
        self.assertEqual(settle_res['withholding_tax_360'], Decimal('8.33'))   # 833.33 * %1 stopaj
        self.assertEqual(settle_res['host_net_payout'], Decimal('841.67'))     # Kuruş tam denkleşir!
        
        # Toplam = 125 + 25 + 8.33 + 841.67 = 1000.00
        total = settle_res['loraks_net_revenue'] + settle_res['loraks_vat_391'] + settle_res['withholding_tax_360'] + settle_res['host_net_payout']
        self.assertEqual(total, Decimal('1000.00'))

    def test_ai_catches_masked_tour_forces_acenta_p2(self):
        """Host P0 gibi gösterip otobüs/transfer yazdığında sistem P2 Acente POS'una kilitliyor mu?"""
        listing = Listing(
            id="LIST_002",
            host_id="HOST_002",
            title="Kapadokya Vadi Gezisi",
            description="Sabah Kadıköy servis kalkış noktası üzerinden yola çıkıp rehber eşliğinde vadiyi gezeceğiz.",
            gross_price=Decimal('2500.00')
        )
        audit_res = self.orchestrator.onboard_and_audit_listing(listing)
        self.assertEqual(audit_res['assigned_pathway'], "P2")
        self.assertEqual(audit_res['merchant_entity'], "LORAKS_ACENTA_AS")
        self.assertIn("AI_MASKED_P2_DETECTED", audit_res['compliance_flags'])
        self.assertEqual(audit_res['gateway_config']['merchant_id'], "ACENTA_IYZICO_MERCHANT_ID")

    def test_offline_hmac_qr_ticket_verification(self):
        """Dağ başında baz istasyonu olmadan HMAC QR bilet doğrulanabiliyor mu?"""
        ticket_str = OfflineQRValidator.generate_signed_ticket(
            booking_id="BOK_777",
            guest_id="GUEST_888",
            listing_id="LIST_999",
            event_timestamp=1775500000
        )
        # Doğrulama
        is_valid, payload, msg = OfflineQRValidator.verify_offline_ticket(ticket_str)
        self.assertTrue(is_valid)
        self.assertEqual(payload['bid'], "BOK_777")
        self.assertEqual(msg, "OFFLINE_VALID_CHECKIN_STORED")

if __name__ == '__main__':
    unittest.main()
