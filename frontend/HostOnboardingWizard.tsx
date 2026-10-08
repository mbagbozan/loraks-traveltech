import React, { useState } from 'react';

interface WizardState {
  title: string;
  category: string;
  description: string;
  location: string;
  venueType: 'fixed' | 'transport_included' | 'self_arrival';
  price: number;
  hasCompany: boolean | null;
  needsSmmmHelp: boolean;
  hasHygieneOrGuideCert: boolean;
}

export const HostOnboardingWizard: React.FC = () => {
  const [step, setStep] = useState<number>(1);
  const [state, setState] = useState<WizardState>({
    title: '',
    category: 'workshop',
    description: '',
    location: '',
    venueType: 'fixed',
    price: 1000,
    hasCompany: null,
    needsSmmmHelp: false,
    hasHygieneOrGuideCert: false,
  });

  // Basit Net Kazanç Hesabı (Arka planda sessizce çalışan FinTech)
  const platformFee = Math.round(state.price * 0.15);
  const taxWithholding = Math.round(state.price * 0.01);
  const netHostPayout = state.price - platformFee - taxWithholding;

  return (
    <div className="max-w-2xl mx-auto my-10 p-8 bg-[#FDFCF8] rounded-2xl border border-[#EBE7DC] shadow-sm font-sans text-[#2C2A29]">
      {/* İlerleme Çubuğu */}
      <div className="flex items-center justify-between mb-8 pb-4 border-b border-[#EBE7DC]">
        <div>
          <span className="text-xs uppercase tracking-wider text-[#8FAF8C] font-semibold">Ev Sahibi Yolculuğu</span>
          <h2 className="font-serif text-2xl text-[#1A432E] mt-0.5">Deneyimini Paylaş</h2>
        </div>
        <div className="text-sm font-medium text-[#8FAF8C]">Adım {step} / 3</div>
      </div>

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

      {/* ADIM 2: BULUŞMA VE YOLCULUK */}
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

          <div>
            <label className="block text-sm font-medium text-[#1A432E] mb-2">Ulaşım ve Buluşma Şekli</label>
            <div className="grid grid-cols-1 gap-3">
              <label className="flex items-center p-4 border border-[#EBE7DC] bg-white rounded-xl cursor-pointer hover:border-[#1A432E]/50">
                <input
                  type="radio"
                  name="venueType"
                  checked={state.venueType === 'fixed'}
                  onChange={() => setState({ ...state, venueType: 'fixed' })}
                  className="accent-[#1A432E] mr-3"
                />
                <div>
                  <span className="font-medium text-sm text-[#1A432E] block">Sabit Mekanımda Buluşuyoruz</span>
                  <span className="text-xs text-[#63605D]">Misafirler kendi imkanlarıyla atölyeme/evime gelir. (Hemen bugün satışa açılabilir)</span>
                </div>
              </label>

              <label className="flex items-center p-4 border border-[#EBE7DC] bg-white rounded-xl cursor-pointer hover:border-[#1A432E]/50">
                <input
                  type="radio"
                  name="venueType"
                  checked={state.venueType === 'transport_included'}
                  onChange={() => setState({ ...state, venueType: 'transport_included' })}
                  className="accent-[#1A432E] mr-3"
                />
                <div>
                  <span className="font-medium text-sm text-[#1A432E] block">Ulaşım / Transfer Dahil Olsun İstiyorum</span>
                  <span className="text-xs text-[#63605D]">LORAKS anlaşmalı D2 lisanslı araç desteği ve seyahat sigortası kalkanıyla korunur.</span>
                </div>
              </label>
            </div>
          </div>

          <div className="flex gap-3">
            <button
              onClick={() => setStep(1)}
              className="w-1/3 py-3.5 border border-[#EBE7DC] text-[#63605D] hover:bg-white font-medium rounded-xl"
            >
              ← Geri
            </button>
            <button
              onClick={() => setStep(3)}
              className="w-2/3 py-3.5 bg-[#1A432E] hover:bg-[#133323] text-white font-medium rounded-xl transition shadow-sm"
            >
              Fiyat & Kazanç Adımına Geç →
            </button>
          </div>
        </div>
      )}

      {/* ADIM 3: FİYAT VE GİRİŞİMCİLİK KULUÇKASI */}
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
              <span>Platform Hizmet Payı (%15):</span>
              <span>- {platformFee.toLocaleString('tr-TR')} TL</span>
            </div>
            <div className="flex justify-between text-[#63605D]">
              <span>Yasal Vergi Tevkifatı (%1):</span>
              <span>- {taxWithholding.toLocaleString('tr-TR')} TL</span>
            </div>
            <div className="pt-2 border-t border-[#EBE7DC] flex justify-between font-semibold text-[#1A432E] text-base">
              <span>Cebinize Kalan Net Kazanç:</span>
              <span>{netHostPayout.toLocaleString('tr-TR')} TL</span>
            </div>
          </div>

          {/* VİTRİN SMMM & GİRİŞİMCİLİK KULUÇKASI KARTI */}
          <div className="p-5 bg-[#8FAF8C]/10 border border-[#8FAF8C]/30 rounded-xl space-y-3">
            <div className="flex items-center gap-2">
              <span className="text-lg">📢</span>
              <h4 className="font-semibold text-sm text-[#1A432E]">Şirketiniz veya Muhasebeciniz Yok mu?</h4>
            </div>
            <p className="text-xs text-[#63605D] leading-relaxed">
              Hiç endişelenmeyin! Genç Girişimci istisnası, Esnaf Muafiyeti veya 24 saatte online şirket açılışını 
              anlaşmalı dijital mali müşavir ağımızla biz çözüyoruz.
            </p>
            <label className="flex items-center gap-2 text-xs font-medium text-[#1A432E] cursor-pointer">
              <input
                type="checkbox"
                checked={state.needsSmmmHelp}
                onChange={(e) => setState({ ...state, needsSmmmHelp: e.target.checked })}
                className="accent-[#1A432E] rounded"
              />
              Evet, ücretsiz mali müşavir ve şirketleşme rehberliği istiyorum.
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
              onClick={() => alert('Harika! Deneyiminiz incelenmek üzere başarıyla oluşturuldu.')}
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
