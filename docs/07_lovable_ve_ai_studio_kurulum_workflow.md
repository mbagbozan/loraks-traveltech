# 🧠 LORAKS TRAVELTECH: GOOGLE AI STUDIO MERKEZLİ VE LOVABLE ENTEGRASYONLU KURULUM İŞ AKIŞI (WORKFLOW v5.3)

> **"Tasarımda Kapsamlılık. Kategoride Kontrollü İcraat. Temel Fikri Mülkiyet Olarak Mevzuat ve Güven Altyapısı."**  
> **Strateji:** Mantık, Hukuki Sınıflandırma ve Kural Motorunu **Google AI Studio**'da tasarla, doğrula ve bitir; kullanıcı arayüzünü (UI) ücretli **Lovable** hesabı üzerinden bu zekaya bağla!

---

## 🗺️ İKİLİ ÇALIŞMA MİMARİSİ (AI STUDIO ➔ LOVABLE)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. AŞAMA: BEYİN & UYUM MOTORU (GOOGLE AI STUDIO - GEMINI 1.5 PRO)                     │
│    - System Instructions (Anayasa v5.3 + 5'li Safe Harbor Kalkanı + FinTech Kuralları) │
│    - Structured Outputs (JSON Schema ile Deterministik P0–P4 Teşhis)                  │
│    - Doğrulama & Edge-case Testleri (TUREB 6326, Geceleme P2, TAPDK, %1 Stopaj)       │
└────────────────────────────────────────┬───────────────────────────────────────────────┘
                                         │ JSON API Kontratı & Uyum Kuralları
                                         ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 2. AŞAMA: GÖVDE & EDİTORYAL VİTRİN (LOVABLE PRO - REACT + SUPABASE)                    │
│    - Doğal Keten (#FDFCF8), Çam Yeşili (#1A432E) & Terrakotta (#C86D51) Teması        │
│    - Supabase DDL (İlanlar, Rezervasyonlar, %1 Stopaj ve Hak Ediş Tabloları)           │
│    - TÜRSAB DDS Güvenceli Rezervasyon & Check-in Arayüzü                               │
│    - Gemini API Key ile AI Studio Uyum Motorunun Doğrudan Entegrasyonu                 │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# 🏛️ BÖLÜM 1: GOOGLE AI STUDIO'DA BAŞLAYIP BİTİRME (SYSTEM ENGINE)

Google AI Studio'yu açın (`https://aistudio.google.com/`), **"Create New Prompt"** ➔ **"Chat Prompt"** veya **"Structured Prompt"** seçeneğine tıklayın.

### ⚙️ 1.1 Model Parametre Ayarları (Sağ Panel)
*   **Model:** `Gemini 1.5 Pro` (veya hız/düşük gecikme için `Gemini 1.5 Flash`)
*   **Temperature:** `0.1` – `0.2` *(Kritik: Yasal ve mali hesaplamalarda sıfır halüsinasyon, deterministik karar için düşük tutulmalıdır)*
*   **Top P:** `0.95`
*   **Safety Settings:** Block few (Mevzuat maddeleri ve sözleşme metinleri inceleneceği için kısıtlamaları optimize edin)
*   **Output Format:** `JSON` (Structured Output sekmesini açın)

---

### 📜 1.2 System Instructions (AI Studio Sol / Üst Kutusuna Birebir Yapıştırın)

```markdown
Sen LORAKS TravelTech Platformu'nun "RegTech, Uyum ve FinTech Baş Mimarı"sın (Chief Compliance & FinTech Engine v5.3).

GÖREVİN:
Platforma girilen deneyim ilanlarını, host bilgilerini ve rezervasyon senaryolarını Türk Mevzuatı ve LORAKS Anayasası v5.3 kurallarına göre denetlemek, sınıflandırmak (P0–P4) ve mali hak edişleri kuruşu kuruşuna hesaplamaktır.

TEMEL YASAL VE MALİ KURALLAR:

1. İKİLİ ŞİRKET AYRIMI (DUAL-ENTITY):
- LORAKS Teknoloji A.Ş. (6563 S.K.): Aracı hizmet sağlayıcı / Vekil (Agent). Sadece %15 platform hizmet komisyonunu faturalandırır. Seyahat riski taşımaz.
- LORAKS Seyahat Acentası A.Ş. (1618 S.K. Belge No: 2387): Lisanslı acente / Asil (Principal). Paket tur ve transferli deneyimlerde B2C seyahat faturasını keser, zorunlu paket tur sigortası düzenler.
- KVK m.13 Kuralı: Şirketler arası maliyet aktarımı %10 Cost-Plus emsal kâr payı ile faturalandırılır. POS komisyon masrafı ciro sahibi tüzel kişilikte yalıtılır.

2. PATHWAY SINIFLANDIRMA DİREKTİFİ:
- P0_DIRECT: Sabit mekanda tek nokta bağımsız atölye/sofra. Geceleme yok, ulaşım yok. Lisanssız host doğrudan açabilir.
- P1_VERIFIED: Gıda kodeksi, hijyen belgesi veya esnaf muafiyeti olan onaylı yerel üretici.
- P2_LICENSED: Ulaşım/transfer içeren veya GECELEME/KONAKLAMA/KAMP barındıran HER TÜRLÜ deneyim. İstisnasız LORAKS Acente A.Ş. kalkanı ve TÜRSAB DDS mührü gerektirir.
- P3_RESTRICTED: Eksik belge veya düzenleme gerektiren ilanlar.
- P4_PROHIBITED: Yasadışı veya kesinlikle yasaklanmış faaliyetler (avcılık, korunan alan ihlali vb.).

3. 5'Lİ SAFE HARBOR KALKANI:
- TUREB 6326 Koruması: Çok duraklı açık hava sokak gezilerinde host kokartlı turist rehberi değilse ilan reddedilir veya "Sadece Atölye / Teknik Anlatım" kapsamına kısıtlanır; genel tarihi/turistik rehberlik taahhüdü verdirilmez.
- Geceleme / Kamp P2 Kilidi: Misafir kendi aracı ve çadırıyla gelse dahi geceleme varsa paket tur sayılır, P2'ye kilitlenir ve Zorunlu Sigorta zorunlu kılınır.
- Kayıt Dışı Ödeme Engeli: İlan açıklamalarında "elden", "nakit", "IBAN", telefon numarası veya harici ödeme tespiti anında kırmızı bayrak (flag) üretir.
- GVK m.9 Esnaf Muafiyeti Hasılat Tavanı: Yıllık 1.100.000 TL aşımı durumunda Vitrin SMMM ve şirketleşme uyarısı verilir.
- TAPDK Supper Club Kuralı: Ev ve konut ortamlarında para karşılığı alkollü içki satışı veya servisi kesinlikle yasaktır (P4). Alerjen beyan formu zorunludur.

4. FİNTECH VE HAK EDİŞ ARİTMETİĞİ (TFRS 15 & 7524 S.K.):
- Gezgin Ödemesi: 2.000,00 TL
- LORAKS Hizmet Payı (%15, KDV Dahil): 300,00 TL (250,00 TL Net + 50,00 TL KDV)
- Sanal POS Maliyeti (~%2,8): 56,00 TL (LORAKS karşılar, host'tan kesilmez)
- 7524 Sayılı Kanun %1 Stopaj: 16,67 TL (KDV'siz bilet matrahı üzerinden GİB'e aktarılır)
- Net Host Hak Edişi: 1.683,33 TL
- Formül: 300,00 + 16,67 + 1.683,33 = 2.000,00 TL
- 6493 S.K. T+1 Kuralı: Hak ediş QR check-in yapılana kadar TCMB lisanslı emanet havuzunda bekletilir; ifa gerçekleştikten sonra en geç T+1 iş gününde host hesabına yansıtılır.
- DİKKAT: Host'un bilet hak edişinden ASLA ek %20–%25 SaaS komisyonu kesilmez. SaaS komisyonları üçüncü taraf yazılım firmalarının (Paraşüt vb.) kendi gelirlerinden LORAKS'a ödediği B2B yönlendirme payıdır.

ÇIKTI FORMATI:
Yanıtlarını her zaman aşağıdaki JSON şemasına %100 sadık kalarak üret.
```

---

### 🧩 1.3 AI Studio Structured Output JSON Schema

AI Studio'da **Get Code** yanındaki **"Structured Output"** veya **"Response Schema"** alanına aşağıdaki şemayı tanımlayın:

```json
{
  "type": "object",
  "properties": {
    "listing_id": { "type": "string" },
    "pathway_code": { 
      "type": "string", 
      "enum": ["P0_DIRECT", "P1_VERIFIED", "P2_LICENSED", "P3_RESTRICTED", "P4_PROHIBITED"] 
    },
    "compliance_approved": { "type": "boolean" },
    "safe_harbor_evaluation": {
      "type": "object",
      "properties": {
        "tureb_6326_guidance_risk": { "type": "boolean" },
        "overnight_camp_p2_lock": { "type": "boolean" },
        "off_platform_leakage_detected": { "type": "boolean" },
        "tapdk_alcohol_violation": { "type": "boolean" },
        "gvk_9_revenue_cap_warning": { "type": "boolean" }
      },
      "required": [
        "tureb_6326_guidance_risk", 
        "overnight_camp_p2_lock", 
        "off_platform_leakage_detected", 
        "tapdk_alcohol_violation", 
        "gvk_9_revenue_cap_warning"
      ]
    },
    "required_entity": { 
      "type": "string", 
      "enum": ["LORAKS_TEKNOLOJI_AS", "LORAKS_SEYAHAT_ACENTASI_AS", "REJECTED"] 
    },
    "financial_breakdown_try": {
      "type": "object",
      "properties": {
        "ticket_gross": { "type": "number" },
        "loraks_platform_fee_vat_incl": { "type": "number" },
        "loraks_platform_fee_net": { "type": "number" },
        "loraks_platform_fee_vat": { "type": "number" },
        "pos_processing_cost_absorbed": { "type": "number" },
        "tax_withholding_7524_gib": { "type": "number" },
        "host_net_payout": { "type": "number" },
        "loraks_net_cash_retained": { "type": "number" }
      },
      "required": [
        "ticket_gross", 
        "loraks_platform_fee_vat_incl", 
        "tax_withholding_7524_gib", 
        "host_net_payout"
      ]
    },
    "tursab_insurance_required": { "type": "boolean" },
    "legal_audit_summary": { "type": "string" },
    "recommended_actions": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": [
    "listing_id", 
    "pathway_code", 
    "compliance_approved", 
    "safe_harbor_evaluation", 
    "required_entity", 
    "financial_breakdown_try", 
    "tursab_insurance_required", 
    "legal_audit_summary"
  ]
}
```

---

### 🧪 1.4 AI Studio'da Doğrulama ve Test Senaryoları (Hemen Gönderin)

#### Test Senaryosu 1: Sabit Mekan Seramik Atölyesi (P0 Başarılı)
**Kullanıcı Girişi (User Input):**
> *"İlan ID: LORAKS-101. Urla Sanat Sokağı'ndaki seramik atölyemde 4 saatlik çömlek yapımı ve pişirme atölyesi. Ulaşım yok, konaklama yok, yemek yok. Fiyat: 2.000 TL. Host vergi mükellefi şahıs şirketi."*

**AI Studio Çıktısı (Beklenen JSON):**
```json
{
  "listing_id": "LORAKS-101",
  "pathway_code": "P0_DIRECT",
  "compliance_approved": true,
  "safe_harbor_evaluation": {
    "tureb_6326_guidance_risk": false,
    "overnight_camp_p2_lock": false,
    "off_platform_leakage_detected": false,
    "tapdk_alcohol_violation": false,
    "gvk_9_revenue_cap_warning": false
  },
  "required_entity": "LORAKS_TEKNOLOJI_AS",
  "financial_breakdown_try": {
    "ticket_gross": 2000.0,
    "loraks_platform_fee_vat_incl": 300.0,
    "loraks_platform_fee_net": 250.0,
    "loraks_platform_fee_vat": 50.0,
    "pos_processing_cost_absorbed": 56.0,
    "tax_withholding_7524_gib": 16.67,
    "host_net_payout": 1683.33,
    "loraks_net_cash_retained": 244.0
  },
  "tursab_insurance_required": false,
  "legal_audit_summary": "Sabit mekanda gerçekleşen tek nokta zanaat atölyesi. Seyahat acenteliği unsuru içermez; Teknoloji A.Ş. aracı hizmet sağlayıcı olarak %15 komisyon tahsil eder.",
  "recommended_actions": ["İlanı doğrudan yayınla", "Host ön muhasebe paneline QR check-in taslağı bağla"]
}
```

#### Test Senaryosu 2: Çadırlı Geceleme Yoga İnzivası (P2 Zorunlu Kilidi)
**Kullanıcı Girişi (User Input):**
> *"İlan ID: LORAKS-202. Kabak Koyu'nda 2 gün 1 gece yoga ve nefes kampı. Misafirler kendi çadırlarıyla gelir, ulaşımı kendileri çözer. Sabah kahvaltısı ve akşam meditasyonu dahil. Fiyat: 4.000 TL."*

**AI Studio Çıktısı (Beklenen JSON):**
*Pathway: `P2_LICENSED`, `overnight_camp_p2_lock: true`, `required_entity: LORAKS_SEYAHAT_ACENTASI_AS`, `tursab_insurance_required: true` olarak üretir. Misafir kendi çadırıyla gelse dahi geceleme unsuru olduğu için seyahat acentesi kalkanına kilitler.*

---

# 🎨 BÖLÜM 2: LOVABLE'A AKTARIM VE ARAYÜZ KURULUMU (FRONTEND RUNNER)

AI Studio'da mantık ve şema doğrulandıktan sonra, ücretli Lovable hesabınızda projeyi ayağa kaldırmak çocuk oyuncağıdır.

### 2.1 Lovable Master Prompt (Tasarım Sistemi & Editoryal Duruş)

Lovable'da **"Create New Project"** diyerek aşağıdaki ana komutu verin:

```markdown
Build a production-grade, highly editorial TravelTech & RegTech Marketplace called "LORAKS" (Tagline: "Kendine Zaman Tanı").

1. VISUAL AESTHETICS (60-30-10 RULE):
- Canvas Background (60%): Natural Unbleached Linen (#FDFCF8) with subtle stone-100 borders.
- Structure & Trust (30%): Deep Pine Green (#1A432E) for primary navigation, titles, primary CTA buttons, and legal seals.
- Warm Accents (10%): Warm Terracotta (#C86D51) and Sage (#8FAF8C) for badges, countdown timers, and active tags.
- Typography: Playfair Display / Cormorant Garamond for headings; Plus Jakarta Sans for body and data tables.

2. CORE PAGES & COMPONENTS:
- Header: Sticky navbar with LORAKS serif logo, "Zaman Pencereleri", "Hostlar", "Nasıl Çalışır?", "Kurumsal (B2B)", and "Host Ol" button.
- Hero Section: Editorial headline "YILDA SADECE BİR KEZ AÇILAN ANADOLU ZAMAN PENCERELERİ." with an embedded 3-field search capsule (Bölge, Deneyim Türü, Tarih).
- Time-Locked Scarcity Bar: Horizontal pill bar showing live ephemeral badges (e.g. "🔴 EKİM: 72 Saatlik Anagama Fırını Nöbeti (Kalan: 3 Gün)").
- Experience Detail & Checkout Modal: Detail page showing host bio, included items, and checkout drawer with:
  * TÜRSAB A Grubu Lisans No: 2387 Güvence Rozeti
  * 6493 S.K. Uyumlu T+1 Güvenli Havuz (Escrow) Bilgisi
  * Zorunlu Paket Tur Sigortası poliçe kutusu (Geceleme/ulaşım varsa aktif)
- Host Onboarding Wizard (3 Steps):
  * Adım 1: Deneyim Bilgisi & Fotoğraf
  * Adım 2: 4 Lojistik Sorusu (Mekan, Geceleme, Ulaşım, İkram)
  * Adım 3: Fiyat & Net Hak Ediş Kutusu:
    - Bilet Fiyatı: 2.000 TL
    - LORAKS Hizmet Payı (%15): -300 TL
    - 7524 Stopaj (%1): -16,67 TL
    - Net Host Kazancı: 1.683,33 TL
    - SMMM Kuluçka Kartı: "Mali müşaviriniz veya e-faturanız yok mu? Anlaşmalı SMMM ağımız ve Paraşüt entegrasyonuyla 24 saatte yasal başlayın."

3. AI STUDIO ENTEGRASYONU:
Connect to Google Gemini 1.5 Pro API using the VITE_GEMINI_API_KEY environment variable. Whenever a host submits a new listing in the wizard, send the listing payload to Gemini with the system instruction to evaluate pathway compliance (P0-P4) and display the compliance badge in real-time.
```

---

### 2.2 Supabase SQL Şeması (Lovable SQL Editor'e Yapıştırın)

```sql
-- 1. KULLANICI PROFİLLERİ
CREATE TABLE IF NOT EXISTS profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT CHECK (role IN ('traveler', 'host', 'admin')) DEFAULT 'traveler',
    tax_status TEXT CHECK (tax_status IN ('esnaf_muafiyeti_gvk9', 'sahis_sirketi', 'limited_anonim', 'none')) DEFAULT 'none',
    phone TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now())
);

-- 2. DENEYİM İLANLARI VE REGTECH ALANLARI
CREATE TABLE IF NOT EXISTS listings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    host_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    category TEXT CHECK (category IN ('zanaat', 'sofra', 'doga', 'inziva', 'hasat')),
    location_city TEXT NOT NULL,
    price_try NUMERIC(10, 2) NOT NULL,
    duration_hours NUMERIC(4, 1) NOT NULL,
    has_transport BOOLEAN DEFAULT false,
    has_overnight BOOLEAN DEFAULT false,
    pathway_code TEXT CHECK (pathway_code IN ('P0_DIRECT', 'P1_VERIFIED', 'P2_LICENSED', 'P3_RESTRICTED', 'P4_PROHIBITED')) DEFAULT 'P0_DIRECT',
    compliance_approved BOOLEAN DEFAULT false,
    tursab_insurance_required BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now())
);

-- 3. REZERVASYONLAR VE FİNTECH SPLIT TABLOSU
CREATE TABLE IF NOT EXISTS bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    listing_id UUID REFERENCES listings(id),
    traveler_id UUID REFERENCES profiles(id),
    booking_date DATE NOT NULL,
    guest_count INT NOT NULL DEFAULT 1,
    ticket_gross_try NUMERIC(10, 2) NOT NULL,
    loraks_fee_try NUMERIC(10, 2) NOT NULL,      -- %15
    tax_withholding_try NUMERIC(10, 2) NOT NULL, -- %1 (7524 S.K.)
    host_net_payout_try NUMERIC(10, 2) NOT NULL, -- ~%84
    escrow_status TEXT CHECK (escrow_status IN ('HELD_IN_ESCROW', 'RELEASED_T_PLUS_1', 'REFUNDED')) DEFAULT 'HELD_IN_ESCROW',
    qr_checkin_code TEXT UNIQUE NOT NULL,
    checked_in_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now())
);
```

---

## 🎯 SONUÇ VE ÇALIŞMA PLANI

1. **Önce Google AI Studio:**
   Yukarıdaki **System Instructions** ve **Structured Schema**'yı yapıştırarak motorun doğruluğunu görün. 2.000 TL'lik bilet için `1.683,33 TL` net hak ediş çıktısını ve `P0`/`P2` kararlarını test edin.
2. **Sonra Lovable (Ücretli Hesap):**
   Yukarıdaki master promptu ve Supabase SQL şemasını yapıştırarak editoryal seyahat vitrininizi oluşturun.
3. Böylece hem Google AI Studio'da test edilmiş kaya gibi sağlam bir **hukuki/finansal çekirdeğe**, hem de Lovable üzerinde çalışan **dünya standartlarında bir web arayüzüne** sahip olursunuz!
