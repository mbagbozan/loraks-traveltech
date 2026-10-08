# src/refund_engine.py
from decimal import Decimal
from src.tax_engine import quantize_money

class RefundEngine:
    def process_refund_allocation(self, booking_transaction, is_checkin_completed: bool = False) -> dict:
        """
        İade / İptal Anında Vergi ve POS Komisyonu Düzeltme Motoru
        """
        gross_amount = booking_transaction.gross_amount
        
        if not is_checkin_completed:
            # QR Check-in öncesi iptal: Vergi henüz GİB'e ödenmedi (Zero-Tax Full Refund)
            return {
                "refund_to_guest": gross_amount,
                "withholding_reversal": Decimal('0.00'),
                "commission_reversal": Decimal('0.00'),
                "status": "ZERO_TAX_INSTANT_REFUND"
            }
        else:
            # QR Check-in sonrası iptal: GİB 7524 S.K. Muhtasar Düzeltme Beyannamesi Kaydı Atılır
            net_sales_base = quantize_money(gross_amount / Decimal('1.20'))
            withholding_reversal = quantize_money(net_sales_base * Decimal('0.01'))
            
            return {
                "refund_to_guest": gross_amount,
                "withholding_reversal": withholding_reversal,
                "tax_amendment_required": True,
                "status": "TAX_AMENDMENT_SETTLED_REFUND"
            }
