# LORAKS TRAVELTECH — LOVABLE & AI STUDIO PREVIEW MASTER PROMPT
**"Time-Locked Scarcity & Living Anatolian Hospitality" (Zamana Kilitli Nadir Anlar & Yaşayan Kültür)**

* **Sürüm:** `v5.3 Production Gold Preview Prompt`
* **Hedef Araçlar:** Lovable, Google AI Studio, v0.dev, Cursor veya Bağımsız React/Tailwind Web Prototipi
* **Referans Tasarım Sistemi:** 60-30-10 Kuralı (Doğal Keten, Çam Yeşili, Pişmiş Toprak)
* **Referans Mimari:** LORAKS Nihai Mimari Anayasa (v5.3) & Dual-Entity Trust Shield

---

## 📋 DOĞRUDAN KOPYALANACAK MASTER PROMPT METNİ

```markdown
Build a production-grade, highly editorial, and modern web application for "LORAKS TravelTech" — Turkey's first RegTech & Universal Experience Marketplace for independent creators, alternative journeys, and time-locked ephemeral experiences.

### 1. CORE BRAND PHILOSOPHY & CONCEPT: "TIME-LOCKED SCARCITY"
- The core value proposition is NOT generic tours or home dinners. It is: "It is too good to wait another year."
- Experiences are strictly ephemeral and tied to nature, harvest, or master craftsmanship schedules (open only 3 to 14 days a year). If missed, guests must wait 365 days.
- Cohorts are ultra-micro (strictly 4 to 8 guests per cohort).
- Hosts are independent creators: sculptors, botanists, traditional anagama potters, wild foragers, and architects.
- Slogan: "Turist Olma. Bir Parçası Ol." (Don't be a tourist. Be part of the living culture.)

### 2. DESIGN SYSTEM & VISUAL IDENTITY (THE 60-30-10 RULE)
- Background (60%): Raw Unbleached Linen / Warm Editorial Paper `#FDFCF8` (and subtle `stone-50`). Warm, breathing, tactile negative space.
- Primary Elements & Structure (30%): Deep Pine Green `#1A432E` (Headings, primary CTA buttons, footer, trust badges, active state indicators).
- Accent Highlights (10%): Baked Terracotta `#C86D51` (Scarcity badges like "Son 2 Kontenjan", live countdown timers, active category tags, subtle hovers).
- Typography Hierarchy:
  - Headings (H1, H2, H3): Elegant Editorial Serif (`font-serif`, e.g., Newsreader, Cormorant Garamond, or Playfair Display).
  - Body, Badges & Interactive Data: Clean, modern Sans-serif (`Plus Jakarta Sans` or `Inter`).
- Micro-details: Subtle borders (`border-stone-200/60`), glassmorphic overlays with linen tint, smooth transitions, zero generic corporate travel elements.

### 3. ESSENTIAL SECTIONS TO BUILD IN THE PREVIEW:

#### A. Header / Navbar
- Logo: "LORAKS" (Editorial serif font, elegant, deep pine green).
- Navigation Links: "Zaman Pencereleri (Timeline)", "Bağımsız Hostlar", "Nasıl Çalışır?", "Kurumsal (B2B)".
- Actions: "Host Ol (Zanaatını Aç)" text button + "Giriş Yap" button.

#### B. Hero Section & Ephemeral Timeline Bar
- Headline: "YILDA SADECE BİR KEZ AÇILAN ANADOLU ZAMAN PENCERELERİ."
- Subtitle: "Her gün yaşayamayacağınız, kaçırırsanız 365 gün bekleyeceğiniz nadir ve bağımsız deneyimler."
- Interactive Search Capsule:
  - Fields: Destinasyon (Urla, Kapadokya, Kazdağları), Deneyim Tipi (Zanaat & Ateş, Saklı Flora, Gece Rotaları), Zaman Penceresi (Bu Ay Açık).
  - Action Button: Deep Pine Green "Keşfet →"
- Live Ephemeral Timeline Bar (Horizontal scrollable pills):
  - "🔴 EKİM: 72 Saatlik Anagama Fırını Nöbeti (Kalan: 3 Gün)"
  - "🟠 EKİM: Safranbolu Şafak Hasadı (Son 2 Kontenjan)"
  - "⚪ KASIM: Ayvalık İlk Soğuk Sıkım & Zeytinlik"
  - "⚪ MAYIS: Gökova Gece Biyolüminesans Kanosu"

#### C. Experience Grid ("Zamana Kilitli Deneyimler" - Ephemeral Cards)
Build interactive cards featuring:
1. Card 1: "72 Saatlik Anagama Odun Fırını Nöbeti & Seramik Pişirimi"
   - Location: Avanos, Nevşehir | Host: Kerem Usta (30 Yıllık Geleneksel Çömlekçi)
   - Badge (Terracotta): "⏳ YILDA SADECE 1 KEZ · AÇIK: 14-17 EKİM"
   - Scarcity Tag: "Son 2 Kontenjan (Maksimum 4 Misafir)"
   - Price: 6.800 ₺ / misafir
   - Trust Badge: "🛡️ TÜRSAB Lisanslı Acente Güvencesi"
   - Next Opportunity Warning: "⚠️ Kaçırırsanız sonraki pencere: Ekim 2027"
2. Card 2: "Kazdağları Yabani Göknar & Şifalı Flora Keşfi"
   - Location: Edremit, Balıkesir | Host: Melis K. (Etnobotanikçi)
   - Badge: "🌱 İLKBAHARIN İLK 10 GÜNÜ"
   - Capacity: "Maks. 6 Kişi" | Price: 3.400 ₺ / misafir
3. Card 3: "Urla Taş Değirmende İlk Hasat ve Zeytin Şef Masası"
   - Location: Urla, İzmir | Host: Ahmet & Zeynep Usta
   - Badge: "🫒 HASAT DÖNEMİ ÖZEL"
   - Capacity: "Maks. 8 Kişi" | Price: 4.200 ₺ / misafir

#### D. Interactive Experience Detail Drawer / Modal (Sticky Booking & Trust Shield)
When a card is clicked, show a rich detail modal with:
- Left Column (Storytelling):
  - "Neden Yılda Sadece Bir Kez?" section explaining the natural cycle.
  - "Hostun Hikayesi & Atölye": High-resolution imagery of hands working with clay/leaves.
  - "Deneyim Akışı": Hour-by-hour breakdown.
- Right Column (Sticky Booking Widget):
  - Price per guest, date selection (only available days highlighted).
  - Guests counter (strict limit up to 4-6 guests).
  - Primary CTA: "Pencereyi Yakala (Rezervasyon Yap)".
  - Waitlist Feature: When sold out, button changes to "2027 Sezonu İçin Sıraya Gir (Waitlist)".
  - Trust Matrix Icons:
    - 🛡️ TÜRSAB A Grubu Seyahat Acentası Koruma Kalkanı (Belge No: 2387).
    - 🔒 %100 TCMB Lisanslı Escrow (Para QR bilet okutulana kadar güvende).
    - 📜 48 Saate Kadar Sıfır Vergi İadesi.

#### E. Host Onboarding & Payout Simulator (Host Preview Mode)
Provide a toggle or a section to preview the Host Onboarding Experience:
- 4-Question Logistics Classifier (Pathway P0/P1/P2/P3 Engine):
  1. Mekan (Sabit stüdyo vs Açık alan)?
  2. Konaklama var mı? (Otel/Çadır)? -> Triggers P2 Travel Agency Shield.
  3. Toplu ulaşım/transfer var mı? -> Triggers D2 Licensed Carrier.
  4. TUREB rehber veya gıda sertifikası var mı?
- Live Net Payout Calculator:
  - Input: Bilet Fiyatı (e.g., 2.000 ₺)
  - Calculations:
    - Platform Hizmet Bedeli (%15): -300 ₺
    - 7524 Sayılı Kanun %1 E-Ticaret Stopajı: -16,67 ₺
    - Net Host Hak Edişi: 1.683,33 ₺ (Kuruşu kuruşuna tam mutabakat)
  - Message: "Siz sadece zanaatınıza odaklanın; faturalandırma, TÜRSAB uyumu ve vergi stopajını LORAKS yönetir."

#### F. Trust & Regulatory Shield Footer
- Dual-Entity Transparency statement:
  - "Platform yazılım ve pazaryeri hizmetleri LORAKS Teknoloji A.Ş. tarafından sağlanmaktadır."
  - "Paket tur, seyahat ve transfer operasyonları T.C. Kültür ve Turizm Bakanlığı A Grubu Seyahat Acentası (Belge No: 2387) güvencesi altındadır."
- Full legal links, KVKK compliance, and contact info.

Make the UI responsive, polished, culturally authentic, and deeply evocative of tactile craftsmanship.
```

---

## 🎯 BU PROMPTUN SAĞLADIĞI TEKNİK VE STRATEJİK AVANTAJLAR

1. **Lovable & Cursor Uyumlu Tek Blok:**  
   Tek bir prompt ile modern bir frontend oluşturucu; hem kahraman alanını (Hero), hem mikro kontenjanlı "Zamana Kilitli" kartları, hem sepet/checkout modalını hem de host simülatörünü aynı anda ayağa kaldırabilir.
2. **60-30-10 Tasarım Sistemi Bütünlüğü:**  
   Doğal Keten (`#FDFCF8`), Çam Yeşili (`#1A432E`) ve Pişmiş Toprak (`#C86D51`) renkleriyle sıradan turizm portallarından anında ayrışan yüksek estetikli bir editoryal hava sunar.
3. **Mevzuat & Finansal Zırh Entegre:**  
   Bakanlık Enformasyon Belgesi No: 2387, %100 TCMB lisanslı emanet (escrow), 2.000 TL / 1.683,33 TL kuruş mutabakatı ve P0–P4 kural sınıflandırması arayüzün içine doğal olarak gömülmüştür.
