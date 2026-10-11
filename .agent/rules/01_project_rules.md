# LORAKS TRAVELTECH — PROJE YÖNETİŞİM, KURALLAR VE ANLAŞMA PROTOKOLÜ (PROJECT CONSTITUTION)
> **Bu dosya, Antigravity ve tüm AI asistanları için HER YENİ SOHBET PENCERESİNDE zorunlu olarak yüklenen ANA ANAYASADIR.**  
> Projede çalışan hiçbir model bu kuralların dışına çıkamaz, eski sürümleri referans alamaz ve kafasına göre değişiklik yapamaz.

---

## 🏛️ 1. TEK GERÇEK KAYNAK İLKESİ (SINGLE SOURCE OF TRUTH)
* **Aktif ve Bağlayıcı Master Blueprint:**  
  👉 [`docs/17_loraks_traveltech_nihai_birlesik_master_blueprint_v5_4.md`](file:///Users/mehmetbagbozan/Documents/antigravity/cool-noether/docs/17_loraks_traveltech_nihai_birlesik_master_blueprint_v5_4.md) (`v5.4 Unified Definitive Edition`)
* **Aktif ve Bağlayıcı Sunum Destesi:**  
  👉 [`docs/18_loraks_kurumsal_tanitim_ve_sunum_destesi_revize.md`](file:///Users/mehmetbagbozan/Documents/antigravity/cool-noether/docs/18_loraks_kurumsal_tanitim_ve_sunum_destesi_revize.md) (20 Slaytlık Güncel Deste)
* **Geçersiz / Arşivlenmiş Sürümler:**  
  `v2.0`, `v5.0`, `v5.1`, `v5.2` ve `v5.3` gibi önceki sürümler yalnızca tarihsel referanstır. Herhangi bir planlama, kodlama veya strateji çalışmasında **ASLA** bu eski sürümler ana metin olarak baz alınamaz.

---

## 👥 2. RESMİ YÖNETİM KURULU VE UNVANLAR (DEĞİŞTİRİLEMEZ)
Resmi sunum, Ticaret Sicil ve kurumsal yapı gereği liderlik matrisi kesindir. Başka isimler veya hayali unvanlar türetilemez:

1. **AYŞEGÜL DENİZLİ:** Yönetim Kurulu Başkanı  
   *(Şirket vizyonu, deneyim standartları, topluluk mimarisi, kürasyon kalitesi)*
2. **GÖKHAN EKRE:** Genel Müdür  
   *(Şirket icraatı, operasyonel mükemmellik, saha lojistiği, tedarikçi ve acente ağı)*
3. **ERAY ERDEMİR:** Finans Direktörü (CFO)  
   *(Finansal yönetim, bütçe ve sermaye planlaması, B2B gelir modelleri, kârlılık) — NOT: "Ray" ve "Eray" ayrı kişiler DEĞİLDİR, tek ve resmi kişi Eray Erdemir'dir.*
4. **MEHMET BAĞBOZAN:** Kurucu Ortak & Strateji, Teknoloji ve TravelTech Lideri  
   *(T.C. Kültür ve Turizm Bakanlığı Seyahat Acentaları Enformasyon Memurluğu Belge No: #2387 — A Grubu acente yasal sorumlu müdürlük şartını sağlar; yapay zeka, RegTech/FinTech mimarisi ve platform teknolojilerini yönetir).*

---

## 🧭 3. MARKA RUHU, TON VE KAZAN - KAZAN FELSEFESİ
* **Slogan & Mottolar:**  
  * *"Kendine Zaman Tanı"*  
  * *"Deneyim. Bağlantı. Dönüşüm."*  
  * *"Bir araya gelmenin değerini bilenler için..."*
* **Kazan - Kazan (Win-Win):**  
  Herkes kazanacak. Host/topluluk lideri korkusuzca ve yasal endişe taşımadan daha çok kişiye ulaşacak, daha çok etkinlik düzenleyecek. Loraks tam operasyonel ve hukuki güvence sağlayacak. Misafir kaliteli hizmet alacak, tedarikçi kazanacak.
* **İletişim Tonu:**  
  Metinler ağır ve baskıcı ceza hukuku maddeleriyle boğulmaz! Yasal uyum, korkutucu bir ceza aracı olarak değil; üreticinin sırtındaki bürokrasi ve ceza korkusunu alan bir **"Güven ve Özgürlük Kalkanı"** olarak anlatılır.
* **Yapay Zeka ve Teknoloji:**  
  Loraks teknolojiyi ve yapay zekayı soğuk bir otomasyon olarak değil; insana dokunan, bir araya gelmeyi kolaylaştıran dünya standardında bir kolaylaştırıcı olarak kullanır.

---

## 🛡️ 4. SİSTEMDE DEĞİŞİKLİK YAPMA PROTOKOLÜ (CHANGE PROTOCOL)
Kullanıcı yeni veya farklı bir sohbet penceresinde değişiklik istediğinde asistan şu adımları **istisnasız** takip etmek zorundadır:

1. **Önce Oku ve Karşılaştır (Check Before Writing):**  
   Kafana göre metin üretme. Önce `docs/17_...` ve `docs/18_...` dosyalarını oku. Değişikliğin mevcut sistemle çelişip çelişmediğini denetle.
2. **Bütünlüğü Koru:**  
   Bir bölüm değiştiğinde diğer bölümlerdeki bağıntıları koparma.
3. **Test Doğrulaması:**  
   Kod veya hesaplama içeren herhangi bir değişiklikte `python3 tests/run_all_tests.py` ve `tests/test_integration.py` (30/30 test) çalıştırılarak 100% yeşil olduğu doğrulanmalıdır.
4. **Git ve Depo Senkronizasyonu:**  
   Yapılan her anlamlı değişiklik doğrudan Git'e commit edilmeli ve GitHub reposuna (`origin master`) pushlanmalıdır:
   * Repo: `https://github.com/mbagbozan/loraks-traveltech.git`
5. **Kullanıcıya Şeffaf Rapor:**  
   Hangi dosyanın neden ve nasıl güncellendiği, hangi testlerin koşulduğu kullanıcıya net bir dille bildirilmelidir.
