# LORAKS TRAVELTECH — STRATEJİK REFERANS VE MİMARİ UYGULAMA PLANI
**"Türkiye Deneyim Ekonomisi İçin Evrensel Pazaryeri ve Güven Altyapısı"**

* **Sürüm:** `v5.3 (Unified Architecture & Production Gold Edition)`
* **Tarih:** 08 Ekim 2026
* **Hukuki Niteliği:** Stratejik Referans ve Mimari Tasarım Belgesi *(Aksi yetkili mercilerce doğrulanana kadar varsayım, hipotez ve operasyonel tasarımları içerir; nihai hukuki/mali kesin hüküm teşkil etmez).*
* **Şirket:** LORAKS ORGANİZASYON DANIŞMANLIK HİZMETLERİ A.Ş.  
  *(İTO Sicil: 1144533 · MERSİS: 0609146560400001 · VKN: 6091465604 · Ticaret Sicili Gazetesi: Sayı 11599)*

---

> ### 🏛️ STRATEJİK İLKE (CORE AXIOM)
> **"Tasarımda Kapsamlılık. Kategoride Kontrollü İcraat. Temel Fikri Mülkiyet Olarak Mevzuat ve Güven Altyapısı."**  
> *(Breadth by design. Controlled execution by category. Compliance as core intellectual property.)*

---

## 1. EVRENSEL DENEYİM PAZARYERİ HARİTASI (MASTER PICTURE)

LORAKS, yalnızca kayıt dışı turizmi dönüştüren bir regülasyon projesi veya münferit bir atölye sitesi değildir. **LORAKS, Türkiye’nin tüm deneyim ekonomisini kapsayan uçtan uca evrensel bir altyapı platformudur.** Kayıt dışı arzın kayıt altına alınması, platformun çözdüğü kritik bir problemdir; ancak platformun tanımı değildir.

```text
                                     LORAKS
                                       │
                      EVRENSEL DENEYİM PAZARYERİ
                   (Universal Experience Marketplace)
                                       │
       ┌───────────────────────────────┼───────────────────────────────┐
       │                               │                               │
   GEZGİNLER / TÜKETİCİLER     EV SAHİPLERİ / ÜRETİCİLER    KURUMSAL ŞİRKETLER (B2B)
   (Keşif, Güven, Sosyallik)   (Zanaat, Mutfak, Doğa, İnziva)  (İK Bütçeleri, Wellbeing)
       │                               │                               │
       └───────────────────────────────┼───────────────────────────────┘
                                       │
                              KEŞİF VE REZERVASYON
                              (Discovery & Booking)
                                       │
                             UYUM VE GÜVEN MOTORU
                           (Compliance & Trust Engine)
              Detect ➔ Classify ➔ Assess ➔ Route ➔ Verify ➔ Escalate ➔ Monitor
                                       │
       ┌───────────────────────┬───────┴───────────────┬───────────────────────┐
       │                       │                       │                       │
      P0                      P1                      P2                      P3/P4
   BAĞIMSIZ ATÖLYE     SERTİFİKALI ÜRETİCİ     LİSANSLI ACENTE          GELİŞİM DESTEĞİ
 (Görünürde Doğrudan   (Doğrulanmış Nitelik)  (Seyahat & Paket Tur   (Eksik Belge Rehberliği
       Uygun)                                  Partner İncelemesi)     & Lisanslı Taşıma)
       │                       │                       │                       │
       └───────────────────────┴───────┬───────────────┴───────────────────────┘
                                       │
                           İŞLEM / SÖZLEŞME / VERGİ
                       (PSP Settlement / 7524 Stopajı)
                                       │
                           GÜVENLİ İFA VE TESLİMAT
                       (QR Check-in / Sigorta Kalkanı)
                                       │
                           VERİ / RETENTION / BÜYÜME
                      (LORAKS Circle / Host OS / B2B ARR)
```

---

## 2. UYUM VE GÜVEN MOTORU: SINIFLANDIRMA VE YÖNLENDİRME DİSİPLİNİ

### 2.1 Hukuki Yetki Değil, Operasyonel Teşhis ve Filtreleme
Uyum Motoru (`src/pathway_engine.py`), bir mahkeme veya kamu otoritesi gibi bağlayıcı "hukuki hüküm" vermez. Platform kuralları doğrultusunda ilanı analiz eder, risk derecesine göre teşhis koyar ve ilgili yasal patikaya yönlendirir:

$$\text{Süreç Akışı: } \mathbf{Tespit (Detect)} \rightarrow \mathbf{Sınıflandır (Classify)} \rightarrow \mathbf{Değerlendir (Assess)} \rightarrow \mathbf{Yönlendir (Route)} \rightarrow \mathbf{Doğrula (Verify)} \rightarrow \mathbf{Üst Seviyeye Aktar (Escalate)} \rightarrow \mathbf{İzle (Monitor)}$$

### 2.2 Pathway Teşhis ve Yönlendirme Matrisi

| Kod | Tetikleyici | Sistemdeki Operasyonel Statüsü | Kullanıcıya Gösterilen Creator Enablement Dili |
|---|---|---|---|
| **P0** | Sabit mekanlı, ulaşım/geceleme içermeyen tekil atölye veya etkinlik | **Görünürde Doğrudan Uygun** *(Apparently eligible under defined rules)* | **Bağımsız Atölye ve Etkinlik:** *"Atölyeniz mevcut platform kriterlerine göre doğrudan rezervasyona ve katılımcılara açılmaya uygundur."* |
| **P1** | Gıda hijyen, uzmanlık veya ilk yardım belgesinin sisteme yüklenmesi | **Doğrulanmış Nitelik** *(Verified Credentials)* | **Sertifikalı / Güvenilir Üretici:** *"Uzmanlık veya hijyen belgeniz operasyon ekibimizce doğrulandı. Nitelikli profilinizle yayındasınız."* |
| **P2** | Ulaşım, geceleme/konaklama veya çok günlük paket tur bileşeni | **Lisanslı Acente İncelemesi Gerektirir** *(Requires Licensed Travel Operation)* | **Seyahat Acentesi Güvencesi Kapsamında İlerleme:** *"Ulaşım veya konaklama içeren deneyiminiz, lisanslı seyahat acentesi incelemesine ve Zorunlu Tur Sigortası sürecine yönlendirilmiştir."* |
| **P3** | Alan uzmanlığı, hijyen veya mesleki belgenin eksik olması | **Gelişim ve Belge Desteği Bekleyen** *(Pending Documentation)* | **Lisans ve Gelişim Desteği:** *"Eksik belgelerinizi tamamlamanız için rehber adımlar hazırlandı. Belgeler tamamlanana kadar ilanınız taslak olarak korunur."* |
| **P4** | Şahsi araçla transfer veya belgesiz yolcu taşıma girişimi | **Lisanslı Operasyona Sevk** *(Rerouted to Licensed Carrier)* | **Doğru Yasal Patika:** *"Yolcu transferi gerektiren kısımlar, platform standartları gereğince D2 lisanslı yetkili taşıyıcılara devredilmek üzere yönlendirilir."* |

### 2.3 RegTech Safe Harbor Kuralları ve Gri Alan Güvenlik Kalkanı (v3.2 Altın Kurallar)
Sektördeki 5 kritik yasal sorumluluk tuzağını yazılımsal sert kısıtlar (*Invariants*) ile önleyen güvenlik kalkanı:

1. **Senaryo A (Balat / TUREB 6326 S.K. Rehberlik Koruması):**
   * *Sorun:* Şehir içinde çok duraklı (multi-stop) sokak atölyeleri düzenleyen fotoğrafçı veya tarih meraklısı hostlar, TUREB denetimlerinde "kaçak rehberlik" cezasına çarptırılabilir.
   * *Yazılımsal Çözüm:* Bakanlık kokartı olmayan hostların ilan açabilmesi için; *"Bu etkinlik süresince tarihi ve kültürel rehberlik yapılmayacağı, sadece teknik fotoğraf/sanat atölyesi eğitimi verileceği"* dijital taahhüdünü onaylaması zorunludur. İlan sayfasına ve bilet onayına yasal feragat metni (*Legal Disclaimer*) otomatik eklenir (`src/safe_harbor_filters.py`).

2. **Senaryo B (Konvoy Kampı / 1618 S.K. Geceleme Kilidi):**
   * *Sorun:* Katılımcıların kendi araçlarıyla geldiği "konvoy doğa kampları"nda ulaşım verilmediği gerekçesiyle P0 zannedilmesi.
   * *Yazılımsal Çözüm:* 1618 Sayılı Kanun uyarınca, ulaşım olmasa dahi **geceleme veya çadır konaklaması içeren her deneyim İSTİSNASIZ P2'dir.** Otomatik olarak LORAKS Seyahat Acentesi A.Ş. yasal kalkanına bağlanır, Zorunlu Paket Tur Sigortası düzenlenir ve komisyon oranı %12'ye optimize edilir.

3. **Senaryo C (Platform Dışı Ödeme / VUK & 6563 S.K. ve Sohbet Maskeleme):**
   * *Sorun:* İlan metninde "kalanı elden şoföre verilecektir" denmesi veya mesajlaşmada IBAN/telefon paylaşılarak komisyon ve vergi kaçırılması.
   * *Yazılımsal Çözüm:* İlan metinleri NLP ajanıyla taranır (`scan_offplatform_payment`); elden/nakit ifadeleri yakalanırsa ilan otomatik karantinaya alınır (`QUARANTINE_LISTING`). Misafir-Host içi sohbet mesajlarındaki TR IBAN'lar, telefon numaraları ve kayıt dışı ödeme çağrıları anında `[GÜVENLİK NEDENİYLE GİZLENMİŞ IBAN]` olarak maskelenir (`src/ai_audit_agent.py`, `src/safe_harbor_filters.py`).

4. **Senaryo D (GVK m.9 Esnaf Muafiyeti Hasılat Tavanı Takibi):**
   * *Sorun:* Bireysel zanaatkâr ve şeflerin yıllık esnaf muafiyeti sınırını aşarak geriye dönük vergi incelemesine ve cezaya uğraması.
   * *Yazılımsal Çözüm:* Sistem, 2026 yılı tavanı olan **1.100.000,00 TL** kümülatif GMV hacmini anlık takip eder. %80 bareminde (880.000 TL) host paneline *"Limitinize yaklaştınız, şirketleşme başlatabilirsiniz"* uyarısı düşer. Tavan %100 aşıldığında yeni rezervasyon alımı kilitlenir ve host Vitrin SMMM ağına sevk edilir.

5. **Senaryo F (Supper Club / Evde Yemek & TAPDK 4733 S.K. Kuralı):**
   * *Sorun:* Ev ve konut ortamlarında para karşılığı şarap/rakı tadımı veya alkollü akşam yemeği düzenlenmesi (mühürleme ve kaçak içki yaptırımı).
   * *Yazılımsal Çözüm:* Mekan türü "ev/konut" (`home`) seçildiğinde alkol seçeneği yazılımsal olarak kesinlikle KİLİTLENİR; TAPDK ruhsatı olmayan konutlarda ücretli alkol servisi engellenir. Yemek etkinliklerinde ayrıca katılımcı Alerjen ve Sağlık Beyan Formu zorunlu tutulur.

---

## 3. CREATOR ENABLEMENT VE VİTRİN SMMM KULUÇKASI

### 3.1 Dildeki Paradigma Kayması
Platform, üreticiye "yasadışı iş yapıyorsun" diyen bir kolluk kuvveti gibi yaklaşmaz. Üreticiyi ticari ve operasyonel olarak yetkinleştiren bir **yol arkadaşı** olarak konumlanır.

### 3.2 Kayıt Sepeti (Onboarding Basket) 4 Teşhis Boyutu
1. **Kimlik ve Vergi Profili:** Şahıs/tüzel kişilik, Esnaf Muafiyeti Belgesi, GVK Mük. m.20 durumu.
2. **Mesleki Yetkinlik:** Ustalık, zanaat belgeleri, ilk yardım sertifikası, kokart durumu.
3. **Mekan ve Lojistik:** Atölye, stüdyo, ev, açık alan; katılımcı ulaşım modeli.
4. **Güvenlik ve Risk:** Fiziksel risk seviyesi, gıda/içecek ikramı, çadır/konaklama durumu.

### 3.3 Vitrin SMMM Kuluçkası ve Katma Değerli Hizmetler (Ancillary Model)
SMMM desteği gizli bir detay değil, host karşılama vitrininin temel güven unsurudur:
* **GVK m.9 Esnaf Muafiyeti:** Evinde veya atölyesinde mikro üretim yapanlar için vergisiz yasal başlangıç rehberliği.
* **Genç Girişimci İstisnası (GVK Mük. m.20):** 29 yaş altı üreticiler için kazanç istisnası ve 1 yıllık Bağ-Kur prim teşvik desteği *(Güncel yıllık tutarlar SMMM koordinasyonuyla teyit edilir)*.
* **Tevkifat Mahsubu:** 7524 kapsamında kesilen %1 stopajın yıl sonu beyannamelerinden mahsuplaştırılması otomasyonu.
* **İş Modeli Açılımı:** Tek seferlik yönlendirme primleri (lead fee) ve ön muhasebe SaaS entegrasyonları *(Yasal dayanak: Şirket Esas Sözleşmesi Md. 3/5 Yönetim ve İş Planı Danışmanlığı yetkisi)*.

---

## 4. SOSYAL MEDYA DAĞITIMI VE HARİCİ PAZARLAMA UYUM KONTROLÜ

### 4.1 Operasyonel Gerçeklik: Sözleşmenin Sınırları
Host ile imzalanan "Konuk Eğitmen Sözleşmesi", platform içi hukuki çerçeveyi belirler; ancak **host'un kendi kişisel sosyal medya hesabındaki davranışlarını tek başına kontrol edemez.** Host'un Instagram hikayesinde *"Hafta sonu kampıma hepinizi bekliyorum"* diyerek seyahat acentesi ibaresi olmaksızın duyuru yapması, işlemin harici görünümünü fiilen belgesiz bir tura dönüştürebilir ve idari inceleme riski doğurabilir.

### 4.2 Yazılımsal Kontrol: Hazır Promosyon Araç Seti (Promotional Tool-Kit)
1. **Otomatik Görsel Üretimi:** İlan onaylandığında sistem, host fotoğraflarından Instagram Story (9:16) ve Post (1:1) formatında hazır şablonlar derler.
2. **Entegre Güvenlik Bileşenleri:** Şablonun üzerine kaldırılması mümkün olmayan şu unsurlar gömülür:
   * TÜRSAB Dijital Doğrulama Sistemi (DDS) Karekodu
   * *"Bu deneyim lisanslı LORAKS Seyahat Acentası operasyon güvencesiyle düzenlenmektedir"* ibaresi
   * Doğrudan platform üzerindeki güvenli rezervasyon bağlantısı.
3. **Pazarlama Argümanı:** Host'a bu durum bir kısıtlama olarak değil; *"Kullanıcılar artık merdiven altı turlardan çekiniyor; bu resmi acente rozeti senin güvenilirliğini tesciller ve rezervasyon dönüşümünü artırır"* değeriyle sunulur.

---

## 5. DİJİTAL UYUM YETKİNLİĞİ (COMPLIANCE AS A SERVICE YAKLAŞIMI)

### 5.1 Sahadaki Mevzuata Aykırılığı Kaynağında Azaltma Hedefi
* **Sektörel Durum:** TÜRSAB’ın sınırlı saha denetim kadrosu ve fiziki takip zorluğu karşısında, sosyal medyada ve sahada kontrolsüz paket tur satışı sektörel bir denetim darboğazı yaratmaktadır.
* **LORAKS’ın Tasarım Hedefi:** LORAKS, yetkili kurumlarca atanmış resmi bir denetim organı değildir; **ancak pazara ulaşan mevzuata aykırı faaliyeti, rezervasyon ve yayınlama öncesinde entegre uyum kontrolleriyle kaynağında azaltmak üzere tasarlanmış bir platformdur.**
* **GSTC Kriterleri:** Sürdürülebilirlik ilkeleri yalnızca defansif bir filtre değil, platformda listelenen deneyimlerin çevresel ve kültürel standart kalitesini yükselten bir iç akreditasyon aracıdır.

---

## 6. İKİLİ KURUMSAL MODEL (DUAL-ENTITY) VE DOST ACENTE PROTOKOLÜ

### 6.1 Sorumluluk ve Risk İzolasyon Mimarisi

| Parametre | LORAKS Teknoloji A.Ş. (Platform / Aracı) | LORAKS Seyahat Acentası A.Ş. (Acente / Principal) |
|---|---|---|
| **Yasal Statü** | 6563 Sayılı Kanun Kapsamında Aracı Hizmet Sağlayıcı (ETAHS) | 1618 Sayılı Kanun Kapsamında TÜRSAB A Grubu Seyahat Acentesi |
| **TFRS 15 Muhasebe Rolü** | **Vekil (Agent):** Brüt hacim ciro yazılamaz; sadece net komisyon hasılat kaydedilir. | **Asil (Principal):** Paket tur satıcısıdır; B2C seyahat faturasını düzenler. |
| **Kurumsal Risk** | 1. Fazda bağımsız kardeş şirket mimarisiyle TTK m.173/178 müteselsil borç riski izole edilir. | Seyahat operasyonunun ayıplı ifa, iptal, kaza ve sigorta yükümlülüklerini üstlenir. |
| **Sermaye / Maliyet** | Seyahat acentesi kuruluş harç blokajlarından muaf; sermaye yazılım ve pazarlamaya. | Resmi TÜRSAB giriş ödentisi ve seyahat teminat blokajlarını taşır. |

### 6.2 Dost Acente 9 Maddelik Geçiş Protokolü
Kendi A Grubu acente belgemiz faaliyete geçene kadar anlaşmalı dost acente ile yürütülen operasyonel prensipler:
* **Sıfır Operasyonel Yük:** Turun saha lojistiği acenteye yüklenmez, LORAKS koordinasyonunda yürütülür.
* **Pasif Lisans Payı:** Yapılan rezervasyonlardan acenteye net **%2–%3** pay aktarılır.
* **Rücu Garantisi:** Operasyonel kusurlardan doğabilecek cezai ve hukuki yükümlülükler sözleşmeyle LORAKS tarafından karşılanır.
* **Tek Tıkla Safe Exit (Madde 8.2):** Kendi acente belgemiz tamamlandığında, satış kanalı tazminatsız olarak kendi acentemize devredilir.

### 6.3 Dışsallaştırılmış Risk Tamponu (Externalized Risk Buffer)
*Ses Analizi Tespiti (Araba Ödünç Alma Analojisi):* LORAKS ile dost acente arasındaki B2B tam rücu sözleşmesi kamu savcısını ve TÜRSAB denetimini bağlamaz. Ağır bir kaza veya idari yaptırımda kamu doğrudan ruhsat sahibine (Dost Acente) gider; kapalı kapılar ardındaki sözleşme acentenin varlıklarının bloke edilmesini engelleyemez. Riski iki şirket arasında ping-pong topu olmaktan çıkarmak için risk üçüncü tarafça dışsallaştırılır:
1. **Özel Mesleki Sorumluluk & 3. Şahıs Mali Mesuliyet Sigortası:** LORAKS, primlerini bizzat ödeyerek operasyona özel kapsamlı bir poliçe yaptırır; kriz anında LORAKS'ın iyi niyetine değil, uluslararası sigorta şirketinin bilançosuna dayanılır.
2. **Rehinli Nakit Teminat Escrow Hesabı (Cash Collateral):** Geçiş dönemi boyunca bankada acente lehine bloke edilmiş ayrı bir teminat fonu tutulur. Acente olası bir kamu cezasını LORAKS'ı beklemeden bu fondan anında karşılayabilir.

---

## 7. FİNANSAL MİMARİ, BİRİM EKONOMİ VE MUTABAKAT

### 7.1 PSP Kontrollü Pazaryeri Mutabakatı (Safeguarded Settlement)
* **Terminoloji:** Müşteri fonları LORAKS'ın serbest cari hesaplarında tutulmaz; TCMB lisanslı Ödeme Hizmeti Sağlayıcısı (PSP - iyzico/PayTR) nezdindeki **Pazaryeri Güvenceli Mutabakat Hesabında** bloke edilir.
* **Çözülme Koşulu:** Deneyim tamamlanıp QR kod check-in doğrulaması yapılana kadar fonlar satıcıya aktarılmaz.

### 7.2 2.000,00 TL Birim Bilet Hesabı ve Uzlaştırılmış Marj Dengesi

Modelde **~%2,8 (56,00 TL) tutarındaki Sanal POS işlem maliyeti LORAKS tarafından üstlenilmektedir.**

| Finansal Kalem | Tutar | Açıklama ve Muhasebe Kaydı |
|---|---|---|
| **Brüt Bilet Bedeli (Gezgin Ödemesi)** | **2.000,00 TL** | PSP güvenli havuzuna tahsil edilir. |
| **LORAKS Komisyonu (%15 KDV Dahil)** | **300,00 TL** | LORAKS Teknoloji B2B E-Arşiv Faturası keser. |
| — KDV Hariç Komisyon Matrahı | 250,00 TL | LORAKS net hasılat matrahı. |
| — Hesaplanan KDV (%20) | 50,00 TL | Beyan edilecek KDV tutarı. |
| **Sanal POS Maliyeti (~%2,8)** | **-56,00 TL** | LORAKS tarafından ödenir (komisyon kârından düşer). |
| **7524 Sayılı Kanun %1 Stopajı** | **16,67 TL** | `2.000 / 1,20 = 1.666,67 TL` matrahın %1'i doğrudan GİB'e aktarılır. |
| **Net Satıcı / Host Hak Edişi** | **1.683,33 TL** | QR check-in sonrası host banka hesabına aktarılır. |
| **Aritmetik Mutabakat:** | **300,00 + 16,67 + 1.683,33 = 2.000,00 TL** | Tam denklem kuruşu kuruşuna dengededir. |

* **LORAKS Net Nakit Retansiyonu:** `300,00 TL - 56,00 TL = 244,00 TL` (Brüt biletin %12,2'si).
* **Ekonomik Tanım:** LORAKS saf bir SaaS değildir; **yazılım ölçeklenebilirliği ve marjlarına sahip bir TravelTech / RegTech Pazaryeri Altyapısıdır.**

### 7.3 Tersine Akış (Reverse Flow) ve İptal/İade Mutabakat Çıkmazı
*Ses Analizi Tespiti ("Macunu Tüpten Çıkarmak"):* Ödeme anında 16,67 TL stopaj GİB'e aktarılır ve VUK 509 faturası kesilirse; turun iptali veya hava muhalefeti durumunda devlete gitmiş parayı ve faturayı geri almak yüzlerce işlemde muhasebesel mutabakat kabusuna dönüşür.
* **Mimari Çözüm (Tahsilat ile Gerçekleşmenin Ayrılması):**
  * `withholdingTax` API tetikleyicisi ve e-arşiv fatura düzenleme anı, kart çekim anından koparılır; **etkinliğin kesinleştiği veya QR check-in'in yapıldığı milisaniyeye bağlanır.**
  * Rezervasyon anında fonlar havuzda vergisiz saf emanet olarak bekler. İptal gerçekleşirse, hiçbir vergi iptal prosedürüne girmeden doğrudan PSP üzerinden kart iadesi yapılır.
* **Mevzuat İhtiyatı (Otomatik İade Döngüsü):** Mevzuat verginin tahsilat anında kesilmesini zorunlu kılarsa; sistem arka planda insan müdahalesi gerektirmeyen **tam otomatik bir Gider Pusulası / İade Faturası (Automated Refund Loop)** döngüsü çalıştırır.

### 7.5 KVK m. 13 Şirketler Arası Hizmet Faturalandırması ve POS Masraf Yalıtımı
5520 Sayılı Kurumlar Vergisi Kanunu m. 13 (Transfer Fiyatlandırması Yoluyla Örtülü Kazanç Dağıtımı) uyarınca, ilişkili şirketler arasında bedelsiz hizmet verilmesi ve masraf kaydırılması yasaktır:
1. **Zorunlu Hizmet Faturası:** LORAKS Teknoloji A.Ş., sağladığı bulut sunucu (AWS), SMS/e-posta altyapısı, yazılım bakım ve destek operasyonlarını kardeş şirket LORAKS Seyahat Acentası A.Ş.'ye bedelsiz kullandıramaz. Her ay paylaşılan maliyetler üzerinden **%10 emsal kâr marjlı (Cost-Plus Yöntemi)** veya P2 brüt işlem hacmi üzerinden **%5 teknoloji lisans bedeli** ile B2B e-Fatura kesilmesi zorunludur (`src/intercompany_billing.py`).
2. **POS Masraf Yalıtım Kuralı (Hard Invariant):** Masrafı ödeyen şirket, hasılatı yazan şirket ile birebir aynı olmalıdır. P0/P1 atölye POS masrafı Teknoloji A.Ş. 653 hesabına; P2 paket tur POS masrafı ise Acente A.Ş. 653 hesabına işlenir. Yanlış şirkete POS masrafı aktarımı yazılımsal olarak engellenmiştir (`ComplianceViolationException`).

### 7.6 Zorunlu Sigorta BSMV Yalıtımı ve No-Show Tazminat Vergi Statüsü
1. **1618 S.K. Zorunlu Paket Tur Sigortası BSMV Ayrıştırması:** P2 paket turlarda kesilen Zorunlu Seyahat Sigortası poliçe primi (örn. 50 TL), 6802 Sayılı Gider Vergileri Kanunu uyarınca Banka ve Sigorta Muameleleri Vergisi'ne (BSMV) tabidir ve KDV'den istisnadır. Bu bedel bilet brütünden düşülerek KDV matrahı yalnızca kalan net hizmet tutarı üzerinden hesaplanır (`src/tax_engine.py`).
2. **No-Show ve İptal Kesintilerinde Cayma Tazminatı Statüsü:** Misafirin etkinliğe katılmaması veya son 24 saatte iptal etmesi halinde alıkonulan cezai şart bedeli, bir "hizmet teslimi" değil 6098 Sayılı Türk Borçlar Kanunu uyarınca **"Sözleşmesel Cayma Tazminatı"** niteliğindedir. Tazminatlar KDV'ye ve 7524 Sayılı Kanun e-ticaret hasılat stopajına tabi değildir; doğrudan 679 Olağandışı Gelirler hesabına kaydedilir.

### 7.7 6493 S.K. T+1 Otomatik Hak Ediş Salınımı ve Lisanssız Havuz Engeli
6493 Sayılı Ödeme Hizmetleri Kanunu uyarınca, TCMB lisansı olmayan şirketlerin müşteri fonlarını vadesiz mevduat gibi bünyesinde tutması suçtur:
1. **Zorunlu T+1 Dağıtımı:** QR kod okutularak kesinleşen host hak edişleri, en geç ifayı takip eden T+1 iş gününde otomatik PSP talimatıyla host IBAN'ına gönderilir (`src/payout_engine.py`).
2. **İçeride Bakiye Biriktirme Talebi Engeli:** Hostun "Paramı sistemde biriktirin, ay sonunda toplu gönderin" talebi sistem tarafından 6493 S.K. gereği otomatik olarak reddedilir; platformun izinsiz bankacılık/ödeme kuruluşu muamelesi görmesi engellenir.

---

## 8. LORAKS CIRCLE: KAPALI DEVRE İSKONTO VE SADAKAT

* **6493 Sayılı Kanun Sınırları:** LORAKS Circle bir elektronik para, ödeme aracı veya nakit cüzdanı değildir. Puanlar nakde çevrilemez, transfer edilemez.
* **Ticari İskonto Niteliği:** Biriken puanlar, bir sonraki rezervasyonda B2C hizmet bedelinden doğrudan **"Ticari İskonto"** olarak mahsup edilir; ek stopaj veya lisans yükümlülüğü doğurmaz.

---

## 9. AÇIKLAYICI 3 YILLIK İŞLETME SENARYOLARI (ILLUSTRATIVE SCENARIOS)

Aşağıdaki veriler kesin birer taahhüt veya tahmin değil; operasyonel varsayımlara dayalı **açıklayıcı yönetim senaryolarıdır (Management Scenarios)**:

| Metrik | 1. Yıl (2026–2027) | 2. Yıl (Temel Senaryo) | 2. Yıl (Agresif Senaryo) | 3. Yıl (Ölçeklenme) |
|---|---|---|---|---|
| **Aktif Host / Sağlayıcı** | 150 | 500 | 1.200 | 1.500+ |
| **Toplam Rezervasyon** | 20.000 | 85.000 | 200.000 | 320.000 |
| **Brüt İşlem Hacmi (GMV)** | 20.000.000 TL | 85.000.000 TL | 243.000.000 TL | 320.000.000 TL+ |
| **Net Platform Komisyonu (%15)**| 3.000.000 TL | 12.750.000 TL | 36.450.000 TL | 48.000.000 TL |
| **SMMM & B2B Yan Gelirler** | 450.000 TL | 2.200.000 TL | 6.500.000 TL | 8.500.000 TL |
| **Net Platform Hasılatı** | **3.450.000 TL** | **14.950.000 TL** | **42.950.000 TL** | **56.500.000 TL** |

*(Not: Önceki araştırmalardaki 243M TL GMV hedefi agresif pazar penetrasyonu senaryosunu; 85M TL GMV ise kontrollü kategori bazlı organik büyüme temel senaryosunu temsil etmektedir).*

---

## 10. YÖNETİŞİM, YÖNETİM VE KURUMSAL YETKİNLİKLER (GOVERNANCE)

Çekirdek operasyonel ekip ve kurumsal yetkinlik matrisi:

* **Ayşegül Denizli (Kurucu & Stratejik Ürün Mimarı):** Deneyim standartları, kürasyon kalitesi, "Modern Anadolu Ev Sahipliği" konsepti ve topluluk mimarisi.
* **Mehmet Bağbozan (Kurucu Ortak & Yönetim Kurulu Başkanı):** Strateji, RegTech/FinTech tasarımı, mevzuat uyumu.  
  * *Mesleki Güvence:* T.C. Kültür ve Turizm Bakanlığı Seyahat Acentaları **Enformasyon Memurluğu Belgesi (No: 2387)** sahibidir; A Grubu acente sorumlu müdürlük yasal gereksinimini karşılar.
* **Gökhan Ekre (Kurucu Ortak & Operasyon Direktörü):** Saha operasyonları, lisanslı D2 transfer ağı yönetimi, tedarikçi lojistik koordinasyonu.
* **Ray Erdemir (Kurucu Ortak & B2B Büyüme Direktörü):** LORAKS for Business kurumsal İK satışları, kurumsal etkinlik paketleri ve stratejik B2B ortaklıklar.

---

## 11. 30 GÜNLÜK UYGULAMA VE GO-LIVE PLANI

* **Hafta 1 — Arayüz & Hukuki Çerçeve:** Doğal Keten (`#FDFCF8`) ve Çam Yeşili (`#1A432E`) tasarım dili; Kullanıcı Sözleşmesi, MSS ve Dost Acente belge numarası entegrasyonu.
* **Hafta 2 — Uyum Motoru & PSP Entegrasyonu:** P0–P4 kural sınıflandırması, PSP mutabakat API'si ve otomatik sosyal medya şablon motorunun bağlanması.
* **Hafta 3 — Amiral Turlar & Onboarding Sepeti:** İlk 50 Kurucu Host'un sisteme kabulü; Şef Sofraları, Tekne Yoga ve Bağ Bozumu amiral listelemeleri.
* **Hafta 4 — Test & Canlı İşlem:** Idempotency, cent mutabakatı ve QR check-in testleri; ilk canlı kart çekimi ile platform lansmanı.

---
*İşbu Belge, LORAKS ekosisteminin v5.3 Mimari ve Stratejik Referans Anayasasıdır.*
