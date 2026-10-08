# src/payment_engine.py
from decimal import Decimal
from src.exceptions import ComplianceViolationException, InvalidPathwayException

class PaymentEngine:
    def process_pos_fee_allocation(self, booking_transaction):
        """
        KVK m. 13 Uyumlu POS Masraf Ayrım Motoru
        """
        merchant_entity = booking_transaction.merchant_entity  # TEKNOLOJI_AS veya ACENTA_AS
        pos_fee_amount = booking_transaction.gross_amount * booking_transaction.pos_commission_rate

        # YASAL KISIT (INVARIANT): Masrafı ödeyen şirket, ciroyu yazan şirket ile BİREBİR aynı olmalıdır!
        if booking_transaction.pathway_code in ['P0', 'P1']:
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
                "account_code": "653_COMMISSION_EXPENSE_TEK",
                "amount": pos_fee_amount,
                "company": "LORAKS_TEKNOLOJI_AS"
            }
            
        elif booking_transaction.pathway_code == 'P2':
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
                "account_code": "653_COMMISSION_EXPENSE_ACE",
                "amount": pos_fee_amount,
                "company": "LORAKS_ACENTA_AS"
            }
        else:
            raise InvalidPathwayException(f"Geçersiz Pathway Kodu: {booking_transaction.pathway_code}")
