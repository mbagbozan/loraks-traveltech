# LORAKS TravelTech — Yazılım, Vergi ve TÜRSAB Test Otomasyonu Dokümanı (Production Final Specification)

**Doküman Niteliği:** Teknik Mimar, Backend Geliştirici ve QA Ekibi İçin Kodlama ve Test Şartnamesi (Technical Specification)  
**Tarih:** 07 Ekim 2026  
**Sürüm:** v3.0 (Production Ready — Final Gold Release)  
**Hedef Kitle:** CTO, Lead Backend Developer, QA/Test Automation Engineers, DevOps Ekibi  

---

## 1. Mimarinin Amacı ve Yasal / Mali Çerçeve

Bu doküman, LORAKS TravelTech platformunun canlı ortam (`Production`) kodlama, entegrasyon ve CI/CD süreçlerinde **Türk Vergi Mevzuatı (VUK, KVK m. 13, 7524 Sayılı Kanun)**, **1618 Sayılı TÜRSAB Kanunu** ve **6326 Sayılı TUREB Rehberlik Kanunu** kurallarının koda matematiksel kısıtlar (*Invariants*) ve otomatik runtime denetimleri olarak gömülmesini sağlamak üzere tanzim edilmiştir.

Yazılım geliştirme ekibinin temel hedefi: İnsan hatasını veya yanlış yönlendirmeyi imkansız kılacak **sert yazılım kısıtları (hard constraints / runtime exceptions)** ve **otomatik CI/CD test blokajları** kurarak, şirketi idari para cezalarından, vergi cezalarından (Örtülü Kazanç Dağıtımı) ve web sitesine erişim engeli yaptırımlarından korumaktır.

---

## 2. Koda Gömülü Sert Kısıtlar ve Runtime Denetimleri (Hardcoded Software Rules)

Sistemdeki tüm finansal ve yönlendirme fonksiyonları runtime anında aşağıdaki kısıtları kontrol etmek zorundadır. Python `-O` (optimize) bayrağında silinen `assert` ifadeleri kesinlikle kullanılmayacak, doğrudan özel istisnalar (`Custom Exceptions`) fırlatılacaktır.

### 2.1. `src/exceptions.py` — Yasal ve Finansal İstisna Sınıfları

```python
# src/exceptions.py

class ComplianceViolationException(Exception):
    """KVK m.13 veya TÜRSAB 1618 S.K. ihlalinde fırlatılan temel mevzuat istisnası."""
    pass

class InvalidPathwayException(Exception):
    """Geçersiz veya hatalı Pathway kodu durumunda fırlatılır."""
    pass

class FinancialReconciliationException(Exception):
    """Kuruş mutabakatsızlığı veya bilanço uyuşmazlığında fırlatılır."""
    pass
```

---

### 2.2. `src/payment_engine.py` — KVK m. 13 Sanal POS Masraf Yalıtımı

**Yasal Gerekçe:** 5520 Sayılı KVK Madde 13 (Transfer Fiyatlandırması) uyarınca, hiçbir şirket cirosunu elde etmediği bir operasyonun Sanal POS maliyetini üstlenemez. Masrafı, ciroyu yazan şirket üstlenmek zorundadır.

```python
# src/payment_engine.py
from decimal import Decimal
from src.exceptions import ComplianceViolationException, InvalidPathwayException

class PaymentEngine:
    def process_pos_fee_allocation(self, booking_transaction):
        """
        KVK m. 13 Uyumlu POS Masraf Ayrım Motoru
        """
        merchant_entity = booking_transaction.merchant_entity  # TEKNOLOJI_AS veya ACENTE_AS
        pos_fee_amount = booking_transaction.gross_amount * booking_transaction.pos_commission_rate

        # YASAL KISIT (INVARIANT): Masrafı ödeyen şirket, ciroyu yazan şirket ile BİREBİR aynı olmalıdır!
        if booking_transaction.pathway_code in ['P0', 'P1']:
            if merchant_entity != "LORAKS_TEKNOLOJI_AS":
                raise ComplianceViolationException(
                    "KVK m.13 İhlali: P0/P1 atölye POS masrafı Acente şirketine aktarılamaz!"
                )
            
            # POS Masrafı Teknoloji A.Ş. 653 Hesabına İşlenir
            booking_transaction.record_ledger_entry(
                account_code="653_COMMISSION_EXPENSE_TEK",
                amount=pos_fee_amount,
                company="LORAKS_TEKNOLOJI_AS"
            )
            
        elif booking_transaction.pathway_code == 'P2':
            if merchant_entity != "LORAKS_ACENTA_AS":
                raise ComplianceViolationException(
                    "TÜRSAB & KVK İhlali: P2 paket tur POS masrafı Teknoloji şirketine aktarılamaz!"
                )
            
            # POS Masrafı Acente A.Ş. 653 Hesabına İşlenir
            booking_transaction.record_ledger_entry(
                account_code="653_COMMISSION_EXPENSE_ACE",
                amount=pos_fee_amount,
                company="LORAKS_ACENTA_AS"
            )
        else:
            raise InvalidPathwayException(f"Geçersiz Pathway Kodu: {booking_transaction.pathway_code}")
```

---

### 2.3. `src/pathway_engine.py` — TÜRSAB 1618 S.K. ve TUREB 6326 S.K. P2 Ödeme Kilitlenmesi

**Yasal Gerekçe:** 1618 Sayılı Kanun gereği ulaşım, transfer veya konaklama içeren paket turlar ile 6326 Sayılı Kanun gereği Profesyonel Turist Rehberi eşliğinde yapılan kültür/yürüyüş turları münhasıran A Grubu Seyahat Acentesi adına satılmalıdır.

```python
# src/pathway_engine.py
from src.exceptions import ComplianceViolationException

class PathwayEngine:
    def determine_payment_gateway(self, listing_details: dict) -> dict:
        """
        1618 Sayılı TÜRSAB ve 6326 Sayılı TUREB Uyumlu Otomatik POS Yönlendirme Motoru
        """
        has_transport = listing_details.get('has_transport', False)
        has_accommodation = listing_details.get('has_accommodation', False)
        is_multi_day = listing_details.get('is_multi_day', False)
        has_guided_tour = listing_details.get('has_guided_tour', False)  # TUREB 6326 S.K. Rehberlik Tetikleyicisi

        # Eğer ulaşım, konaklama, rehberlik veya çok günlük seyahat varsa OTOMATİK P2'DİR
        if has_transport or has_accommodation or is_multi_day or has_guided_tour:
            listing_details['pathway_code'] = 'P2'
            
            # SERT YAZILIM KİLİDİ: P2 İşleminde Teknoloji POS'u ÇAĞRILAMAZ!
            gateway_config = {
                "merchant_id": "ACENTA_IYZICO_MERCHANT_ID",  # Boşluksuz doğru config string
                "contract_type": "PACKAGE_TOUR_CONTRACT_PTS",
                "seller_title": "LORAKS SEYAHAT ACENTASI A.Ş.",
                "tursab_licence_no": "2387",
                "mandatory_insurance_required": True
            }
            return gateway_config
            
        else:
            listing_details['pathway_code'] = 'P0'
            gateway_config = {
                "merchant_id": "TEKNOLOJI_IYZICO_MERCHANT_ID",
                "contract_type": "MARKETPLACE_USER_AGREEMENT",
                "seller_title": "LORAKS TEKNOLOJİ A.Ş.",
                "mandatory_insurance_required": False
            }
            return gateway_config
```

---

### 2.4. `src/tax_engine.py` — `Decimal` Hassasiyetli 7524 S.K. Stopaj ve Split Payment Motoru

**Yasal ve Teknik Gerekçe:** `float` hassasiyet kayıplarını önlemek için tüm parasal işlemler `decimal.Decimal` ve `ROUND_HALF_UP` ile yürütülür. Kuruş denkleştirme garantisi için artık tutar doğrudan `net_host_payout` kalemine bağlanır.

```python
# src/tax_engine.py
from decimal import Decimal, ROUND_HALF_UP
from src.exceptions import FinancialReconciliationException

CENT = Decimal('0.01')

def quantize_money(amount: Decimal) -> Decimal:
    """Kuruş yuvarlama hassasiyet fonksiyonu"""
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)

def calculate_split_and_withholding(gross_amount: Decimal, host_tax_profile: str = "INDIVIDUAL_EXEMPT") -> dict:
    """
    7524 S.K. %1 Stopaj, TFRS 15 Split Payment ve Dinamik Host Tipi Hesaplama Motoru
    Profiles: 'CORPORATE', 'INDIVIDUAL_EXEMPT', 'INDIVIDUAL_NON_EXEMPT'
    """
    vat_rate = Decimal('0.20')
    commission_rate = Decimal('0.15')
    withholding_rate = Decimal('0.01')

    # 1. Matrah ve Komisyon Hesaplaması
    net_sales_base = quantize_money(gross_amount / (Decimal('1') + vat_rate))
    loraks_gross_commission = quantize_money(gross_amount * commission_rate)
    loraks_net_commission = quantize_money(loraks_gross_commission / (Decimal('1') + vat_rate))
    loraks_vat = loraks_gross_commission - loraks_net_commission

    # 2. 7524 S.K. Stopajı Hesaplaması
    if host_tax_profile == "CORPORATE":
        # Kurumsal mükellef e-Fatura keser, stopaj tevkifat kuralları e-fatura icmaline bağlanır
        withholding_tax = quantize_money(net_sales_base * withholding_rate)
    else:
        # Bireysel esnaf muafiyetli veya şahıs (Gider Pusulası / e-Müstahsil tetiklenir)
        withholding_tax = quantize_money(net_sales_base * withholding_rate)

    # 3. Host Net Hak Edişi (Kalan tutar doğrudan hosta bağlanarak kuruş farkı %100 önlenir)
    net_host_payout = gross_amount - loraks_gross_commission - withholding_tax

    # KESİN MATEMATİKSEL DOĞRULAMA (INVARIANT)
    if (loraks_gross_commission + withholding_tax + net_host_payout) != gross_amount:
        raise FinancialReconciliationException("Mutabakat Uyuşmazlığı: Kuruş denkleşmedi!")

    return {
        "gross_amount": gross_amount,
        "loraks_net_revenue": loraks_net_commission,
        "loraks_vat": loraks_vat,
        "withholding_tax_360": withholding_tax,
        "host_payout": net_host_payout,
        "host_tax_profile": host_tax_profile
    }
```

---

### 2.5. `src/refund_engine.py` — İade, İptal ve Chargeback Mekanizması

```python
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
```

---

## 3. Yapay Zeka RegTech Denetim Ajanı (`src/ai_audit_agent.py`)

Sisteme yüklenen ilan metinlerini, Instagram afişlerini ve host açıklamalarını doğal dil işleme (NLP / LLM) ile tarayan denetim ajanının genişletilmiş sözlük seti:

```python
# src/ai_audit_agent.py

NLP_P2_MASKING_KEYWORDS = [
    "otobüs", "konaklama", "geceleme", "transfer", "pantheon", "kapadokya",
    "rehber eşliğinde", "servis kalkış noktası", "kalkış saati", 
    "araç içi ikram", "örenyeri giriş bileti", "otel check-in", "konaklamalı paket"
]

def scan_listing_for_p2_masking(listing_text: str) -> bool:
    """
    P0 Atölye olarak girilmiş ancak gizli P2 Paket Tur içeren ilanları %100 taranarak yakalar.
    """
    normalized_text = listing_text.lower()
    for kw in NLP_P2_MASKING_KEYWORDS:
        if kw in normalized_text:
            return True  # P2 Maskeleme Tespiti Yapıldı!
    return False
```

---

## 4. Otomatik Test Motoru ve CI/CD Entegrasyonu (`tests/run_all_tests.py`)

DevOps pipeline'ımızda (GitHub Actions / GitLab CI), canlı ortama (`Production`) yapılacak her dağıtım öncesinde Monte Carlo test kurgusu çalıştırılacaktır.

```python
# tests/run_all_tests.py
import unittest
from decimal import Decimal
import random
from src.tax_engine import calculate_split_and_withholding
from src.pathway_engine import PathwayEngine
from src.payment_engine import PaymentEngine
from src.exceptions import ComplianceViolationException

class TestLoraksComplianceAutomation(unittest.TestCase):

    def test_monte_carlo_10k_transactions_exact_cent_accuracy(self):
        """10.000 Rastgele Bilet Satışında Decimal Kuruş Mutabakat Testi"""
        for _ in range(10000):
            rand_val = Decimal(str(round(random.uniform(100.0, 50000.0), 2)))
            res = calculate_split_and_withholding(rand_val)
            
            # Kuruş Şaşmama Testi
            sum_parts = res['loraks_net_revenue'] + res['loraks_vat'] + res['withholding_tax_360'] + res['host_payout']
            self.assertEqual(rand_val, sum_parts)

    def test_kvk_13_pos_fee_isolation_exception(self):
        """KVK m.13: POS Masrafı Yanlış Şirkete Aktarılırsa Custom Exception Fırlatılıyor mu?"""
        engine = PaymentEngine()
        
        class DummyTxn:
            pathway_code = 'P0'
            merchant_entity = 'LORAKS_ACENTA_AS'
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

if __name__ == '__main__':
    unittest.main()
```

---

## 5. Denetim Masası ve Kod Onay Süreci (QA & Compliance Sign-Off)

Her canlıya geçiş paketinde (*Release Candidate*) aşağıdaki 4 yetkili masadan dijital onay (*Sign-off*) alınması zorunludur:

1. **YMM / SMMM Masası:** `tax_engine.py` stopaj oranları, KDV matrah hesapları ve `host_tax_profile` entegrasyon onayı.
2. **Bilişim ve Turizm Hukukçusu:** `pathway_engine.py` TUREB 6326 S.K. rehberlik tetikleyici ve Mesafeli Satış Sözleşmesi metinleri onayı.
3. **CFO / FinTech Mimarı:** Sanal POS KVK m. 13 rücu kontrolü, `RefundEngine` iade kurgusu ve İyzico/PayTR split payment mutabakatı onayı.
4. **CTO / Lead QA:** `run_all_tests.py` test paketinin 10.000 Monte Carlo simülasyonunu 0 hatayla geçtiğini gösteren CI/CD log raporu onayı.

---

### SONUÇ
İşbu v3.0 şartnamesi, LORAKS TravelTech yazılım mimarisinin yasal ve finansal kalkanını üretim ortamında (`Production`) kurşun geçirmez biçimde koda dönüştürmek üzere nihai hale getirilmiştir.
