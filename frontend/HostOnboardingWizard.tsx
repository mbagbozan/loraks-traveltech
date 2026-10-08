import React, { useState } from 'react';

interface WizardState {
  title: string;
  category: string;
  description: string;
  location: string;
  venueType: 'fixed' | 'transport_included';
  venueEnvironment: 'studio' | 'home' | 'outdoor';
  price: number;
  hasCompany: boolean | null;
  needsSmmmHelp: boolean;
  hasHygieneOrGuideCert: boolean;
  
  // Safe Harbor & RegTech Uyum Alanları (v3.2)
  isOvernight: boolean;
  alcoholServed: boolean;
  allergenDeclarationAccepted: boolean;
  isMultiStop: boolean;
  hasTurebLicense: boolean;
  turebLicenseNo: string;
  nonGuidingWarrantyAccepted: boolean;
}

export const HostOnboardingWizard: React.FC = () => {
  const [step, setStep] = useState<number>(1);
  const [validationError, setValidationError] = useState<string | null>(null);
  const [state, setState] = useState<WizardState>({
    title: '',
    category: 'workshop',
    description: '',
    location: '',
    venueType: 'fixed',
    venueEnvironment: 'studio',
    price: 1500,
    hasCompany: null,
    needsSmmmHelp: false,
    hasHygieneOrGuideCert: false,
    isOvernight: false,
    alcoholServed: false,
    allergenDeclarationAccepted: false,
    isMultiStop: false,
    hasTurebLicense: false,
    turebLicenseNo: '',
    nonGuidingWarrantyAccepted: false,
  });

  // Otomatik Pathway ve Komisyon Tespiti
  const isP2Regulated = state.venueType === 'transport_included' || state.isOvernight;
  const commissionRate = isP2Regulated ? 0.12 : 0.15;
  const platformFee = Math.round(state.price * commissionRate);
  const taxWithholding = Math.round(state.price * 0.01);
  const netHostPayout = state.price - platformFee - taxWithholding;

  const validateStep2 = (): boolean => {
    setValidationError(null);

    // Senaryo F: Evde yemek ve alkol yasağı (TAPDK)
    if (state.venueEnvironment === 'home' && state.alcoholServed) {
      setValidationError('TAPDK 4733 S.K. Kısıtı: Ev ve konut ortamlarında para karşılığı alkollü içki sunumu kanunen yasaktır. Alkol servisi yalnızca TAPDK ruhsatlı ticari işletmelerde yapılabilir.');
      return false;
    }

    // Senaryo F: Gıda alerjen formu
    if (state.category === 'food' && !state.allergenDeclarationAccepted) {
      setValidationError('Gıda Güvenliği Şartı: Yemek etkinliklerinde katılımcı Alerjen ve Sağlık Beyan Formu taahhüdünün onaylanması yasal olarak zorunludur.');
      return false;
    }

    // Senaryo A: Çok duraklı sokak yürüyüşü & TUREB 6326 S.K.
    if (state.isMultiStop && !state.hasTurebLicense && !state.nonGuidingWarrantyAccepted) {
      setValidationError('TUREB 6326 S.K. Kalkanı: Çok duraklı açık alan gezilerinde Turist Rehberi kokartı yoksa, etkinliğin tarihi rehberlik değil teknik atölye olduğunu beyan eden taahhüt kutusu onaylanmalıdır.');
      return false;
    }

    return true;
  };

  const handleNextToStep3 = () => {
    if (validateStep2()) {
      setStep(3);
    }
  };

  return (
    <div className="max-w-2xl mx-auto my-10 p-8 bg-[#FDFCF8] rounded-2xl border border-[#EBE7DC] shadow-sm font-sans text-[#2C2A29]">
      {/* İlerleme Çubuğu */}
      <div className="flex items-center justify-between mb-8 pb-4 border-b border-[#EBE7DC]">
        <div>
          <span className="text-xs uppercase tracking-wider text-[#8FAF8C] font-semibold">Ev Sahibi Güvenli Yolculuğu</span>
          <h2 className="font-serif text-2xl text-[#1A432E] mt-0.5">Deneyimini Paylaş (v3.2)</h2>
        </div>
        <div className="text-sm font-medium text-[#8FAF8C]">Adım {step} / 3</div>
      </div>

      {validationError && (
        <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-xl text-xs text-red-800 leading-relaxed">
          <strong>⚠️ Mevzuat Uyarısı:</strong> {validationError}
        </div>
      )}

      {/* ADIM 1: TEMEL BİLGİLER */}
      {step === 1 && (
        <div className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-[#1A432E] mb-2">Deneyiminin Adı Nedir?</label>
            <input
              type="text"
              placeholder="Örn: Urla Bağlarında Günbatımı ve Doğal Zeytinyağı Tadımı"
              className="w-full px-4 py-3 bg-white border border-[#EBE7DC] rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1A432E]/20 text-[#2C2A29]"
              value={state.title}
              onChange={(e) => setState({ ...state, title: e.target.value })}
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-[#1A432E] mb-2">Kategori</label>
            <select
              className="w-full px-4 py-3 bg-white border border-[#EBE7DC] rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1A432E]/20"
              value={state.category}
              onChange={(e) => setState({ ...state, category: e.target.value })}
            >
              <option value="workshop">Zanaat & Sanat Atölyesi (Seramik, Resim vb.)</option>
              <option value="food">Mutfak, Sofra & Tadım Buluşmaları</option>
              <option value="retreat">Doğa, Yoga & Esenlik Buluşması</option>
              <option value="camp">Doğa Kampı & Konaklama</option>
              <option value="cultural">Kültür, Tarih & Şehir Yürüyüşü</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-[#1A432E] mb-2">Deneyimini Kısaca Anlat</label>
            <textarea
              rows={4}
              placeholder="Misafirlerini nasıl bir ortam bekliyor? Neler yapacaksınız?"
              className="w-full px-4 py-3 bg-white border border-[#EBE7DC] rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1A432E]/20"
              value={state.description}
              onChange={(e) => setState({ ...state, description: e.target.value })}
            />
          </div>

          <button
            onClick={() => setStep(2)}
            className="w-full py-3.5 bg-[#1A432E] hover:bg-[#133323] text-white font-medium rounded-xl transition shadow-sm"
          >
            Devam Et →
          </button>
        </div>
      )}

      {/* ADIM 2: BULUŞMA, MEKAN VE REGTECH GÜVENLİK FİLTRESİ */}
      {step === 2 && (
        <div className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-[#1A432E] mb-2">Nerede Buluşacaksınız?</label>
            <input
              type="text"
              placeholder="Örn: Kadıköy Atölye veya Urla Bağ Evi"
              className="w-full px-4 py-3 bg-white border border-[#EBE7DC] rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1A432E]/20"
              value={state.location}
              onChange={(e) => setState({ ...state, location: e.target.value })}
            />
          </div>

          {/* Mekan Türü ve Çevre */}
          <div>
            <label className="block text-sm font-medium text-[#1A432E] mb-2">Mekan Türü</label>
            <div className="grid grid-cols-3 gap-2">
              <button
                type="button"
                className={`py-2.5 px-3 rounded-xl border text-xs font-medium transition ${state.venueEnvironment === 'studio' ? 'bg-[#1A432E] text-white border-[#1A432E]' : 'bg-white text-[#63605D] border-[#EBE7DC]'}`}
                onClick={() => setState({ ...state, venueEnvironment: 'studio' })}
              >
                Ticari Stüdyo / Atölye
              </button>
              <button
                type="button"
                className={`py-2.5 px-3 rounded-xl border text-xs font-medium transition ${state.venueEnvironment === 'home' ? 'bg-[#1A432E] text-white border-[#1A432E]' : 'bg-white text-[#63605D] border-[#EBE7DC]'}`}
                onClick={() => setState({ ...state, venueEnvironment: 'home' })}
              >
                Ev / Konut Ortamı
              </button>
              <button
                type="button"
                className={`py-2.5 px-3 rounded-xl border text-xs font-medium transition ${state.venueEnvironment === 'outdoor' ? 'bg-[#1A432E] text-white border-[#1A432E]' : 'bg-white text-[#63605D] border-[#EBE7DC]'}`}
                onClick={() => setState({ ...state, venueEnvironment: 'outdoor' })}
              >
                Açık Hava / Doğa
              </button>
            </div>
          </div>

          {/* Senaryo B: Geceleme & Kamp Kontrolü */}
          <div className="p-4 bg-white border border-[#EBE7DC] rounded-xl space-y-3">
            <label className="flex items-center gap-3 cursor-pointer">
              <input
                type="checkbox"
                checked={state.isOvernight || state.category === 'camp'}
                onChange={(e) => setState({ ...state, isOvernight: e.target.checked })}
                className="accent-[#1A432E] w-4 h-4 rounded"
              />
              <span className="text-sm font-medium text-[#1A432E]">
                Bu deneyim geceleme, çadır veya konaklama içeriyor.
              </span>
            </label>
            {(state.isOvernight || state.category === 'camp') && (
              <div className="p-3 bg-amber-50 border border-amber-200 rounded-lg text-xs text-amber-800 leading-relaxed">
                🛡️ <strong>1618 S.K. Seyahat Kalkanı Devrede:</strong> Geceleme içeren tüm deneyimler LORAKS Seyahat Acentesi A.Ş. yasal şemsiyesi altına alınır ve misafir adına Zorunlu Paket Tur Sigortası düzenlenir. Komisyon %12'ye optimize edilir.
              </div>
            )}
          </div>

          {/* Senaryo F: Supper Club & Alkol / Alerjen Kontrolü */}
          {state.category === 'food' && (
            <div className="p-4 bg-white border border-[#EBE7DC] rounded-xl space-y-3">
              <span className="font-semibold text-xs text-[#1A432E] uppercase tracking-wider block">Gastronomi & Mutfak Uyumu</span>
              
              <label className="flex items-center gap-3 cursor-pointer">
                <input
                  type="checkbox"
                  checked={state.alcoholServed}
                  onChange={(e) => setState({ ...state, alcoholServed: e.target.checked })}
                  className="accent-[#1A432E] w-4 h-4 rounded"
                />
                <span className="text-xs text-[#2C2A29]">Deneyim sırasında alkollü içki servisi/tadımı yer alıyor.</span>
              </label>

              {state.venueEnvironment === 'home' && state.alcoholServed && (
                <div className="p-3 bg-red-50 border border-red-200 rounded-lg text-xs text-red-700">
                  ❌ <strong>TAPDK 4733 S.K. Engeli:</strong> Evde ücretli alkol sunumu yasaktır. Lütfen alkol sunumunu kaldırın veya ruhsatlı bir mekana geçin.
                </div>
              )}

              <label className="flex items-center gap-3 cursor-pointer">
                <input
                  type="checkbox"
                  checked={state.allergenDeclarationAccepted}
                  onChange={(e) => setState({ ...state, allergenDeclarationAccepted: e.target.checked })}
                  className="accent-[#1A432E] w-4 h-4 rounded"
                />
                <span className="text-xs text-[#2C2A29]">Katılımcılara sunulacak Gıda Alerjen & Sağlık Beyan Formu taahhüdünü kabul ediyorum.</span>
              </label>
            </div>
          )}

          {/* Senaryo A: Çok Duraklı Gezi & TUREB 6326 Kokart Kontrolü */}
          <div className="p-4 bg-white border border-[#EBE7DC] rounded-xl space-y-3">
            <label className="flex items-center gap-3 cursor-pointer">
              <input
                type="checkbox"
                checked={state.isMultiStop}
                onChange={(e) => setState({ ...state, isMultiStop: e.target.checked })}
                className="accent-[#1A432E] w-4 h-4 rounded"
              />
              <span className="text-sm font-medium text-[#1A432E]">Birden fazla duraklı sokak veya rota yürüyüşü içeriyor.</span>
            </label>

            {state.isMultiStop && (
              <div className="space-y-3 pt-2">
                <label className="flex items-center gap-2 text-xs cursor-pointer">
                  <input
                    type="checkbox"
                    checked={state.hasTurebLicense}
                    onChange={(e) => setState({ ...state, hasTurebLicense: e.target.checked })}
                    className="accent-[#1A432E] rounded"
                  />
                  <span>T.C. Kültür ve Turizm Bakanlığı kokartlı Turist Rehberiyim</span>
                </label>

                {!state.hasTurebLicense && (
                  <div className="p-3 bg-blue-50 border border-blue-200 rounded-lg space-y-2">
                    <span className="text-xs font-semibold text-blue-900 block">6326 S.K. Rehberlik Koruması Taahhüdü:</span>
                    <label className="flex items-start gap-2 text-xs text-blue-800 cursor-pointer">
                      <input
                        type="checkbox"
                        checked={state.nonGuidingWarrantyAccepted}
                        onChange={(e) => setState({ ...state, nonGuidingWarrantyAccepted: e.target.checked })}
                        className="accent-[#1A432E] mt-0.5 rounded"
                      />
                      <span>"Bu etkinlik süresince tarihi ve kültürel rehberlik yapılmayacak; yalnızca teknik sanat/fotoğraf eğitimi verilecektir." taahhüdünü onaylıyorum.</span>
                    </label>
                  </div>
                )}
              </div>
            )}
          </div>

          <div className="flex gap-3">
            <button
              onClick={() => setStep(1)}
              className="w-1/3 py-3.5 border border-[#EBE7DC] text-[#63605D] hover:bg-white font-medium rounded-xl"
            >
              ← Geri
            </button>
            <button
              onClick={handleNextToStep3}
              className="w-2/3 py-3.5 bg-[#1A432E] hover:bg-[#133323] text-white font-medium rounded-xl transition shadow-sm"
            >
              Fiyat & Kazanç Adımına Geç →
            </button>
          </div>
        </div>
      )}

      {/* ADIM 3: FİYAT VE GİRİŞİMCİLİK KULUÇKASI & GVK m.9 TAKİBİ */}
      {step === 3 && (
        <div className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-[#1A432E] mb-2">Kişi Başı Katılım Bedeli (TL)</label>
            <input
              type="number"
              className="w-full px-4 py-3 bg-white border border-[#EBE7DC] rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1A432E]/20 text-lg font-semibold"
              value={state.price}
              onChange={(e) => setState({ ...state, price: Number(e.target.value) })}
            />
          </div>

          {/* Şeffaf ve Net Para Hesabı */}
          <div className="p-4 bg-white border border-[#EBE7DC] rounded-xl space-y-2 text-sm">
            <div className="flex justify-between text-[#63605D]">
              <span>Bilet Fiyatı:</span>
              <span className="font-medium">{state.price.toLocaleString('tr-TR')} TL</span>
            </div>
            <div className="flex justify-between text-[#63605D]">
              <span>Platform Hizmet Payı (%{(commissionRate * 100).toFixed(0)}):</span>
              <span>- {platformFee.toLocaleString('tr-TR')} TL</span>
            </div>
            <div className="flex justify-between text-[#63605D]">
              <span>7524 Sayılı Yasal Stopaj (%1 GİB):</span>
              <span>- {taxWithholding.toLocaleString('tr-TR')} TL</span>
            </div>
            <div className="pt-2 border-t border-[#EBE7DC] flex justify-between font-semibold text-[#1A432E] text-base">
              <span>Cebinize Kalan Net Kazanç:</span>
              <span>{netHostPayout.toLocaleString('tr-TR')} TL</span>
            </div>
            <div className="text-[11px] text-[#8FAF8C] pt-1">
              * QR Check-in sonrasında ertesi iş günü (T+1) doğrudan banka IBAN hesabınıza yatırılır (6493 S.K. tam güvence).
            </div>
          </div>

          {/* GVK m. 9 ESNAF MUAFIYETI VE VITRIN SMMM KARTI */}
          <div className="p-5 bg-[#8FAF8C]/10 border border-[#8FAF8C]/30 rounded-xl space-y-3">
            <div className="flex items-center gap-2">
              <span className="text-lg">📈</span>
              <h4 className="font-semibold text-sm text-[#1A432E]">GVK m.9 Esnaf Muafiyeti & SMMM Rehberliği</h4>
            </div>
            <p className="text-xs text-[#63605D] leading-relaxed">
              Bireysel üreticilerimiz için 2026 yılı <strong>1.100.000 TL</strong> Esnaf Muafiyeti tavanı sistemimizce otomatik takip edilir. Sınırın %80'ine ulaştığınızda bildirim alırsınız; şirketleşme sürecinizi anlaşmalı Vitrin SMMM ağımızla 24 saatte tamamlayabilirsiniz.
            </p>
            <label className="flex items-center gap-2 text-xs font-medium text-[#1A432E] cursor-pointer">
              <input
                type="checkbox"
                checked={state.needsSmmmHelp}
                onChange={(e) => setState({ ...state, needsSmmmHelp: e.target.checked })}
                className="accent-[#1A432E] rounded"
              />
              Evet, ücretsiz mali müşavir ve esnaf muafiyeti rehberliği istiyorum.
            </label>
          </div>

          <div className="flex gap-3">
            <button
              onClick={() => setStep(2)}
              className="w-1/3 py-3.5 border border-[#EBE7DC] text-[#63605D] hover:bg-white font-medium rounded-xl"
            >
              ← Geri
            </button>
            <button
              onClick={() => alert('🎉 Harika! Deneyiminiz mevzuata tam uyumlu olarak incelenmek üzere oluşturuldu.')}
              className="w-2/3 py-3.5 bg-[#C86D51] hover:bg-[#B55D42] text-white font-semibold rounded-xl transition shadow-sm"
            >
              Deneyimi Yayına Al 🎉
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
