"""
LORAKS TRAVELTECH — LORAKS CIRCLE LOYALTY & WALLET LEDGER
Compliant with: Law 6493 (Non-Cashable, Single-Merchant Discount Credits)
"""

from typing import Dict, Any, List
import uuid
import datetime

class WalletLedger:
    INVITE_REWARD_POINTS = 500.00    # 500 LORAKS Puanı for successful invitation
    BOOKING_REWARD_PERCENT = 0.05    # 5% of booking value credited as future discount points

    def __init__(self):
        # In-memory store: buyer_id -> { "available": float, "pending": float }
        self.wallets: Dict[str, Dict[str, float]] = {}
        # In-memory transactions list
        self.transactions: List[Dict[str, Any]] = []

    def get_or_create_wallet(self, buyer_id: str) -> Dict[str, float]:
        if buyer_id not in self.wallets:
            self.wallets[buyer_id] = {"available": 0.00, "pending": 0.00}
        return self.wallets[buyer_id]

    def credit_points(
        self,
        buyer_id: str,
        points: float,
        reference_type: str,
        reference_id: str,
        description: str
    ) -> Dict[str, Any]:
        """
        Credits non-cashable loyalty discount points to a user's wallet.
        """
        if points <= 0:
            raise ValueError("Kazanılan puan pozitif bir değer olmalıdır.")

        wallet = self.get_or_create_wallet(buyer_id)
        wallet["available"] = round(wallet["available"] + points, 2)

        tx = {
            "transaction_id": f"TX-{uuid.uuid4().hex[:10].upper()}",
            "buyer_id": buyer_id,
            "points": points,
            "transaction_type": "EARN",
            "reference_type": reference_type,
            "reference_id": reference_id,
            "description": description,
            "balance_after": wallet["available"],
            "created_at": datetime.datetime.utcnow().isoformat()
        }
        self.transactions.append(tx)
        return tx

    def redeem_points(
        self,
        buyer_id: str,
        points_to_spend: float,
        booking_id: str
    ) -> Dict[str, Any]:
        """
        Redeems loyalty discount points against a booking.
        """
        wallet = self.get_or_create_wallet(buyer_id)
        if wallet["available"] < points_to_spend:
            raise ValueError(f"Yetersiz LORAKS Puanı. Mevcut: {wallet['available']}, İstenen: {points_to_spend}")

        wallet["available"] = round(wallet["available"] - points_to_spend, 2)

        tx = {
            "transaction_id": f"TX-{uuid.uuid4().hex[:10].upper()}",
            "buyer_id": buyer_id,
            "points": -points_to_spend,
            "transaction_type": "SPEND",
            "reference_type": "BOOKING_DISCOUNT",
            "reference_id": booking_id,
            "description": f"{booking_id} nolu rezervasyonda kullanılan ticari sadakat indirimi.",
            "balance_after": wallet["available"],
            "created_at": datetime.datetime.utcnow().isoformat()
        }
        self.transactions.append(tx)
        return tx
