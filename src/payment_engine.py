"""
LORAKS TRAVELTECH — FINTECH SPLIT PAYMENT & TAX ENGINE
Compliant with: Law 6493 (Payment Facilitator), Law 7524 & Decree 9284 (1% Withholding), TFRS 15 (Agent Net Revenue)
"""

from typing import Dict, Any, Optional
import uuid
import datetime

class PaymentEngine:
    DEFAULT_COMMISSION_RATE = 0.15      # 15% standard platform take rate
    DIRECT_SALE_COMMISSION_RATE = 0.05  # 5% if traveler books via host direct link
    WITHHOLDING_TAX_RATE = 0.01         # 1% Law 7524 & Decree 9284 e-commerce tevkifat

    def __init__(self):
        # In-memory mock idempotency & payment store for verification and testing
        self.processed_idempotency_keys: Dict[str, Dict[str, Any]] = {}
        self.settlement_ledger: Dict[str, Dict[str, Any]] = {}

    def calculate_split(
        self,
        gross_amount: float,
        pathway_code: str = "P0",
        is_direct_link: bool = False,
        tax_basis: str = "net_matrah"  # 'net_matrah' (KDV-exclusive matrah 7524 tevkifat) or 'gross'
    ) -> Dict[str, Any]:
        """
        Calculates exact split allocations down to the cent:
        GMV (Gross) = Platform Commission (Take Rate) + 1% GİB Withholding + Net Supplier Payout
        """
        if gross_amount <= 0:
            raise ValueError("Brüt tutar sıfırdan büyük olmalıdır.")

        gross_amount = round(gross_amount, 2)

        # 1. Commission rate selection
        if is_direct_link:
            commission_rate = self.DIRECT_SALE_COMMISSION_RATE
        elif pathway_code == "P2":
            commission_rate = 0.12 # Regulated travel has 12% tech take-rate
        else:
            commission_rate = self.DEFAULT_COMMISSION_RATE

        # 2. Commission calculation (KDV included)
        platform_commission_gross = round(gross_amount * commission_rate, 2)
        platform_commission_net_matrah = round(platform_commission_gross / 1.20, 2)
        platform_commission_kdv = round(platform_commission_gross - platform_commission_net_matrah, 2)

        # 3. Sanal POS fee calculation (~2.8% benchmark)
        pos_fee = round(gross_amount * 0.028, 2)
        platform_net_retention = round(platform_commission_gross - pos_fee, 2)

        # 4. Law 7524 / Decree 9284 Withholding Tax (1% e-commerce tevkifat)
        # In Turkish VAT law, withholding is computed on KDV-exclusive base (gross / 1.20)
        if tax_basis == "net_matrah":
            kdv_exclusive_base = round(gross_amount / 1.20, 2)
            withholding_tax = round(kdv_exclusive_base * self.WITHHOLDING_TAX_RATE, 2)
        else:
            withholding_tax = round(gross_amount * self.WITHHOLDING_TAX_RATE, 2)

        # 5. Net Supplier / Agency Payout
        net_supplier_payout = round(gross_amount - platform_commission_gross - withholding_tax, 2)

        # Exact cent-balance check
        total_calculated = round(platform_commission_gross + withholding_tax + net_supplier_payout, 2)
        if total_calculated != gross_amount:
            discrepancy = round(gross_amount - total_calculated, 2)
            net_supplier_payout = round(net_supplier_payout + discrepancy, 2)

        # 5. TFRS 15 Invoicing Route
        if pathway_code == "P2":
            b2c_issuer = "LORAKS ORGANİZASYON DANIŞMANLIK HİZMETLERİ A.Ş. (TÜRSAB A Grubu No: 16978)"
            b2c_desc = "Zorunlu Sigortalı Paket Tur / Deneyim Hizmet Bedeli"
        else:
            b2c_issuer = "DOĞRULANMIŞ ORGANİZATÖR (HOST)"
            b2c_desc = "Atölye / Nitelikli Etkinlik Hizmet Bedeli"

        return {
            "gross_amount": gross_amount,
            "pathway_code": pathway_code,
            "commission_rate": commission_rate,
            "splits": {
                "platform_take_rate": {
                    "recipient": "LORAKS TEKNOLOJİ ANONİM ŞİRKETİ",
                    "gross_amount": platform_commission_gross,
                    "net_matrah": platform_commission_net_matrah,
                    "kdv_20": platform_commission_kdv,
                    "pos_fee_absorbed": pos_fee,
                    "net_cash_retention": platform_net_retention,
                    "invoice_type": "B2B_E_ARSIV_KOMISYON"
                },
                "tax_withholding_gib": {
                    "recipient": "GİB_TEVKIFAT_HAVUZU",
                    "amount": withholding_tax,
                    "tax_basis": tax_basis,
                    "law_reference": "7524 Sayılı Kanun & 9284 Sayılı C.K."
                },
                "supplier_net_payout": {
                    "recipient": "HOST_VEYA_OPERASYON_ACENTESİ",
                    "net_amount": net_supplier_payout,
                    "payout_condition": "QR_CHECKIN_OR_EVENT_COMPLETION"
                }
            },
            "invoicing": {
                "b2c_customer_invoice": {
                    "issuer": b2c_issuer,
                    "total_amount": gross_amount,
                    "description": b2c_desc
                },
                "b2b_platform_invoice": {
                    "issuer": "LORAKS TEKNOLOJİ ANONİM ŞİRKETİ",
                    "receiver": b2c_issuer,
                    "amount": platform_commission_gross,
                    "description": "Pazaryeri Yazılım ve Aracılık Hizmet Bedeli"
                }
            }
        }

    def process_charge(
        self,
        booking_id: str,
        gross_amount: float,
        idempotency_key: str,
        pathway_code: str = "P0",
        buyer_info: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Executes an idempotent payment charge via PSP rails, locking funds in escrow.
        """
        # Idempotency guard: Return existing payment if duplicate key presented
        if idempotency_key in self.processed_idempotency_keys:
            existing = self.processed_idempotency_keys[idempotency_key]
            return {
                "status": "IDEMPOTENT_REPLAY",
                "message": "İşlem daha önce başarıyla gerçekleştirildi.",
                "data": existing
            }

        payment_id = f"PAY-{uuid.uuid4().hex[:12].upper()}"
        split_details = self.calculate_split(gross_amount, pathway_code)

        payment_record = {
            "payment_id": payment_id,
            "booking_id": booking_id,
            "idempotency_key": idempotency_key,
            "gross_amount": gross_amount,
            "currency": "TRY",
            "status": "IN_ESCROW",
            "escrow_locked_at": datetime.datetime.utcnow().isoformat(),
            "split_details": split_details,
            "buyer_info": buyer_info or {}
        }

        self.processed_idempotency_keys[idempotency_key] = payment_record
        self.settlement_ledger[payment_id] = payment_record

        return {
            "status": "SUCCESS",
            "message": "Ödeme başarıyla provizyona alındı; fonlar TCMB korumalı havuzda bloke edildi.",
            "data": payment_record
        }

    def settle_payment(self, payment_id: str, verified_by_qr: bool = True) -> Dict[str, Any]:
        """
        Releases escrow upon verified QR check-in or event execution.
        """
        if payment_id not in self.settlement_ledger:
            raise KeyError(f"Ödeme kaydı bulunamadı: {payment_id}")

        record = self.settlement_ledger[payment_id]
        if record["status"] == "SETTLED":
            return {"status": "ALREADY_SETTLED", "data": record}

        record["status"] = "SETTLED"
        record["settled_at"] = datetime.datetime.utcnow().isoformat()
        record["verification_method"] = "QR_CHECKIN" if verified_by_qr else "ADMIN_RELEASE"

        return {
            "status": "SETTLED",
            "message": "Emanet (escrow) çözüldü; hak ediş transferleri ve vergi beyan kuyruğu tetiklendi.",
            "data": record
        }

    def cancel_and_refund(self, payment_id: str, reason: str = "GUEST_OR_WEATHER_CANCELLATION") -> Dict[str, Any]:
        """
        Handles cancellation before event execution (Reverse Flow / Tersine Akış Koruması).
        If payment is still IN_ESCROW (prior to QR check-in / realization):
        - Funds are 100% refunded to the buyer immediately via PSP rails.
        - Zero withholding tax is remitted to GİB, completely avoiding the tax claw-back bureaucracy.
        """
        if payment_id not in self.settlement_ledger:
            raise KeyError(f"Ödeme kaydı bulunamadı: {payment_id}")

        record = self.settlement_ledger[payment_id]
        if record["status"] == "SETTLED":
            return {
                "status": "REQUIRES_FORMAL_TAX_REVERSAL",
                "message": "Ödeme çoktan QR ile kesinleştirilmiş ve vergi kuyruğuna iletilmiş. Otomatik İade Faturası / Gider Pusulası döngüsü gereklidir.",
                "data": record
            }

        if record["status"] == "REFUNDED":
            return {"status": "ALREADY_REFUNDED", "data": record}

        record["status"] = "REFUNDED"
        record["refunded_at"] = datetime.datetime.utcnow().isoformat()
        record["cancellation_reason"] = reason
        record["refund_type"] = "PURE_ESCROW_REVERSAL_ZERO_TAX_PENALTY"

        return {
            "status": "REFUNDED",
            "message": "Rezervasyon etkinlik gerçekleşmeden önce iptal edildi. %100 bilet tutarı emanet havuzundan iade edildi; devlete vergi aktarımı tetiklenmedi.",
            "data": record
        }

    def process_pos_fee_allocation(self, booking_transaction: Any) -> Dict[str, Any]:
        """
        KVK m. 13 Uyumlu POS Masraf Ayrım Motoru
        YASAL KISIT (INVARIANT): Masrafı ödeyen şirket, ciroyu yazan şirket ile BİREBİR aynı olmalıdır!
        """
        from src.exceptions import ComplianceViolationException, InvalidPathwayException
        from decimal import Decimal
        from src.tax_engine import quantize_money

        merchant_entity = getattr(booking_transaction, 'merchant_entity', None)
        pathway_code = getattr(booking_transaction, 'pathway_code', None)
        gross_amount = getattr(booking_transaction, 'gross_amount', Decimal('0.00'))
        if not isinstance(gross_amount, Decimal):
            gross_amount = Decimal(str(gross_amount))
        gross_amount = quantize_money(gross_amount)

        pos_rate = getattr(booking_transaction, 'pos_commission_rate', Decimal('0.028'))
        if not isinstance(pos_rate, Decimal):
            pos_rate = Decimal(str(pos_rate))
        pos_fee_amount = quantize_money(gross_amount * pos_rate)

        if pathway_code in ['P0', 'P1']:
            if merchant_entity != "LORAKS_TEKNOLOJI_AS":
                raise ComplianceViolationException(
                    "KVK m.13 İhlali: P0/P1 atölye POS masrafı Acente şirketine aktarılamaz!"
                )
            
            # POS Masrafı Teknoloji A.Ş. 653 Hesabına İşlenir
            if hasattr(booking_transaction, 'record_ledger_entry'):
                booking_transaction.record_ledger_entry(
                    account_code="653_COMMISSION_EXPENSE_TEK",
                    amount=pos_fee_amount,
                    company="LORAKS_TEKNOLOJI_AS"
                )
            return {
                "company": "LORAKS_TEKNOLOJI_AS",
                "account_code": "653_COMMISSION_EXPENSE_TEK",
                "pos_fee_amount": pos_fee_amount
            }
            
        elif pathway_code == 'P2':
            if merchant_entity != "LORAKS_ACENTA_AS":
                raise ComplianceViolationException(
                    "TÜRSAB & KVK İhlali: P2 paket tur POS masrafı Teknoloji şirketine aktarılamaz!"
                )
            
            # POS Masrafı Acente A.Ş. 653 Hesabına İşlenir
            if hasattr(booking_transaction, 'record_ledger_entry'):
                booking_transaction.record_ledger_entry(
                    account_code="653_COMMISSION_EXPENSE_ACE",
                    amount=pos_fee_amount,
                    company="LORAKS_ACENTA_AS"
                )
            return {
                "company": "LORAKS_ACENTA_AS",
                "account_code": "653_COMMISSION_EXPENSE_ACE",
                "pos_fee_amount": pos_fee_amount
            }
        else:
            raise InvalidPathwayException(f"Geçersiz Pathway Kodu: {pathway_code}")
