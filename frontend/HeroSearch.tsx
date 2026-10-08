import React, { useState } from 'react';

export const HeroSearch: React.FC = () => {
  const [location, setLocation] = useState('');
  const [category, setCategory] = useState('');
  const [date, setDate] = useState('');

  return (
    <div className="w-full bg-[#FDFCF8] py-16 px-6 border-b border-[#EBE7DC]">
      <div className="max-w-4xl mx-auto text-center space-y-4">
        <span className="text-xs uppercase tracking-widest text-[#8FAF8C] font-semibold">
          Kendine Zaman Tanı
        </span>
        <h1 className="font-serif text-3xl md:text-5xl text-[#1A432E] leading-tight">
          Özenle seçilmiş sofralar, zanaat ve yaşayan buluşmalar.
        </h1>
        <p className="text-[#63605D] text-sm md:text-base max-w-xl mx-auto">
          Ekranlardan uzaklaş; yerel zanaatkarların atölyelerine, bağ sofralarına ve doğanın kalbine konuk ol.
        </p>

        {/* Arama Çubuğu */}
        <div className="mt-8 bg-white p-3 rounded-2xl shadow-sm border border-[#EBE7DC] grid grid-cols-1 md:grid-cols-4 gap-3 text-left">
          {/* Nereye */}
          <div className="p-2 border-b md:border-b-0 md:border-r border-[#EBE7DC]">
            <label className="block text-[11px] font-bold text-[#1A432E] uppercase tracking-wider">Nereye?</label>
            <input
              type="text"
              placeholder="Urla, Kadıköy, Kaş..."
              className="w-full text-xs text-[#2C2A29] focus:outline-none placeholder:text-[#63605D]/60 mt-1"
              value={location}
              onChange={(e) => setLocation(e.target.value)}
            />
          </div>

          {/* Ne Tür Deneyim */}
          <div className="p-2 border-b md:border-b-0 md:border-r border-[#EBE7DC]">
            <label className="block text-[11px] font-bold text-[#1A432E] uppercase tracking-wider">Hangi Buluşma?</label>
            <select
              className="w-full text-xs text-[#2C2A29] focus:outline-none bg-transparent mt-1"
              value={category}
              onChange={(e) => setCategory(e.target.value)}
            >
              <option value="">Tüm Deneyimler</option>
              <option value="sofra">Sofra & Gastronomi</option>
              <option value="zanaat">Zanaat & Sanat</option>
              <option value="doga">Doğa & Esenlik</option>
            </select>
          </div>

          {/* Ne Zaman */}
          <div className="p-2 border-b md:border-b-0 border-[#EBE7DC]">
            <label className="block text-[11px] font-bold text-[#1A432E] uppercase tracking-wider">Ne Zaman?</label>
            <input
              type="date"
              className="w-full text-xs text-[#2C2A29] focus:outline-none bg-transparent mt-1"
              value={date}
              onChange={(e) => setDate(e.target.value)}
            />
          </div>

          {/* Ara Butonu */}
          <div className="flex items-center">
            <button
              onClick={() => alert(`Arama yapılıyor: ${location || 'Tümü'}, ${category || 'Tümü'}`)}
              className="w-full h-full py-3 bg-[#1A432E] hover:bg-[#133323] text-white text-sm font-semibold rounded-xl transition shadow-sm flex items-center justify-center gap-2"
            >
              <span>🔍</span>
              <span>Keşfet</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
