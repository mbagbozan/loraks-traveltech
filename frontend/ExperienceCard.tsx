import React from 'react';

export interface ExperienceCardProps {
  id: string;
  title: string;
  category: string;
  location: string;
  price: number;
  imageUrl: string;
  hostName: string;
  hostAvatarUrl?: string;
  rating?: number;
  reviewCount?: number;
  duration?: string;
  badgeText?: string;
}

export const ExperienceCard: React.FC<ExperienceCardProps> = ({
  title,
  category,
  location,
  price,
  imageUrl,
  hostName,
  hostAvatarUrl,
  rating = 4.9,
  reviewCount = 12,
  duration = '2.5 saat',
  badgeText = 'Özenle Seçilmiş',
}) => {
  return (
    <div className="group bg-white rounded-2xl border border-[#EBE7DC] overflow-hidden hover:shadow-md transition duration-200 flex flex-col font-sans">
      {/* Görsel Alanı */}
      <div className="relative aspect-[4/3] w-full overflow-hidden bg-[#F5F3EB]">
        <img
          src={imageUrl}
          alt={title}
          className="w-full h-full object-cover group-hover:scale-105 transition duration-300"
        />
        {/* Zarif Rozet */}
        <span className="absolute top-3 left-3 bg-[#FDFCF8]/95 backdrop-blur-sm text-[#1A432E] text-xs font-semibold px-3 py-1 rounded-full shadow-sm">
          🌿 {badgeText}
        </span>
      </div>

      {/* İçerik Alanı */}
      <div className="p-5 flex flex-col flex-1 justify-between">
        <div>
          {/* Lokasyon ve Süre */}
          <div className="flex items-center justify-between text-xs text-[#63605D] mb-1.5">
            <span>📍 {location}</span>
            <span>⏱️ {duration}</span>
          </div>

          {/* Başlık */}
          <h3 className="font-serif text-lg text-[#1A432E] line-clamp-2 leading-snug group-hover:text-[#C86D51] transition">
            {title}
          </h3>

          {/* Host Bilgisi */}
          <div className="flex items-center gap-2 mt-3">
            {hostAvatarUrl ? (
              <img src={hostAvatarUrl} alt={hostName} className="w-6 h-6 rounded-full object-cover" />
            ) : (
              <div className="w-6 h-6 rounded-full bg-[#8FAF8C]/20 text-[#1A432E] text-xs flex items-center justify-center font-bold">
                {hostName.charAt(0)}
              </div>
            )}
            <span className="text-xs text-[#63605D]">{hostName} ile buluşma</span>
          </div>
        </div>

        {/* Alt Kısım: Puan & Fiyat */}
        <div className="pt-4 mt-4 border-t border-[#EBE7DC] flex items-center justify-between">
          <div className="flex items-center gap-1 text-xs font-medium text-[#2C2A29]">
            <span className="text-[#E5A93C]">★</span>
            <span>{rating}</span>
            <span className="text-[#63605D]">({reviewCount})</span>
          </div>

          <div className="text-right">
            <span className="text-xs text-[#63605D] block">kişi başı</span>
            <span className="text-base font-semibold text-[#1A432E]">
              {price.toLocaleString('tr-TR')} TL
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};
