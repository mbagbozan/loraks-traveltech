# 🚀 LORAKS TRAVELTECH: PROJE BAŞLATMA VE WEB ARAYÜZÜ KURULUM PLANI (v5.3 NİHAİ SÜRÜM)

**Hedef:** Eski "sofra/yemek kulübü" kalıntılarını tamamen çöpe atarak; **Zamana Kilitli Nadir Anlar (Time-Locked Scarcity)** ve **v5.3 Yasal/Mali Kalkanı** ile sıfırdan modern bir TravelTech web platformu inşa etmek.

---

## 🛠️ ADIM 1: TASARIM SİSTEMİ & RENK PALETİ (60-30-10 KURALI)

### Prompt 1 (Projeyi Başlatma ve Tasarım Dili):
> *"Create a clean, highly editorial TravelTech & Experience Marketplace called 'LORAKS'. 
> Use an editorial, tactile Anatolian craftsmanship palette:
> - Background (60%): Raw Unbleached Linen `#FDFCF8` / `stone-50`.
> - Primary Elements & Buttons (30%): Deep Pine Green `#1A432E`.
> - Scarcity & Accent Highlights (10%): Baked Terracotta `#C86D51` for badges like 'Son 2 Kontenjan' and live countdowns.
> - Typography: Elegant Serif (Newsreader, Playfair Display) for headings; Plus Jakarta Sans or Inter for UI/data.
> - Navigation: Top sticky nav with logo 'LORAKS', links ('Zaman Pencereleri', 'Bağımsız Hostlar', 'Nasıl Çalışır?', 'Kurumsal B2B') and CTA button 'Host Ol (Zanaatını Aç)'."*

---

## 🗄️ ADIM 2: VERİTABANI ŞEMASI (v5.3 UYUMLU POSTGRESQL / SUPABASE)

### Prompt 2 (Veritabanı Tabloları):
> *"Setup database tables for LORAKS with the following clean architecture:
> 1. `profiles`: id (uuid, auth), full_name, email, role ('traveler' or 'host'), phone, created_at.
> 2. `listings`: id (uuid), host_id (references profiles), title, description, category ('atölye_zanaat', 'sakli_rotalar', 'yasayan_kultur', 'ozel_bulusmalar'), location, city, price_per_person (numeric), duration_hours, venue_type ('studio', 'outdoor', 'heritage_route', 'home'), has_transport (boolean), has_accommodation (boolean), has_guided_tour (boolean), pathway_code ('P0', 'P1', 'P2', 'P3', 'P4'), time_window_start (date), time_window_end (date), max_capacity (integer, max 8), current_booked (integer), is_annual_only (boolean, default true), next_year_date (text), status ('active', 'draft', 'pending'), created_at.
> 3. `bookings`: id (uuid), listing_id (references listings), traveler_id (references profiles), booking_date, guest_count, total_amount, platform_fee_gross, withholding_tax_360, host_net_payout, payment_status ('held_in_escrow', 'settled', 'refunded'), qr_checkin_token, created_at.
> 4. `waitlist`: id (uuid), listing_id (references listings), user_id, email, requested_cohort_year (e.g. '2027'), created_at."*

---

## 🌿 ADIM 3: ANA SAYFA & ZAMAN PENCERELERİ (DISCOVERY & SCARCITY UI)

### Prompt 3 (Ana Sayfa, Hero ve Kıtlık Çizelgesi):
> *"Build the Homepage for LORAKS around the core concept: 'It is too good to wait another year':
> 1. Hero Section: Clean Natural Linen (#FDFCF8) background with headline: 'YILDA SADECE BİR KEZ AÇILAN ANADOLU ZAMAN PENCERELERİ.' and subheadline: 'Turist olma. Bağımsız üreticilerin atölyelerinde, bilinmeyen patikalarda ve saklı hafızalarda; hayat boyu hatırlanacak alternatif anılar.'
> 2. Search Capsule: Inputs for 'Destinasyon' (Urla, Kapadokya, Kazdağları), 'Deneyim Türü' (Zanaat & Ateş, Saklı Flora, Kültürel Bellek), and 'Zaman Penceresi' (Bu Ay Açık Pencereler), plus a Deep Pine Green (#1A432E) 'Keşfet →' button.
> 3. Live Ephemeral Timeline Bar (Horizontal scrollable pills):
>    - '🔴 EKİM: 72 Saatlik Anagama Odun Fırını Nöbeti (Kalan: 3 Gün)'
>    - '🟠 EKİM: Safranbolu Şafak Hasadı (Son 2 Kontenjan)'
>    - '⚪ KASIM: Ayvalık İlk Soğuk Sıkım & Zeytinlik'
>    - '⚪ MAYIS: Gökova Gece Biyolüminesans Kanosu'
> 4. Experience Cards Grid: Show 3 cards with time-locked badges:
>    - Card 1: '72 Saatlik Anagama Odun Fırını Nöbeti & Seramik Pişirimi' (Avanos | Kerem Usta | ⏳ YILDA SADECE 1 KEZ | 🔴 Son 2 Kontenjan / Maks. 4 Kişi | 6.800 ₺ | ⚠️ Kaçırırsanız: Ekim 2027 | 🛡️ TÜRSAB Lisans No: 2387 Güvencesi).
>    - Card 2: 'Kazdağları Yabani Göknar & Şifalı Flora Keşfi' (Edremit | Melis K. | 🌱 İlkbaharın İlk 10 Günü | Maks. 6 Kişi | 3.400 ₺).
>    - Card 3: 'Balat ve Fener Kültür Rotası: Saklı Avlular' (Balat | TUREB Kokartlı Rehber Eşliğinde | Maks. 8 Kişi | 1.850 ₺)."*

---

## 🛡️ ADIM 4: DENEYİM DETAYI & ASİMETRİK REZERVASYON MODÜLÜ

### Prompt 4 (Detay Sayfası ve Güvenlik Zırhı):
> *"Build the Experience Detail Page with a 65/35 asymmetric two-column layout:
> 1. Left Column (Storytelling):
>    - 'Neden Yılda Sadece Bir Kez?': Explanation of the harvest or firing cycle.
>    - 'Host Hikayesi': Portrait of the maker working with raw materials.
>    - 'Deneyim Akışı': Hour-by-hour authentic schedule.
> 2. Right Column (Sticky Booking Widget):
>    - Price per person.
>    - Limited date selector (only open time-window days enabled).
>    - Guest counter (strictly capped at 4-8).
>    - Primary Button: 'Pencereyi Yakala (Rezervasyon Yap)'.
>    - Waitlist Feature: If full, button changes to '2027 Sezonu İçin Sıraya Gir (Waitlist)'.
>    - Trust Matrix:
>      * 🛡️ T.C. Kültür ve Turizm Bakanlığı A Grubu Seyahat Acentası (Belge No: 2387) Güvencesi.
>      * 🔒 TCMB Lisanslı Güvenli Havuz (Escrow): Para QR bilet okutulana kadar korunur.
>      * 📜 48 Saate Kadar Sıfır Vergi İadesi."*

---

## 🏡 ADIM 5: HOST ONBOARDING (PATHWAY P0-P4 & CANLI HAKEDİŞ SİMÜLATÖRÜ)

### Prompt 5 (Host Kayıt Sihirbazı):
> *"Build a friendly 4-step 'Host Ol' (Creator Onboarding) Wizard based on the 13_Organizator_Ol specification:
> - Step 1: Deneyim Adı, Kategori (Atölye/Zanaat, Saklı Rotalar, Kültür/Bellek), Açıklama ve Doğal Işıklı Fotoğraf yükleme.
> - Step 2 (4 Lojistik Sorusu):
>    1. Mekan Durumu: Sabit stüdyo/atölye mi, Açık alan mı?
>    2. Konaklama var mı (Otel/Kamp)? -> Evet ise sistem otomatik 'P2 Lisanslı Acente Kalkanı'na geçirir.
>    3. Toplu ulaşım/transfer var mı? -> Evet ise sistem 'D2 Lisanslı Taşıyıcı'ya bağlar.
>    4. Tarihi anlatım / Rehberlik var mı? -> Evet ise 'TUREB Kokartlı Rehber' şartı arar.
> - Step 3 (Fiyatlandırma & Şeffaf Hakediş Simülatörü):
>    - Fiyat Girdisi (Örn: 2.000 TL).
>    - Canlı Matematik Kutusu:
>      * Misafirin Ödediği: 2.000,00 TL
>      * LORAKS Platform Payı (%15): -300,00 TL
>      * 7524 Sayılı Kanun %1 E-Ticaret Stopajı: -16,67 TL
>      * Hesabınıza Yatacak Net Hak Ediş: 1.683,33 TL (Kuruşu kuruşuna tam mutabakat)
>    - '📢 Şirketiniz veya Muhasebeciniz Yok mu? Esnaf Muafiyeti ve Genç Girişimci istisnası rehberliğiyle yanınızdayız.'
> - Step 4: Submit creates listing in draft mode awaiting verification."*
