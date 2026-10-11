# 🌲 LORAKS TravelTech — Universal Experience Marketplace
> **"Türkiye Deneyim Ekonomisi İçin Evrensel Pazaryeri ve Güven Altyapısı"**  
> *Slogan:* **"Kendine Zaman Tanı"** · *Motto:* **"Bir araya gelmenin değerini bilenler için."**

[![Tests](https://img.shields.io/badge/tests-29%2F29%20passing-10B981)](tests/run_all_tests.py)
[![Architecture](https://img.shields.io/badge/architecture-Dual--Entity%20v5.4%20%7C%20Definitive%20Edition-1A432E)](docs/17_loraks_traveltech_nihai_birlesik_master_blueprint_v5_4.md)
[![Compliance](https://img.shields.io/badge/compliance-1618%20%7C%206326%20%7C%206563%20%7C%207524%20%7C%20KVK%2013-D97706)](docs/01_master_plan_v5_1.md)
[![Design](https://img.shields.io/badge/aesthetic-Modern%20Anatolian%20Editorial-8FAF8C)](docs/04_marka_kimligi_ve_gorsel_rehber.md)

---

## 🏛️ 1. Proje Genel Bakışı ve Temel İlke

LORAKS, münferit bir bilet satış motoru ya da indirim sepeti değildir. **LORAKS; yerel zanaatkârları, şef sofralarını, butik atölyeleri ve doğa deneyimlerini; yasal kalkan (1618 S.K.), FinTech split payment, KVK m.13 emsal faturalama ve otomatik %1 vergi tevkifatı (7524 S.K.) ile tek çatı altında toplayan EVRENSEL DENEYİM PAZARYERİDİR.**

> **Temel Stratejik İlke:**  
> *"Tasarımda Kapsamlılık. Kategoride Kontrollü İcraat. Temel Fikri Mülkiyet Olarak Mevzuat ve Güven Altyapısı."*  
> *(Breadth by design. Controlled execution by category. Compliance as core intellectual property.)*

---

## 🧭 2. Evrensel Değer Akışı ve RegTech Safe Harbor Kalkanı (v3.2)

```text
                      EVRENSEL DENEYİM PAZARYERİ
              (Tüketiciler · Üreticiler · Kurumsal B2B)
                                 │
                         KEŞİF & REZERVASYON
                                 │
                        UYUM VE GÜVEN MOTORU
           (Detect ➔ Classify ➔ Assess ➔ Route ➔ Verify)
                                 │
       ┌───────────────┬─────────────────┬───────────────┐
      P0              P1                P2              P3/P4
 Bağımsız Atölye  Sertifikalı Üretici  Lisanslı Acente  Gelişim & D2 Transfer
                                 │
     5'Lİ SAFE HARBOR KALKANI (TUREB 6326, Geceleme P2, TAPDK Alkol, GVK 9, Chat)
                                 │
            PSP SPLIT & VERGİ (%1 STOPAJ & KVK m.13 POS YALITIMI)
                                 │
               GÜVENLİ İFA (QR CHECK-IN & 6493 T+1 TRANSFER)
                                 │
                   BÜYÜME, CIRCLE & B2B İK SATIŞI
```

### 5'li Safe Harbor RegTech Moat (Altın Kurallar):
1. **TUREB 6326 Koruması (Senaryo A):** Çok duraklı sokak gezilerinde kokartsız hostlara dijital 'teknik atölye' taahhüdü şartı.
2. **Geceleme / Kamp P2 Kilidi (Senaryo B):** Kendi aracıyla gelse dahi geceleme/çadır varsa istisnasız lisanslı acente kalkanı ve Zorunlu Sigorta.
3. **Kayıt Dışı Ödeme & Chat Maskeleme (Senaryo C):** İlan metinlerinde elden/nakit taraması; sohbette TR IBAN ve telefon numaralarını otomatik maskeleme.
4. **GVK m.9 Esnaf Muafiyeti Hasılat Tavanı Takibi (Senaryo D):** Yıllık 1.100.000 TL limit takibi, %80 uyarısı ve Vitrin SMMM yönlendirmesi.
5. **TAPDK Supper Club Uyumu (Senaryo F):** Ev ve konut ortamlarında para karşılığı alkollü içki servisi yasağı kilidi ve gıda alerjen formu zorunluluğu.

---

## 🏢 3. İkili Kurumsal Mimari (Dual-Entity Architecture)

Şirketimizi operasyonel risklerden korumak ve yatırımcı değerlemesini (7x–12x SaaS çarpanı) muhafaza etmek için **İkili Şirket Modeli** uygulanmaktadır:

1. **LORAKS Teknoloji A.Ş. (Platform / Aracı Hizmet Sağlayıcı - ETAHS):**  
   * 6563 Sayılı Elektronik Ticaret Kanunu uyarınca pazar yerini işletir.  
   * TFRS 15 uyarınca **"Vekil (Agent)"** rolündedir; yalnızca aldığı **%15 platform hizmet komisyonunu** net hasılat yazar.  
   * Seyahat risklerinden ve ağır acente sermaye blokajlarından yalıtılmıştır.

2. **LORAKS Seyahat Acentası A.Ş. (Operasyon / Lisanslı Seyahat Acentesi):**  
   * 1618 Sayılı Kanun kapsamında T.C. Kültür ve Turizm Bakanlığı & TÜRSAB A Grubu lisansına sahiptir (Mehmet Bağbozan Belge No: 2387).  
   * TFRS 15 uyarınca **"Asil (Principal)"** rolündedir; B2C seyahat faturasını keser ve Zorunlu Paket Tur Sigortasını düzenler.  
   * *Geçiş Dönemi:* Kendi acente tescilimiz tamamlanana kadar anlaşmalı lisanslı Dost Acente protokolü, **Dışsallaştırılmış Risk Tamponu (Özel Mesleki Sorumluluk Sigortası + Rehinli Nakit Teminat Havuzu)** ile güvenceye alınmıştır.

3. **KVK m. 13 Şirketler Arası Emsallere Uygun Hizmet Faturalandırması:**  
   * Teknoloji A.Ş., sunduğu AWS sunucu, yazılım ve müşteri destek altyapısını Acente A.Ş.'ye bedelsiz aktaramaz. Aylık emsal maliyet artı kâr (**%10 Cost-Plus**) B2B e-Faturası düzenlenir.  
   * POS komisyon masrafları ciroyu yazan tüzel kişilikte yalıtılır (`653_COMMISSION_EXPENSE`).

---

## 💳 4. FinTech Birim Ekonomisi ve Tersine Akış Koruması

### 2.000,00 TL Birim Bilet Hesabı

$$\begin{aligned}
\text{Brüt Bilet (Gezgin Öder)} &= \mathbf{2.000,00\text{ TL}} \\
\text{LORAKS Komisyonu (%15, KDV Dahil)} &= 300,00\text{ TL (250 TL Matrah + 50 TL KDV)} \\
\text{Sanal POS Kesintisi (~%2,8)} &= -56,00\text{ TL (LORAKS tarafından karşılanır)} \\
\text{7524 Sayılı Kanun %1 Stopajı} &= -16,67\text{ TL (2.000 / 1,20 = 1.666,67 \times \%1 \rightarrow \text{GİB'e})} \\
\text{Net Host Hak Edişi} &= \mathbf{1.683,33\text{ TL}} \\
\hline
\textbf{Aritmetik Denklem:} & \mathbf{300,00 + 16,67 + 1.683,33 = 2.000,00\text{ TL}} \\
\textbf{LORAKS Net Kasa Retansiyonu:} & 300,00 - 56,00 = \mathbf{244,00\text{ TL}} \text{ (KDV Dahil)}
\end{aligned}$$

* **Tersine Akış (Reverse Flow):** Fonlar QR check-in yapılana kadar TCMB korumalı mutabakat havuzunda saf emanet olarak bekletilir. Erken iptallerde stopaj ve KDV bürokrasisine girmeden %100 iade sağlanır.
* **6493 S.K. T+1 Kuralı:** QR check-in gerçekleştikten sonra host hak edişi en geç T+1 iş gününde otomatik transfer edilir; platformda bakiye biriktirilmesi kanunen engellenir.
* **No-Show ve Cayma Tazminatı:** No-show kesintileri Borçlar Kanunu cayma tazminatı niteliğinde olup KDV ve 7524 stopajından muaftır.

---

## 🎨 5. Görsel Kimlik ve Tasarım Standartları (60-30-10 Kuralı)

* **%60 Zemin (Ham Doğal Keten `#FDFCF8`):** Kinfolk / Cereal editoryal seyahat dergisi ferahlığı.
* **%30 Kurumsal Güven (Derin Çam Yeşili `#1A432E`):** LORAKS logosu, başlıklar, ana butonlar ve TÜRSAB DDS mühürleri.
* **%10 Mikro Sıcaklık (Terrakotta `#C86D51` & Kehribar `#E5A93C`):** Zanaatkar rozetleri, değerlendirme yıldızları ve Kurucu Host madalyonları.
* **Tipografi:** Başlıklarda *Playfair Display / Newsreader* (High-Contrast Serif); arayüzde *Plus Jakarta Sans / Inter*.

---

## 📂 6. Proje Dizin Yapısı

```text
cool-noether/
├── docs/                                    # 📚 Stratejik, Hukuki ve Finansal Dokümantasyon
│   ├── 01_master_plan_v5_1.md               # v5.3 Master Dönüşüm Planı (Unified Architecture & Gold Edition)
│   ├── 02_yonetim_kurulu_ve_ortaklar_sunum_notu.md # Yönetim Kurulu ve Ortaklar Sunum Notu
│   ├── 03_kuresel_iyi_ornekler_ve_buyume_kanallari.md # 5 Stratejik Dikey Benchmark & Büyüme Raporu
│   ├── 04_marka_kimligi_ve_gorsel_rehber.md # 60-30-10 Renk, Logo ve AI Studio Prompt Rehberi
│   ├── 05_smmm_ve_acente_gorusme_dosyasi.md # Muhasebe, Vergi Dairesi ve Sorumlu Müdürlük Dosyası
│   ├── 06_host_os_ve_yan_gelirler.md        # Creator Enablement ve Yan Gelir Kanalları
│   ├── 07_lovable_ve_ai_studio_kurulum_workflow.md # 5 Adımlı Sıfırdan Web Kurulum Akışı
│   ├── 08_one_pager_yatirimci_ozeti.md      # Kurucular ve Yatırımcılar İçin Executive Özet
│   ├── 09_yazilim_ve_vergi_test_otomasyonu_dokumani_v3.md # v3.0 Final Production Test Şartnamesi
│   ├── 10_loraks_preview_master_prompt.md   # Editoryal "Zamana Kilitli Nadir Anlar" Arayüz Promptu
│   ├── 11_creator_academy_ve_kokartli_rehber_agi_raporu.md # Creator Academy & TUREB Rehber Ağı Büyüme Raporu
│   ├── 12_loraks_traveltech_final_master_blueprint_v5_3.md # Nihai Master Proje Blueprinti (Unified Gold v5.3)
│   ├── 13_denetim_simulasyonu_ve_stratejik_kiyaslama.md # Resmi Denetim Simülasyonu & BuArada.com Çapraz Teftiş Raporu
│   ├── 14_loraks_traveltech_uc_uc_analiz_raporu.md # 360° Hukuki, Operasyonel ve Teknik Mimari Analiz Raporu
│   ├── 15_canliya_gecis_master_yapilacaklar_listesi.md # Canlıya Geçiş Master Yapılacaklar Listesi, Zamanlama & Çapraz Eşleşme Matrisi
│   ├── 16_surum_evrimi_ve_eksiklik_analiz_raporu.md # Kronolojik Sürüm Evrim Günlüğü ve Master Blueprint Eksiklik/Çelişki Analizi
│   ├── 17_loraks_traveltech_nihai_birlesik_master_blueprint_v5_4.md # NİHAİ BİRLEŞİK MASTER PROJE BLUEPRINTİ (v5.4 Definitive Edition - Tek Gerçek Kaynak)
│   └── 18_loraks_kurumsal_tanitim_ve_sunum_destesi_revize.md # LORAKS Kurumsal Tanıtım ve Vizyon Sunumu (20 Slaytlık Güncel Deste)
├── src/                                     # ⚙️ Python Uyum, RegTech ve FinTech Çekirdeği
│   ├── pathway_engine.py                    # P0–P4 Kural ve Teşhis Motoru (Creator Enablement)
│   ├── payment_engine.py                    # FinTech Split Payment, %1 Stopaj & KVK 13 POS Yalıtımı
│   ├── safe_harbor_filters.py               # v3.2 Safe Harbor Filtreleri (TUREB, Kamp, Chat, GVK 9, TAPDK)
│   ├── intercompany_billing.py              # KVK m.13 Şirketler Arası Emsal Hizmet & Cost-Plus Faturası
│   ├── tax_engine.py                        # Decimal Hassasiyetli 7524 Stopaj, BSMV & Cayma Tazminatı
│   ├── payout_engine.py                     # 6493 S.K. T+1 Otomatik Hak Ediş & Lisanssız Havuz Engeli
│   ├── refund_engine.py                     # Reverse Flow Sıfır-Vergi Escrow İade ve Vergi Düzeltme
│   ├── ai_audit_agent.py                    # NLP/LLM P2 Paket Tur Maskeleme & Kayıt Dışı Ödeme Dedektörü
│   ├── wallet_ledger.py                     # LORAKS Circle Sadakat Cüzdanı (6493 Uyumlu Ledger)
│   ├── exceptions.py                        # ComplianceViolationException ve Yasal Hata Sınıfları
│   └── server.py                            # Yerel REST API ve Uyum Kokpiti Sunucusu (v3.2)
├── database/                                # 🗄️ Veritabanı ve Şema Tanımları
│   ├── schema.sql                           # PostgreSQL DDL (Merchants, Safe Harbor, Splits, GVK/KVK)
│   └── seed.sql                             # Gerçekçi Tohum Verileri (Şef Sofrası, Atölye, Tekne Yoga, Kamp)
├── frontend/                                # 💻 React / TypeScript Kullanıcı Arayüzü & Kokpit
│   ├── App.tsx                              # Ana Vitrin ve Navigasyon
│   ├── HeroSearch.tsx                       # Doğal Keten Arama Kapsülü
│   ├── ExperienceCard.tsx                   # 4:3 Editoryal Deneyim Kartı
│   ├── HostOnboardingWizard.tsx             # Safe Harbor & SMMM Kuluçkalı 3 Adımlı Host Sihirbazı
│   ├── SocialTemplateGenerator.tsx          # Muvazaa Önleyici TÜRSAB DDS QR Kodlu Sosyal Şablon
│   ├── LORAKSCheckoutUyum.tsx               # TÜRSAB Güvenceli Rezervasyon & Sözleşme Modalı
│   ├── index.html                           # Canlı İnteraktif Uyum, RegTech & FinTech Kokpiti (v3.2)
│   └── types.ts                             # Ortak TypeScript Tipleri (SafeHarbor, GVK9, Intercompany)
└── tests/                                   # 🧪 Otomatik Test Paketi (29 Test - 100% Başarı)
    ├── test_compliance_automation.py        # 10.000 Monte Carlo, KVK 13, Safe Harbor, BSMV, TUREB Testleri
    ├── test_pathway_engine.py               # P0-P4 Pathway Teşhis Testleri
    ├── test_payment_engine.py               # Split Payment, %1 Stopaj & Tersine Akış Testleri
    ├── test_wallet_ledger.py                # Cüzdan Bakiye ve Overdraft Engelleme Testleri
    ├── test_integration.py                  # Uçtan Uca Rezervasyon & QR Check-in Entegrasyonu
    └── run_all_tests.py                     # Master Test Koşturucu
```

---

## 🚀 7. Hızlı Başlangıç ve Doğrulama

### 1. Otomatik Testleri Koşturun (29 Test)
```bash
python3 tests/run_all_tests.py
```
*Tüm kural motorları, 10.000 Monte Carlo kuruş mutabakatı, KVK m.13 POS yalıtımı, Safe Harbor filtreleri ve sadakat cüzdanı kuruşu kuruşuna doğrulanır.*

### 2. Canlı Uyum Kokpitini Başlatın
```bash
python3 src/server.py
```
*Tarayıcınızda `http://localhost:8080` adresine giderek Pathway teşhisi, FinTech split hesaplayıcı, sohbet maskeleme, Safe Harbor kontrolleri ve KVK m.13 faturalama konsolunu anlık olarak test edebilirsiniz.*

---
*© 2026 LORAKS TravelTech Platform. Bütün hakları saklıdır.*
