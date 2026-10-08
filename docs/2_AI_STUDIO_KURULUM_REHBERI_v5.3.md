# LORAKS TravelTech — Google AI Studio Proje Kurulum Kılavuzu (v5.3 Ready)

Bu dosya, [Google AI Studio](https://aistudio.google.com/)'da yeni bir proje/prompt açtığınızda birebir kopyalayıp yapıştırarak sistemi anında canlıya almanız için hazırlanmıştır.

---

## 1. PROJE VE MODEL AYARLARI (Sağ Panel)

* **Prompt Tipi:** `Chat Prompt` (veya `Structured Prompt`)
* **Model:** `Gemini 1.5 Pro` (Önerilen) veya `Gemini 1.5 Flash`
* **Temperature:** `0.0` veya `0.1` *(Matematiksel ve yasal kuralların şaşmaması için sıfıra yakın tutun)*
* **Structured Output (JSON Mode):** `AÇIK (Enabled)`

---

## 2. SYSTEM INSTRUCTIONS (Sistem Talimatı Kutusu)

Google AI Studio'nun sol üstündeki **"System Instructions"** alanına aşağıdaki metnin tamamını yapıştırın:

```text
Sen LORAKS TravelTech platformunun Akıllı RegTech Karar ve Uyum Motorusun (Host OS & Compliance Engine).
Görevin; platforma kayıt olan ev sahiplerinin (host) profilini doğrulamak, girdikleri deneyimleri Türkiye mevzuatına (1618 S.K. TÜRSAB, 6326 S.K. TUREB, 6563 S.K. E-Ticaret, 7524 S.K. Vergi Tevkifatı, TAPDK) göre otomatik sınıflandırmak (P0-P4 Pathway), sorumlu tüzel kişiliği ve ödeme geçidini belirlemek ve TFRS 15 kurallarına göre kuruşu kuruşuna denk finansal hak ediş tablosunu üretmektir.

TEMEL YASAL VE FİNANSAL ÇALIŞMA KURALLARIN:

1. PATHWAY SINIFLANDIRMA VE İKİLİ ŞİRKET MİMARİSİ:
- P0 (Sabit Atölye - Doğrudan Uygun): Etkinlik tek bir sabit mekanda (mutfak, seramik stüdyosu, marangozhane) gerçekleşir. Ulaşım, geceleme, rehberli rota yoktur. Alkol satışı/ikramı yoktur.
  • Sorumlu Şirket: LORAKS Teknoloji A.Ş. (6563 S.K. ETAHS - Aracı Hizmet Sağlayıcı).
  • Sözleşme: 07_Pazaryeri_Hizmet_Sozlesmesi + 08_Organizator_Sozlesmesi.
  • TFRS 15 Muhasebesi: VEKİL (Agent). Yalnızca %15 komisyon ciro yazılır.
  • Stopaj: 7524 S.K. %1 pazar yeri stopajı kesilir.
  • POS Masrafı (%2,8): LORAKS Teknoloji A.Ş. bilançosunda kalır (KVK m.13).

- P1 (Sertifikalı / Doğrulanmış Üretici): Gıda hijyen belgesi, ustalık belgesi, federasyon lisansı yüklenmiş üretici. P0 statüsündedir, doğrulanmış rozetle yayınlanır.

- P2 (Lisanslı Tur / Kamp - Acente Kalkanı): Araçla transfer, konaklama, geceleme, çok günlük program veya TUREB 6326 S.K. kapsamında profesyonel turist rehberi eşliğinde tarihi/kültürel rota içeren tüm deneyimler ZORUNLU P2'dir.
  • Sorumlu Şirket: LORAKS Seyahat Acentası A.Ş. (T.C. Kültür ve Turizm Bakanlığı TÜRSAB Belge No: 2387).
  • Sözleşme: 05_Mesafeli_Satis_Sozlesmesi (Paket Tur Sözleşmesi) + Zorunlu Paket Tur Sigortası.
  • TFRS 15 Muhasebesi: ASİL (Principal). Bilet bedelinin TAMAMI acente cirosu yazılır (600).
  • Stopaj: 7524 S.K. pazar yeri stopajı uygulanmaz (0.00 TL); tedarikçiye (otel/rehber) e-Fatura veya SMM karşılığı 621 Satılan Hizmet Maliyeti üzerinden ödeme yapılır.
  • POS Masrafı (%2,8): LORAKS Seyahat Acentası A.Ş. bilançosunda kalır (KVK m.13).

- P3 (Gelişim ve Belge Desteği Bekleyen): Zorunlu mesleki veya hijyen belgesi eksik olan ilanlar yayınlanmaz; taslak (Draft) statüsünde tutulur ve rehberlik kartı açılır.

- P4 (Lisanslı Taşıyıcıya Sevk): Şahsi araçla korsan yolcu taşıma girişimi engellenir; D2 lisanslı taşıyıcılara devredilmek üzere yönlendirilir.

2. KRİTİK DENETİM VE KISIT MOTORU:
- NLP Maskeleme Taraması: Host deneyim tipini "P0 Atölye" seçse dahi; metinde "otobüs", "servis kalkış noktası", "transfer", "geceleme", "otel", "rehber eşliğinde", "kalkış saati", "örenyeri" kelimeleri geçiyorsa ilanı otomatik P2'ye çek ve "AI_MASKED_P2_DETECTED" bayrağı ekle.
- TAPDK Evde Alkol Yasağı: venue_type "home" (ev mutfağı/supper club) iken alkol satışı/ikramı varsa ilanı derhal REDDET ("TAPDK_HOME_ALCOHOL_PROHIBITED"). Bağ turları yalnızca açık içki ruhsatlı lisanslı tesislerde ve P2 kalkanında yapılabilir.
- No-Show Cezai Şartı: Misafirin son 24 saatte gelmemesi durumunda kesilen tutar cayma tazminatıdır; KDV ve 7524 stopajı hesaplanmaz.
- KVK m.13 Kısıtı: Hiçbir şirket diğerinin POS masrafını üstlenemez. Şirketler arası masraf rücusu yasaktır.
- Esnaf Muafiyeti Takibi: host_ytd_sales_amount yasal tavanın %80'ini aşarsa "ESNAF_MUAFIYETI_CAP_WARNING" bayrağı ekle ve şirketleşme çağrısı yap.

3. FİNANSAL FORMÜLLER VE KURUŞ MUTABAKATI:
- P0 İçin (Vekil):
  • Brüt Bilet = GMV
  • LORAKS Komisyonu = Brüt x 0.15 (KDV Dahil)
  • LORAKS Net Satışlar (600) = Komisyon / 1.20
  • LORAKS KDV (391) = Komisyon - Net Satışlar
  • KDV Hariç Satış Matrahı = Brüt / 1.20
  • 7524 S.K. %1 Stopajı (360) = Satış Matrahı x 0.01
  • Host Net Hak Edişi = Brüt - Komisyon - Stopaj
  • Sağlama: Komisyon + Stopaj + Host Hak Edişi == Brüt Fiyat.
- P2 İçin (Asil):
  • Resmi Ciro (600) = Brüt / 1.20
  • Hesaplanan KDV (391) = Brüt - Resmi Ciro
  • Tedarikçi/Host Maliyeti (621) = Brüt x 0.85 (Acente kalan brüt kârı: %15)
  • 7524 Stopajı = 0.00 TL.

4. DİL VE YAKLAŞIM (CREATOR ENABLEMENT):
Host'a asla suçlayıcı konuşma. "Yasa dışısın" deme. "Etkinliğiniz yasal koruma amacıyla LORAKS Seyahat Acentası A.Ş. operasyon kalkanına yönlendirilmiştir" diyerek güven veren bir ortak dili kullan.

ÇIKTI KURALI:
Yanıtını DAİMA aşağıda tanımlanan JSON şemasına tam uyumlu tek bir JSON nesnesi olarak üret.
```

---

## 3. STRUCTURED OUTPUT JSON SCHEMA (Şema Ayarı)

Google AI Studio'nun sağ panelindeki **"Response Schema"** alanına aşağıdaki şemayı yapıştırın:

```json
{
  "type": "object",
  "properties": {
    "listing_audit": {
      "type": "object",
      "properties": {
        "listing_id": { "type": "string" },
        "title": { "type": "string" },
        "assigned_pathway": { "type": "string", "enum": ["P0", "P1", "P2", "P3", "P4"] },
        "merchant_entity": { "type": "string", "enum": ["LORAKS_TEKNOLOJI_AS", "LORAKS_ACENTA_AS"] },
        "contract_type": { "type": "string", "enum": ["MARKETPLACE_USER_AGREEMENT", "PACKAGE_TOUR_CONTRACT_PTS", "PENDING_DOCUMENTATION"] },
        "compliance_flags": { "type": "array", "items": { "type": "string" } },
        "is_approved_for_publish": { "type": "boolean" },
        "creator_enablement_message": { "type": "string" },
        "social_promo_story_copy": { "type": "string" }
      },
      "required": ["listing_id", "title", "assigned_pathway", "merchant_entity", "contract_type", "compliance_flags", "is_approved_for_publish", "creator_enablement_message"]
    },
    "financial_settlement": {
      "type": "object",
      "properties": {
        "accounting_model": { "type": "string", "enum": ["TFRS_15_AGENT_NET", "TFRS_15_PRINCIPAL_GROSS"] },
        "gross_amount": { "type": "number" },
        "revenue_recognition_600": { "type": "number" },
        "calculated_vat_391": { "type": "number" },
        "withholding_tax_360": { "type": "number" },
        "host_or_supplier_payout": { "type": "number" },
        "pos_fee_allocation": {
          "type": "object",
          "properties": {
            "amount": { "type": "number" },
            "charged_to_company": { "type": "string", "enum": ["LORAKS_TEKNOLOJI_AS", "LORAKS_ACENTA_AS"] }
          },
          "required": ["amount", "charged_to_company"]
        },
        "reconciliation_verified": { "type": "boolean" }
      },
      "required": ["accounting_model", "gross_amount", "revenue_recognition_600", "calculated_vat_391", "withholding_tax_360", "host_or_supplier_payout", "pos_fee_allocation", "reconciliation_verified"]
    }
  },
  "required": ["listing_audit", "financial_settlement"]
}
```

---

## 4. ON UÇTAN UCA TESTİN TAMAMI (Girdiler ve Beklenen Yanıtlar)

Sistemi AI Studio'da test etmek için aşağıdaki 10 senaryoyu sohbete sırayla yapıştırın:

### TEST 1: P0 — Sabit Mekan Seramik Atölyesi (Esnaf Muafiyeti)
* **Sohbete Yapıştırılacak JSON:**
```json
{
  "listing_id": "LST-001",
  "title": "Kadıköy Çamur Tornası Seramik Atölyesi",
  "description": "Kendi stüdyomuzda 2 saat killi çamur ile fincan ve kase yapımı. Çay ikramı dahildir.",
  "gross_price": 1000.0,
  "venue_type": "studio",
  "has_transport": false,
  "has_accommodation": false,
  "has_guided_tour": false,
  "serves_alcohol": false,
  "host_tax_profile": "INDIVIDUAL_EXEMPT"
}
```
* **Beklenen Sonuç:**
  * `assigned_pathway`: `"P0"` | `merchant_entity`: `"LORAKS_TEKNOLOJI_AS"`
  * `accounting_model`: `"TFRS_15_AGENT_NET"` | `revenue_recognition_600`: `125.00` | `calculated_vat_391`: `25.00`
  * `withholding_tax_360`: `8.33` | `host_or_supplier_payout`: `841.67` | `is_approved_for_publish`: `true`

---

### TEST 2: P1 — Gıda Hijyen Belgeli Şef Sofrası (Doğrulanmış Rozet)
* **Sohbete Yapıştırılacak JSON:**
```json
{
  "listing_id": "LST-002",
  "title": "Moda'da Yerel Ege Zeytinyağlıları Tadımı",
  "description": "Şef mutfağında 4 çeşit zeytinyağlı yapımı ve tadımı.",
  "gross_price": 1500.0,
  "venue_type": "commercial_kitchen",
  "has_transport": false,
  "has_accommodation": false,
  "has_guided_tour": false,
  "serves_alcohol": false,
  "has_food_hygiene_certificate": true,
  "host_tax_profile": "SOLE_PROPRIETOR"
}
```
* **Beklenen Sonuç:**
  * `assigned_pathway`: `"P1"` | `merchant_entity`: `"LORAKS_TEKNOLOJI_AS"`
  * `compliance_flags`: `["VERIFIED_FOOD_SAFETY_BADGE"]` | `is_approved_for_publish`: `true`

---

### TEST 3: P2 — Konaklamalı Doğa & Yoga Kampı (Açık Paket Tur)
* **Sohbete Yapıştırılacak JSON:**
```json
{
  "listing_id": "LST-003",
  "title": "Assos 2 Gece 3 Gün Yoga ve Meditasyon İnzivası",
  "description": "Assos taş otelde 2 gece konaklama, sabah-akşam yoga ve nefes çalışmaları.",
  "gross_price": 8500.0,
  "venue_type": "hotel_retreat",
  "has_transport": false,
  "has_accommodation": true,
  "has_guided_tour": false,
  "serves_alcohol": false,
  "host_tax_profile": "CORPORATE"
}
```
* **Beklenen Sonuç:**
  * `assigned_pathway`: `"P2"` | `merchant_entity`: `"LORAKS_ACENTA_AS"` | `contract_type`: `"PACKAGE_TOUR_CONTRACT_PTS"`
  * `accounting_model`: `"TFRS_15_PRINCIPAL_GROSS"` | `revenue_recognition_600`: `7083.33` (Brüt bilet matrahı)
  * `calculated_vat_391`: `1416.67` | `withholding_tax_360`: `0.00` | `host_or_supplier_payout`: `7225.00`

---

### TEST 4: P2 — Maskelenmiş Doğa Gezisi (AI Metin Taraması)
* **Sohbete Yapıştırılacak JSON:**
```json
{
  "listing_id": "LST-004",
  "title": "Haftasonu Kazdağları Buluşması",
  "description": "Doğada nefes çalışması. Sabah Kadıköy servis kalkış noktasından hareket edip şelaleye gideceğiz.",
  "gross_price": 2000.0,
  "venue_type": "outdoor",
  "has_transport": false,
  "has_accommodation": false,
  "has_guided_tour": false,
  "serves_alcohol": false,
  "host_tax_profile": "INDIVIDUAL_EXEMPT"
}
```
* **Beklenen Sonuç:**
  * Metindeki *"servis kalkış noktası"* ifadesi yakalanır -> `assigned_pathway`: `"P2"`
  * `compliance_flags`: `["AI_MASKED_P2_DETECTED"]` | `merchant_entity`: `"LORAKS_ACENTA_AS"`

---

### TEST 5: P2 — Tarihi Kültür Yürüyüşü (TUREB 6326 Kokart Kuralı)
* **Sohbete Yapıştırılacak JSON:**
```json
{
  "listing_id": "LST-005",
  "title": "Balat ve Fener Kültür Rotası",
  "description": "Balat sokaklarında 4 saatlik tarihi kiliseler ve mimari anlatımlı yürüyüş.",
  "gross_price": 750.0,
  "venue_type": "heritage_route",
  "has_transport": false,
  "has_accommodation": false,
  "has_guided_tour": true,
  "has_tureb_licensed_guide": false,
  "serves_alcohol": false,
  "host_tax_profile": "INDIVIDUAL_EXEMPT"
}
```
* **Beklenen Sonuç:**
  * Kokartlı rehber olmadığı için tek başına P0 olamaz -> `assigned_pathway`: `"P2"`
  * `compliance_flags`: `["TUREB_GUIDE_REQUIRED"]` | `merchant_entity`: `"LORAKS_ACENTA_AS"`

---

### TEST 6: P3 — Belge Eksiği Olan Atölye (Taslakta Bekletme)
* **Sohbete Yapıştırılacak JSON:**
```json
{
  "listing_id": "LST-006",
  "title": "Temel Dövme ve İğne Sanatı Atölyesi",
  "description": "Kendi atölyemde suni deri üzerinde dövme yapım teknikleri eğitimi.",
  "gross_price": 3000.0,
  "venue_type": "studio",
  "has_transport": false,
  "has_accommodation": false,
  "has_guided_tour": false,
  "has_sterilization_permit": false,
  "serves_alcohol": false,
  "host_tax_profile": "INDIVIDUAL_NON_EXEMPT"
}
```
* **Beklenen Sonuç:**
  * `assigned_pathway`: `"P3"` | `is_approved_for_publish`: `false`
  * `contract_type`: `"PENDING_DOCUMENTATION"`
  * `creator_enablement_message`: *"Sterilizasyon ve hijyen belgeniz yüklenene kadar ilanınız taslak olarak korunmaktadır."*

---

### TEST 7: P4 — Şahsi Araçla Korsan Transfer Girişimi (Yolcu Taşıma Kuralı)
* **Sohbete Yapıştırılacak JSON:**
```json
{
  "listing_id": "LST-007",
  "title": "Kendi Arabamla Sizi Alıp Belgrad Ormanı'nda Yürüyüşe Götürüyorum",
  "description": "Katılımcıları kendi binek arabamla evlerinden alıp ormana götüreceğim.",
  "gross_price": 1200.0,
  "venue_type": "outdoor",
  "transport_mode": "ORGANISER_PRIVATE_VEHICLE",
  "has_transport": true,
  "has_accommodation": false,
  "serves_alcohol": false,
  "host_tax_profile": "INDIVIDUAL_EXEMPT"
}
```
* **Beklenen Sonuç:**
  * `assigned_pathway`: `"P4"` | `is_approved_for_publish`: `false`
  * `compliance_flags`: `["ILLEGAL_PRIVATE_VEHICLE_TRANSPORT"]`
  * `creator_enablement_message`: *"Karayolu Taşıma Kanunu uyarınca şahsi araçla transfer yapılamaz. Transfer D2 lisanslı araçlara yönlendirilmelidir."*

---

### TEST 8: TAPDK Kalkanı — Evde Şarap / Alkol İkramı (Ev Ortamı Yasağı)
* **Sohbete Yapıştırılacak JSON:**
```json
{
  "listing_id": "LST-008",
  "title": "Cihangir Evde İtalyan Makarnası ve Şarap Eşleşmesi",
  "description": "Evimin salonunda taze makarna yapıp yanında özel butik şaraplar tadacağız.",
  "gross_price": 1800.0,
  "venue_type": "home",
  "has_transport": false,
  "has_accommodation": false,
  "has_guided_tour": false,
  "serves_alcohol": true,
  "host_tax_profile": "INDIVIDUAL_EXEMPT"
}
```
* **Beklenen Sonuç:**
  * `is_approved_for_publish`: `false`
  * `compliance_flags`: `["TAPDK_HOME_ALCOHOL_PROHIBITED"]`
  * `creator_enablement_message`: *"TAPDK mevzuatı gereğince ev ortamında biletli alkol sunumu yasal değildir. Menüden alkolü çıkararak ilanınızı yayınlayabilirsiniz."*

---

### TEST 9: TAPDK Kalkanı — Lisanslı Tesiste Bağ Bozumu & Şarap Tadımı (Yasal Model)
* **Sohbete Yapıştırılacak JSON:**
```json
{
  "listing_id": "LST-009",
  "title": "Urla Bağ Yolu Hasat ve Şarap Tadım Gezisi",
  "description": "Urla'da TAPDK açık içki ruhsatlı lisanslı bağ evinde hasat ve şarap tadımı.",
  "gross_price": 4500.0,
  "venue_type": "licensed_winery",
  "has_transport": true,
  "has_accommodation": false,
  "has_guided_tour": true,
  "serves_alcohol": true,
  "host_tax_profile": "CORPORATE"
}
```
* **Beklenen Sonuç:**
  * `assigned_pathway`: `"P2"` | `merchant_entity`: `"LORAKS_ACENTA_AS"`
  * `compliance_flags`: `["TAPDK_LICENSED_FACILITY_VERIFIED"]` | `is_approved_for_publish`: `true`

---

### TEST 10: Esnaf Muafiyeti Yıllık Ciro Limiti (Cap Tracker)
* **Sohbete Yapıştırılacak JSON:**
```json
{
  "listing_id": "LST-010",
  "title": "Geleneksel Ebru Sanatı Atölyesi",
  "description": "2 saatlik ebru yapımı çalışması.",
  "gross_price": 1200.0,
  "venue_type": "studio",
  "has_transport": false,
  "has_accommodation": false,
  "has_guided_tour": false,
  "serves_alcohol": false,
  "host_tax_profile": "INDIVIDUAL_EXEMPT",
  "host_ytd_sales_amount": 950000.0
}
```
* **Beklenen Sonuç:**
  * `assigned_pathway`: `"P0"` | `merchant_entity`: `"LORAKS_TEKNOLOJI_AS"`
  * `compliance_flags`: `["ESNAF_MUAFIYETI_CAP_WARNING"]`
  * `creator_enablement_message`: *"Yıllık esnaf muafiyeti limitinize yaklaştınız. SMMM kuluçkamız üzerinden şahıs şirketi kuruluş sürecinizi başlatabilirsiniz."*
