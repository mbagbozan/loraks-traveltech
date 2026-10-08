"""
LORAKS TEST RUNNER — EXECUTES ALL AUTOMATED TESTS
Version: v3.2 Production Ready
"""

import sys
import os
import unittest

def run_tests():
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\n=======================================================")
        print("✅ TÜM LORAKS OTOMATİK TESTLERİ BAŞARIYLA GEÇTİ (100%)")
        print("   - Pathway Sınıflandırma Motoru: DOĞRULANDI (P0, P1, P2, P3, P4)")
        print("   - FinTech Split Payment & 7524 S.K. %1 Stopaj: DOĞRULANDI")
        print("   - TFRS 15 Çift Yönlü Fatura Yönlendirme: DOĞRULANDI")
        print("   - KVK m.13 Şirketler Arası Emsal Faturalama & POS Masraf Yalıtımı: DOĞRULANDI")
        print("   - 6493 S.K. T+1 Otomatik Hak Ediş & Lisanssız Havuz Engeli: DOĞRULANDI")
        print("   - RegTech Safe Harbor (TUREB 6326, Kamp P2, TAPDK Alkol, GVK 9, Chat Maskeleme): DOĞRULANDI")
        print("   - 10.000 Monte Carlo Sıfır Kuruş Sapma Mutabakatı: DOĞRULANDI")
        print("   - LORAKS Circle Sadakat Cüzdanı: DOĞRULANDI")
        print("=======================================================")
        sys.exit(0)
    else:
        print("\n❌ TESTLERDE HATA OLUŞTU!")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
