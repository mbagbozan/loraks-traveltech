"""
AUTOMATED TEST SUITE FOR LORAKS FINTECH SPLIT PAYMENT & TAX ENGINE
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from payment_engine import PaymentEngine

class TestPaymentEngine(unittest.TestCase):

    def setUp(self):
        self.engine = PaymentEngine()

    def test_split_calculation_1000_try(self):
        """Verify exact 1,000 TL split with gross tax basis: 150 TL Platform, 10 TL GİB, 840 TL Host."""
        res = self.engine.calculate_split(1000.00, pathway_code="P0", tax_basis="gross")
        splits = res["splits"]
        
        self.assertEqual(splits["platform_take_rate"]["gross_amount"], 150.00)
        self.assertEqual(splits["tax_withholding_gib"]["amount"], 10.00)
        self.assertEqual(splits["supplier_net_payout"]["net_amount"], 840.00)
        
        # Cent-level sum integrity
        total_sum = round(
            splits["platform_take_rate"]["gross_amount"] +
            splits["tax_withholding_gib"]["amount"] +
            splits["supplier_net_payout"]["net_amount"],
            2
        )
        self.assertEqual(total_sum, 1000.00)

    def test_split_calculation_2000_try_net_matrah(self):
        """
        Verify the official Master Plan v5.1 unit economics on 2.000 TL ticket:
        - Gross Ticket: 2.000,00 TL
        - Platform Commission (%15 KDV Incl): 300,00 TL (250 TL matrah + 50 TL KDV)
        - Law 7524 %1 Withholding on KDV-excl matrah (2000 / 1.20 = 1666.67 * 0.01): 16,67 TL
        - Net Supplier Payout: 1.683,33 TL
        - Sanal POS Absorbed (~2.8%): 56,00 TL
        - Platform Net Cash Retention: 244,00 TL
        """
        res = self.engine.calculate_split(2000.00, pathway_code="P0", tax_basis="net_matrah")
        splits = res["splits"]

        self.assertEqual(splits["platform_take_rate"]["gross_amount"], 300.00)
        self.assertEqual(splits["platform_take_rate"]["net_matrah"], 250.00)
        self.assertEqual(splits["platform_take_rate"]["kdv_20"], 50.00)
        self.assertEqual(splits["platform_take_rate"]["pos_fee_absorbed"], 56.00)
        self.assertEqual(splits["platform_take_rate"]["net_cash_retention"], 244.00)

        self.assertEqual(splits["tax_withholding_gib"]["amount"], 16.67)
        self.assertEqual(splits["supplier_net_payout"]["net_amount"], 1683.33)

        # Cent-level mathematical equation verification: 300.00 + 16.67 + 1683.33 = 2000.00
        total_sum = round(
            splits["platform_take_rate"]["gross_amount"] +
            splits["tax_withholding_gib"]["amount"] +
            splits["supplier_net_payout"]["net_amount"],
            2
        )
        self.assertEqual(total_sum, 2000.00)

    def test_cancel_and_refund_from_escrow(self):
        """
        Verify Reverse Flow Protection:
        Cancellation before QR check-in refunds 100% from escrow with ZERO tax remittance.
        """
        key = "idemp_cancel_key_444"
        charge_res = self.engine.process_charge("BK-CANCEL-1", 2000.00, key, "P0")
        payment_id = charge_res["data"]["payment_id"]

        # Cancel while in escrow
        refund_res = self.engine.cancel_and_refund(payment_id, reason="BAD_WEATHER_CANCEL")
        self.assertEqual(refund_res["status"], "REFUNDED")
        self.assertEqual(refund_res["data"]["status"], "REFUNDED")
        self.assertEqual(refund_res["data"]["refund_type"], "PURE_ESCROW_REVERSAL_ZERO_TAX_PENALTY")

    def test_split_calculation_p2_regulated_travel(self):
        """Verify P2 regulated travel with 12% tech take-rate."""
        res = self.engine.calculate_split(2500.00, pathway_code="P2", tax_basis="gross")
        splits = res["splits"]
        
        # 12% of 2500 = 300.00 TL
        self.assertEqual(splits["platform_take_rate"]["gross_amount"], 300.00)
        # 1% withholding = 25.00 TL
        self.assertEqual(splits["tax_withholding_gib"]["amount"], 25.00)
        # Net agency/host payout = 2500 - 300 - 25 = 2175.00 TL
        self.assertEqual(splits["supplier_net_payout"]["net_amount"], 2175.00)
        
        # Verify TFRS 15 B2C issuer is the Licensed Travel Agency
        self.assertIn("TÜRSAB A Grubu", res["invoicing"]["b2c_customer_invoice"]["issuer"])

    def test_idempotent_payment_charge(self):
        """Verify idempotency key prevents duplicate charges."""
        key = "idemp_test_unique_key_12345"
        
        # 1st charge
        res1 = self.engine.process_charge(
            booking_id="BK-001",
            gross_amount=1000.00,
            idempotency_key=key,
            pathway_code="P0"
        )
        self.assertEqual(res1["status"], "SUCCESS")
        payment_id = res1["data"]["payment_id"]
        
        # 2nd charge with same key (Replay)
        res2 = self.engine.process_charge(
            booking_id="BK-001",
            gross_amount=1000.00,
            idempotency_key=key,
            pathway_code="P0"
        )
        self.assertEqual(res2["status"], "IDEMPOTENT_REPLAY")
        self.assertEqual(res2["data"]["payment_id"], payment_id)

    def test_settlement_escrow_release(self):
        """Verify escrow settles and records QR check-in."""
        key = "idemp_settle_key_999"
        res = self.engine.process_charge("BK-002", 1500.00, key, "P0")
        payment_id = res["data"]["payment_id"]
        
        settle_res = self.engine.settle_payment(payment_id, verified_by_qr=True)
        self.assertEqual(settle_res["status"], "SETTLED")
        self.assertEqual(settle_res["data"]["status"], "SETTLED")
        self.assertEqual(settle_res["data"]["verification_method"], "QR_CHECKIN")

if __name__ == "__main__":
    unittest.main()
