"""
AUTOMATED TEST SUITE FOR LORAKS CIRCLE WALLET LEDGER
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from wallet_ledger import WalletLedger

class TestWalletLedger(unittest.TestCase):

    def setUp(self):
        self.ledger = WalletLedger()

    def test_points_credit_and_balance(self):
        """Verify non-cashable loyalty points credit and balance tracking."""
        buyer_id = "BUYER-100"
        tx = self.ledger.credit_points(
            buyer_id=buyer_id,
            points=500.00,
            reference_type="INVITATION",
            reference_id="INV-999",
            description="Arkadaş davet sadakat ödülü"
        )
        self.assertEqual(tx["points"], 500.00)
        wallet = self.ledger.get_or_create_wallet(buyer_id)
        self.assertEqual(wallet["available"], 500.00)

    def test_points_redemption(self):
        """Verify loyalty discount point deduction from booking."""
        buyer_id = "BUYER-101"
        self.ledger.credit_points(buyer_id, 300.00, "BOOKING_REWARD", "BK-1", "Ödül")
        
        tx = self.ledger.redeem_points(buyer_id, 100.00, "BK-2")
        self.assertEqual(tx["points"], -100.00)
        
        wallet = self.ledger.get_or_create_wallet(buyer_id)
        self.assertEqual(wallet["available"], 200.00)

    def test_insufficient_points_raises(self):
        """Verify overdraft prevention on loyalty wallet."""
        buyer_id = "BUYER-102"
        self.ledger.credit_points(buyer_id, 50.00, "REWARD", "BK-1", "Ödül")
        
        with self.assertRaises(ValueError):
            self.ledger.redeem_points(buyer_id, 100.00, "BK-2")

if __name__ == "__main__":
    unittest.main()
