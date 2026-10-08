"""
LORAKS TRAVELTECH — PAYOUT & TCMB / 6493 S.K. COMPLIANCE ENGINE
Version: v3.1 Production Ready
Enforces strict T+1 automatic payout release upon QR check-in to prevent unauthorized escrow deposits.
"""

from decimal import Decimal
from typing import Dict, Any, Optional
import datetime
from src.exceptions import ComplianceViolationException

class PayoutEngine:
    """
    6493 Sayılı Kanun Uyumlu Otomatik Dağıtım Motoru (TCMB Lisanssız Mevduat/Havuz Tutma Önleyici)
    """
    MAX_ALLOWABLE_HOLD_DAYS = 3  # İfa sonrası en fazla 3 iş günü içinde PSP transferi zorunludur

    @classmethod
    def execute_t1_payout_schedule(
        cls,
        settlement_record: Dict[str, Any],
        host_iban: str,
        execution_time: Optional[datetime.datetime] = None
    ) -> Dict[str, Any]:
        """
        QR Check-in ile kesinleşen bakiyenin host IBAN'ına zorunlu T+1 transfer emrini oluşturur.
        Host bakiyeyi platformda biriktirmek istese dahi bu işlem BLOKE EDİLİR.
        """
        if not host_iban or not host_iban.startswith("TR") or len(host_iban.replace(" ", "")) != 26:
            raise ValueError(f"Geçersiz Türkiye IBAN formatı: {host_iban}")

        status = settlement_record.get("status")
        if status != "SETTLED":
            raise ComplianceViolationException(
                "Yalnızca QR Check-in ile kesinleşmiş (SETTLED) bakiyeler transfere konu edilebilir."
            )

        now = execution_time or datetime.datetime.utcnow()
        # T+1 iş günü transfer zamanlaması
        payout_due_date = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        payout_amount = settlement_record.get("host_payout") or settlement_record.get("data", {}).get("split_details", {}).get("splits", {}).get("net_supplier_payout", {}).get("amount")
        if not payout_amount:
            payout_amount = settlement_record.get("net_host_payout", 0.0)

        return {
            "payout_id": f"PO_{settlement_record.get('payment_id', 'TXN')}",
            "recipient_iban": host_iban.replace(" ", ""),
            "amount": payout_amount,
            "currency": "TRY",
            "payout_schedule": "AUTOMATIC_T_PLUS_ONE",
            "scheduled_transfer_date": payout_due_date,
            "status": "QUEUED_FOR_PSP_DIRECT_SETTLEMENT",
            "regulatory_compliance": "LAW_6493_ZERO_DEPOSIT_HOLD",
            "description": "LORAKS Etkinlik Hakedişi - Otomatik Lisanslı PSP Hakediş Transferi"
        }

    @classmethod
    def reject_unlicensed_wallet_deposit_request(cls, host_request: Dict[str, Any]):
        """
        Host'un 'Parayı içeride tutun, ay sonu toplu gönderin' talebini 6493 S.K. gereği reddeder.
        """
        if host_request.get("request_type") == "HOLD_FUNDS_ACCUMULATED_MONTH_END":
            raise ComplianceViolationException(
                "6493 Sayılı Kanun Madde 12/15 Uyarınca: LORAKS bir banka veya TCMB lisanslı "
                "ödeme kuruluşu değildir. Hakedişler platform bünyesinde vadesiz hesap gibi biriktirilemez; "
                "ifayı takiben T+1 iş gününde host banka hesabına zorunlu olarak aktarılmalıdır."
            )
