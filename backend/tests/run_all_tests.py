# tests/run_all_tests.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from decimal import Decimal
import random
from src.tax_engine import calculate_split_and_withholding
from src.pathway_engine import PathwayEngine
from src.payment_engine import PaymentEngine
from src.exceptions import ComplianceViolationException
from src.ai_audit_agent import scan_listing_for_p2_masking

class TestLoraksComplianceAutomation(unittest.TestCase):

    def test_monte_carlo_10k_transactions_exact_cent_accuracy(self):
        """10.000 Rastgele Bilet Satışında Decimal Kuruş Mutabakat Testi"""
        for _ in range(10000):
            rand_val = Decimal(str(round(random.uniform(100.0, 50000.0), 2)))
            res = calculate_split_and_withholding(rand_val)
            
            # Kuruş Şaşmama Testi: Bütün parçaların toplamı brüt tutara kuruşu kuruşuna eşit olmalıdır!
            sum_parts = res['loraks_net_revenue'] + res['loraks_vat'] + res['withholding_tax_360'] + res['host_payout']
            self.assertEqual(rand_val, sum_parts)

    def test_kvk_13_pos_fee_isolation_exception(self):
        """KVK m.13: POS Masrafı Yanlış Şirkete Aktarılırsa Custom Exception Fırlatılıyor mu?"""
        engine = PaymentEngine()
        
        class DummyTxn:
            pathway_code = 'P0'
            merchant_entity = 'LORAKS_ACENTA_AS'  # P0 işleminde Acente POS'u çağrılmaya çalışılıyor (YASAK!)
            gross_amount = Decimal('1000.00')
            pos_commission_rate = Decimal('0.028')
            
        with self.assertRaises(ComplianceViolationException):
            engine.process_pos_fee_allocation(DummyTxn())

    def test_1618_tursab_and_6326_tureb_guided_tour_lock(self):
        """Rehberli Tur (has_guided_tour) Varsa P2 ve Acente POS Zorunlu mu?"""
        pathway = PathwayEngine()
        
        listing = {"title": "Tarihi Yarımada Yürüyüş Turu", "has_guided_tour": True}
        config = pathway.determine_payment_gateway(listing)
        
        self.assertEqual(config['merchant_id'], "ACENTA_IYZICO_MERCHANT_ID")
        self.assertEqual(config['contract_type'], "PACKAGE_TOUR_CONTRACT_PTS")

    def test_ai_audit_agent_catches_masked_p2(self):
        """Host P0 Atölye dese bile metinde otobüs/transfer varsa AI yakalıyor mu?"""
        text_with_transfer = "Seramik atölyemiz için Kadıköy'den servis kalkış noktası belirlenmiştir."
        self.assertTrue(scan_listing_for_p2_masking(text_with_transfer))
        
        pure_workshop = "Kendi atölyemizde 2 saat boyunca çamur tornasında vazo yapacağız."
        self.assertFalse(scan_listing_for_p2_masking(pure_workshop))

if __name__ == '__main__':
    unittest.main()
