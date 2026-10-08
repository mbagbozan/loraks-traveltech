"""
LORAKS TRAVELTECH — COMPLIANCE AUTOMATION & MONTE CARLO TEST SUITE (v3.0)
Testing:
- 10,000 Monte Carlo transaction exact cent reconciliation
- KVK m. 13 Sanal POS fee isolation invariant
- TÜRSAB 1618 & TUREB 6326 guided tour & transport locks
- AI Audit RegTech P2 masking keyword detection
- Reverse flow escrow zero-tax refund vs settled tax amendment
"""

import unittest
from decimal import Decimal
import random
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.tax_engine import calculate_split_and_withholding, quantize_money
from src.pathway_engine import PathwayEngine
from src.payment_engine import PaymentEngine
from src.refund_engine import RefundEngine
from src.ai_audit_agent import scan_listing_for_p2_masking
from src.exceptions import (
    ComplianceViolationException,
    InvalidPathwayException,
    FinancialReconciliationException
)

class TestLoraksComplianceAutomation(unittest.TestCase):

    def test_monte_carlo_10k_transactions_exact_cent_accuracy(self):
        """10.000 Rastgele Bilet Satışında Decimal Kuruş Mutabakat Testi (Zero Cent Discrepancy)"""
        for _ in range(10000):
            rand_val = Decimal(str(round(random.uniform(10.0, 50000.0), 2)))
            res = calculate_split_and_withholding(rand_val)
            
            # Kuruş Şaşmama Testi: Brüt = Platform Komisyonu (Net+KDV) + 360 Stopaj + Net Host Hakedişi
            sum_parts = res['loraks_gross_commission'] + res['withholding_tax_360'] + res['host_payout']
            self.assertEqual(rand_val, sum_parts)

    def test_kvk_13_pos_fee_isolation_exception(self):
        """KVK m.13: POS Masrafı Yanlış Şirkete Aktarılırsa Custom Exception Fırlatılıyor mu?"""
        engine = PaymentEngine()
        
        class DummyTxnIllegal:
            pathway_code = 'P0'
            merchant_entity = 'LORAKS_ACENTA_AS'
            gross_amount = Decimal('1000.00')
            pos_commission_rate = Decimal('0.028')
            
        with self.assertRaises(ComplianceViolationException):
            engine.process_pos_fee_allocation(DummyTxnIllegal())

        class DummyTxnP2Illegal:
            pathway_code = 'P2'
            merchant_entity = 'LORAKS_TEKNOLOJI_AS'
            gross_amount = Decimal('2000.00')
            pos_commission_rate = Decimal('0.028')
            
        with self.assertRaises(ComplianceViolationException):
            engine.process_pos_fee_allocation(DummyTxnP2Illegal())

        # Doğru Dağıtımlar Başarılı Olmalıdır
        class DummyTxnP0Valid:
            pathway_code = 'P0'
            merchant_entity = 'LORAKS_TEKNOLOJI_AS'
            gross_amount = Decimal('1000.00')
            pos_commission_rate = Decimal('0.028')

        res_p0 = engine.process_pos_fee_allocation(DummyTxnP0Valid())
        self.assertEqual(res_p0['company'], "LORAKS_TEKNOLOJI_AS")
        self.assertEqual(res_p0['account_code'], "653_COMMISSION_EXPENSE_TEK")
        self.assertEqual(res_p0['pos_fee_amount'], Decimal('28.00'))

        class DummyTxnP2Valid:
            pathway_code = 'P2'
            merchant_entity = 'LORAKS_ACENTA_AS'
            gross_amount = Decimal('2000.00')
            pos_commission_rate = Decimal('0.028')

        res_p2 = engine.process_pos_fee_allocation(DummyTxnP2Valid())
        self.assertEqual(res_p2['company'], "LORAKS_ACENTA_AS")
        self.assertEqual(res_p2['account_code'], "653_COMMISSION_EXPENSE_ACE")
        self.assertEqual(res_p2['pos_fee_amount'], Decimal('56.00'))

    def test_1618_tursab_and_6326_tureb_guided_tour_lock(self):
        """Rehberli Tur (has_guided_tour) Varsa P2 ve Acente POS Zorunlu mu?"""
        listing = {"title": "Tarihi Yarımada Yürüyüş Turu", "has_guided_tour": True}
        config = PathwayEngine.determine_payment_gateway(listing)
        
        self.assertEqual(config['merchant_id'], "ACENTA_IYZICO_MERCHANT_ID")
        self.assertEqual(config['contract_type'], "PACKAGE_TOUR_CONTRACT_PTS")
        self.assertEqual(config['seller_title'], "LORAKS SEYAHAT ACENTASI A.Ş.")
        self.assertTrue(config['mandatory_insurance_required'])

    def test_p0_workshop_gateway_routing(self):
        """Sabit mekanlı atölye P0 Teknoloji POS yönlendirmesi doğrulaması"""
        listing = {"title": "Seramik Şekillendirme Atölyesi", "category": "workshop"}
        config = PathwayEngine.determine_payment_gateway(listing)
        
        self.assertEqual(config['merchant_id'], "TEKNOLOJI_IYZICO_MERCHANT_ID")
        self.assertEqual(config['contract_type'], "MARKETPLACE_USER_AGREEMENT")
        self.assertEqual(config['seller_title'], "LORAKS TEKNOLOJİ A.Ş.")
        self.assertFalse(config['mandatory_insurance_required'])

    def test_ai_audit_agent_p2_keyword_detection(self):
        """Yapay zeka NLP tarayıcısının gizli paket tur ifadelerini yakalama testi"""
        masked_text = "Hafta sonu doğa yürüyüşümüz Kadıköy servis kalkış noktası ile başlayacaktır."
        self.assertTrue(scan_listing_for_p2_masking(masked_text))

        innocent_text = "Kadıköy stüdyomuzda 2 saatlik suluboya atölyesi. Boyalar ve tuval fiyata dahildir."
        self.assertFalse(scan_listing_for_p2_masking(innocent_text))

    def test_refund_engine_escrow_vs_settled(self):
        """İade motorunun QR check-in öncesi ve sonrası vergi davranışları"""
        refund_engine = RefundEngine()
        
        class MockBooking:
            gross_amount = Decimal('1200.00')

        # Check-in öncesi: Sıfır vergi bürokrasisi, tam iade
        res_pre = refund_engine.process_refund_allocation(MockBooking(), is_checkin_completed=False)
        self.assertEqual(res_pre['status'], "ZERO_TAX_INSTANT_REFUND")
        self.assertEqual(res_pre['refund_to_guest'], Decimal('1200.00'))
        self.assertEqual(res_pre['withholding_reversal'], Decimal('0.00'))

        # Check-in sonrası: 7524 S.K. düzeltme beyannamesi tetiklenmeli
        res_post = refund_engine.process_refund_allocation(MockBooking(), is_checkin_completed=True)
        self.assertEqual(res_post['status'], "TAX_AMENDMENT_SETTLED_REFUND")
        self.assertEqual(res_post['refund_to_guest'], Decimal('1200.00'))
        self.assertEqual(res_post['withholding_reversal'], Decimal('10.00')) # 1200 / 1.20 * 0.01 = 10.00 TL
        self.assertTrue(res_post['tax_amendment_required'])

    def test_intercompany_billing_kvk_13_cost_plus(self):
        """KVK m.13: Şirketler arası bedelsiz hizmet yasağı ve emsal maliyet artı faturalama testi"""
        from src.intercompany_billing import IntercompanyBillingEngine

        # Bedelsiz altyapı aktarımı istisna fırlatmalıdır
        with self.assertRaises(ComplianceViolationException):
            IntercompanyBillingEngine.calculate_monthly_intercompany_invoice(
                p2_gross_turnover=Decimal('500000.00'),
                allocated_shared_costs=Decimal('0.00'),
                method="COST_PLUS"
            )

        # 50.000 TL sunucu/personel maliyetinde %10 emsal kâr ve %20 KDV hesabı
        res = IntercompanyBillingEngine.calculate_monthly_intercompany_invoice(
            p2_gross_turnover=Decimal('500000.00'),
            allocated_shared_costs=Decimal('50000.00'),
            method="COST_PLUS"
        )
        self.assertEqual(res['base_amount_net'], Decimal('55000.00')) # 50.000 * 1.10
        self.assertEqual(res['vat_amount'], Decimal('11000.00'))      # 55.000 * 0.20
        self.assertEqual(res['total_invoice_amount'], Decimal('66000.00'))
        self.assertEqual(res['invoice_type'], "B2B_E_FATURA_YONETIM_VE_YAZILIM_BEDELI")

    def test_package_tour_mandatory_insurance_bsmv_isolation(self):
        """P2 turlarda KDV'den istisna olan Zorunlu Seyahat Sigortası matrah ayrıştırma testi"""
        # 2.000 TL bilet, 50 TL Zorunlu Sigorta
        res = calculate_split_and_withholding(
            gross_amount=Decimal('2000.00'),
            mandatory_insurance_cost=Decimal('50.00'),
            pathway_code="P2"
        )
        # KDV matrahı 1.950 TL üzerinden hesaplanmalı (2000 - 50)
        self.assertEqual(res['taxable_service_gross'], Decimal('1950.00'))
        self.assertEqual(res['mandatory_insurance_cost_bsmv'], Decimal('50.00'))
        # 1950 / 1.20 = 1625.00 TL matrah; %1 stopaj = 16.25 TL
        self.assertEqual(res['net_sales_base'], Decimal('1625.00'))
        self.assertEqual(res['withholding_tax_360'], Decimal('16.25'))

    def test_cancellation_penalty_tax_exemption_indemnity(self):
        """No-show ve iptal kesintilerinde stopajsız/KDV'siz cayma tazminatı doğrulaması"""
        from src.tax_engine import calculate_cancellation_penalty_taxation
        penalty_res = calculate_cancellation_penalty_taxation(Decimal('1000.00'))
        self.assertEqual(penalty_res['tax_status'], "INDEMNITY_NON_TAXABLE_UNDER_7524")
        self.assertEqual(penalty_res['withholding_tax_360'], Decimal('0.00'))
        self.assertEqual(penalty_res['vat_applicable'], Decimal('0.00'))
        self.assertEqual(penalty_res['host_penalty_payout'], Decimal('700.00'))
        self.assertEqual(penalty_res['platform_penalty_retention'], Decimal('300.00'))

    def test_6493_payout_engine_t1_and_unlicensed_hold_prevention(self):
        """6493 S.K.: QR sonrası otomatik T+1 transferi ve hostun 'içeride biriktirin' talebinin engellenmesi"""
        from src.payout_engine import PayoutEngine

        # Host içeride tutma talebi gönderirse kanunen reddedilmeli
        with self.assertRaises(ComplianceViolationException):
            PayoutEngine.reject_unlicensed_wallet_deposit_request({
                "request_type": "HOLD_FUNDS_ACCUMULATED_MONTH_END"
            })

        # QR Check-in ile kesinleşmiş bakiye T+1 transfer emrine dönüşmeli
        settlement_mock = {
            "payment_id": "PAY_999",
            "status": "SETTLED",
            "host_payout": Decimal('1683.33')
        }
        payout_cmd = PayoutEngine.execute_t1_payout_schedule(
            settlement_record=settlement_mock,
            host_iban="TR33 0006 1005 1978 6457 8410 01"
        )
        self.assertEqual(payout_cmd['regulatory_compliance'], "LAW_6493_ZERO_DEPOSIT_HOLD")
        self.assertEqual(payout_cmd['payout_schedule'], "AUTOMATIC_T_PLUS_ONE")
        self.assertEqual(payout_cmd['amount'], Decimal('1683.33'))

    def test_scenario_a_multi_stop_turing_warranty_enforcement(self):
        """Senaryo A: Çok duraklı gezilerde TUREB kokartı yoksa taahhüt kutusu zorunlu mu?"""
        from src.safe_harbor_filters import SafeHarborComplianceFilter

        # Kokart yok ve taahhüt yoksa -> İSTİSNA FIRLATILMALI
        listing_bad = {"is_multi_stop": True, "has_tourist_guide_license": False, "non_guiding_warranty_accepted": False}
        with self.assertRaises(ComplianceViolationException):
            SafeHarborComplianceFilter.evaluate_multi_stop_turing_lock(listing_bad)

        # Kokart yok ama taahhüt kabul edilmişse -> Onaylanmalı ve disclaimera eklenmeli
        listing_ok = {"is_multi_stop": True, "has_tourist_guide_license": False, "non_guiding_warranty_accepted": True}
        res = SafeHarborComplianceFilter.evaluate_multi_stop_turing_lock(listing_ok)
        self.assertEqual(res['status'], "APPROVED_WITH_LEGAL_DISCLAIMER")
        self.assertTrue(res['safe_harbor_logged'])

    def test_scenario_b_overnight_camping_mandatory_p2(self):
        """Senaryo B: Kendi aracıyla gelse bile geceleme/çadır varsa P2 kilitlenmeli"""
        from src.safe_harbor_filters import SafeHarborComplianceFilter
        camp_listing = {"category": "camp", "overnight": True, "transport_arranged": "none"}
        self.assertTrue(SafeHarborComplianceFilter.enforce_overnight_p2_lock(camp_listing))

    def test_scenario_c_offplatform_payment_and_chat_masking(self):
        """Senaryo C: İlan metninde elden ödeme taraması ve sohbette IBAN/telefon maskeleme"""
        from src.safe_harbor_filters import SafeHarborComplianceFilter
        from src.ai_audit_agent import scan_offplatform_payment

        # İlan metni taraması
        listing_txt = "Atölye ücreti 500 TL olup, transfer ve yemek ücreti otobüste elden şoföre verilecektir."
        audit_res = scan_offplatform_payment(listing_txt)
        self.assertTrue(audit_res['detected'])
        self.assertEqual(audit_res['action_required'], "QUARANTINE_LISTING")

        # Sohbet mesajı maskeleme
        msg = "Merhaba, ücretin kalanını TR33 0006 1005 1978 6457 8410 01 nolu IBAN'a veya 0532 111 22 33 noya nakit gönderin."
        chat_res = SafeHarborComplianceFilter.scan_and_mask_chat_message(msg)
        self.assertTrue(chat_res['violation_detected'])
        self.assertIn("[GÜVENLİK NEDENİYLE GİZLENMİŞ IBAN]", chat_res['sanitized_message'])
        self.assertIn("[GÜVENLİK NEDENİYLE GİZLENMİŞ TELEFON]", chat_res['sanitized_message'])
        self.assertIn("[KAYIT DIŞI İŞLEM UYARISI]", chat_res['sanitized_message'])

    def test_scenario_d_gvk9_exemption_cap_tracker(self):
        """Senaryo D: GVK m.9 Esnaf Muaflığı %80 uyarısı ve %100 rezervasyon blokajı"""
        from src.safe_harbor_filters import SafeHarborComplianceFilter
        cap = Decimal('1000000.00')

        # %85 ciroda uyarı vermeli
        warn_res = SafeHarborComplianceFilter.check_gvk9_exemption_cap(
            cumulative_annual_gmv=Decimal('820000.00'),
            new_booking_amount=Decimal('30000.00'),
            annual_cap=cap
        )
        self.assertEqual(warn_res['status'], "WARNING_APPROACHING_LIMIT")
        self.assertEqual(warn_res['ratio_used'], 85.0)

        # 1.000.000 TL aşımında doğrudan rezervasyon blokajı
        with self.assertRaises(ComplianceViolationException):
            SafeHarborComplianceFilter.check_gvk9_exemption_cap(
                cumulative_annual_gmv=Decimal('990000.00'),
                new_booking_amount=Decimal('20000.00'),
                annual_cap=cap
            )

    def test_scenario_f_supper_club_home_alcohol_ban(self):
        """Senaryo F: Evde yemek deneyimlerinde alkol yasağı ve alerjen beyan şartı"""
        from src.safe_harbor_filters import SafeHarborComplianceFilter

        # Evde alkol servisi denenirse -> TAPDK YASAĞI FIRLATILMALI
        bad_home_bar = {"venue_type": "home", "alcohol_served": True, "category": "food"}
        with self.assertRaises(ComplianceViolationException):
            SafeHarborComplianceFilter.validate_supper_club_and_alcohol(bad_home_bar)

        # Alerjen beyanı olmadan yemek atölyesi açılamaz
        no_allergen = {"venue_type": "studio", "alcohol_served": False, "category": "food", "allergen_declaration_accepted": False}
        with self.assertRaises(ComplianceViolationException):
            SafeHarborComplianceFilter.validate_supper_club_and_alcohol(no_allergen)

        # Yasal kriterleri sağlayan stüdyo yemek atölyesi
        valid_dining = {"venue_type": "studio", "alcohol_served": False, "category": "food", "allergen_declaration_accepted": True}
        valid_res = SafeHarborComplianceFilter.validate_supper_club_and_alcohol(valid_dining)
        self.assertEqual(valid_res['status'], "APPROVED")


if __name__ == '__main__':
    unittest.main()
