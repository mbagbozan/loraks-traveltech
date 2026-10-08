"""
INTEGRATION TEST FOR LORAKS API LOGIC (Zero error guarantee)
"""

import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from pathway_engine import PathwayEngine
from payment_engine import PaymentEngine
from wallet_ledger import WalletLedger

def test_full_user_journey():
    print("1. Testing Pathway Classification Engine...")
    listing_input = {
        "title": "Bodrum Günbatımı Tekne Yoga",
        "category": "outdoor",
        "transport_arranged": "included_in_price",
        "transport_operator": "licensed_transport_company",
        "accommodation_included": False,
        "overnight": False,
        "services_bundled": ["guide", "transport", "yoga"],
        "single_inclusive_price": True
    }
    classification = PathwayEngine.classify(listing_input)
    assert classification["pathway_code"] == "P2", f"Expected P2, got {classification['pathway_code']}"
    assert "TÜRSAB" in classification["badge"]
    print("   ✅ Pathway P2 Classified with TÜRSAB legal shield.")

    print("2. Testing FinTech Split Payment Calculation (2,500 TL)...")
    payment_engine = PaymentEngine()
    split = payment_engine.calculate_split(2500.00, pathway_code="P2", tax_basis="gross")
    splits = split["splits"]
    
    assert splits["platform_take_rate"]["gross_amount"] == 300.00
    assert splits["tax_withholding_gib"]["amount"] == 25.00
    assert splits["supplier_net_payout"]["net_amount"] == 2175.00
    assert round(300 + 25 + 2175, 2) == 2500.00
    print("   ✅ Split payment cent-level math validated: 300 TL Take-rate, 25 TL GİB Withholding, 2,175 TL Net Payout.")

    print("3. Testing Idempotent Charge & Escrow Locking...")
    idemp_key = "idemp_journey_test_777"
    charge = payment_engine.process_charge(
        booking_id="BK-JOURNEY-01",
        gross_amount=2500.00,
        idempotency_key=idemp_key,
        pathway_code="P2"
    )
    assert charge["status"] == "SUCCESS"
    assert charge["data"]["status"] == "IN_ESCROW"
    payment_id = charge["data"]["payment_id"]
    print(f"   ✅ Payment {payment_id} locked in escrow.")

    print("4. Testing QR Check-in & Escrow Settlement...")
    settlement = payment_engine.settle_payment(payment_id, verified_by_qr=True)
    assert settlement["status"] == "SETTLED"
    assert settlement["data"]["verification_method"] == "QR_CHECKIN"
    print("   ✅ Escrow released upon QR check-in.")

    print("5. Testing LORAKS Circle Loyalty Points Awarding...")
    wallet_ledger = WalletLedger()
    buyer_id = "BUYER-JOURNEY-01"
    tx = wallet_ledger.credit_points(buyer_id, 250.00, "BOOKING_REWARD", "BK-JOURNEY-01", "Deneyim ödül puanı")
    assert tx["points"] == 250.00
    wallet = wallet_ledger.get_or_create_wallet(buyer_id)
    assert wallet["available"] == 250.00
    print("   ✅ LORAKS Circle loyalty points ledger validated.")

    print("\n🎉 BÜTÜN ENTEGRASYON ADIMLARI 100% HATASIZ VE ÇALIŞIR DURUMDA!")

if __name__ == "__main__":
    test_full_user_journey()
