import React, { useState } from 'react';
import { HeroSearch } from './HeroSearch';
import { ExperienceCard } from './ExperienceCard';
import { HostOnboardingWizard } from './HostOnboardingWizard';
import { LORAKSCheckoutUyum } from './LORAKSCheckoutUyum';
import { SocialTemplateGenerator } from './SocialTemplateGenerator';

export const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'discover' | 'host' | 'social' | 'checkout'>('discover');

  const sampleExperiences = [
    {
      id: '1',
      title: 'Urla Bağlarında Doğal Şarap & Zeytinyağı Tadımı',
      category: 'sofra',
      location: 'Urla, İzmir',
      price: 1850,
      imageUrl: 'https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?auto=format&fit=crop&w=800&q=80',
      hostName: 'Zeynep Kaya',
      duration: '3 saat',
      badgeText: 'Özenle Seçilmiş Sofra'
    },
    {
      id: '2',
      title: 'Kadıköy Tarihi Moda Atölyesinde Çömlek & Seramik Deneyimi',
      category: 'zanaat',
      location: 'Kadıköy, İstanbul',
      price: 950,
      imageUrl: 'https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?auto=format&fit=crop&w=800&q=80',
      hostName: 'Murat Usta',
      duration: '2 saat',
      badgeText: 'Doğrudan Zanaat'
    },
    {
      id: '3',
      title: 'Kaz Dağları Göknar Ormanlarında Doğa Yürüyüşü & Ses Meditasyonu',
      category: 'doga',
      location: 'Edremit, Balıkesir',
      price: 2400,
      imageUrl: 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80',
      hostName: 'Deniz Akın',
      duration: '1 gün',
      badgeText: '🛡️ TÜRSAB Lisanslı Seyahat'
    }
  ];

  return (
    <div className="min-h-screen bg-[#FDFCF8] text-[#2C2A29] font-sans">
      {/* Üst Menü */}
      <header className="border-b border-[#EBE7DC] bg-[#FDFCF8]/90 backdrop-blur sticky top-0 z-50 px-6 py-4">
        <div className="max-w-6xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-3 cursor-pointer" onClick={() => setActiveTab('discover')}>
            <span className="font-serif text-2xl tracking-wide text-[#1A432E] font-bold">LORAKS</span>
            <span className="text-xs text-[#8FAF8C] hidden md:inline">| Kendine Zaman Tanı</span>
          </div>

          <nav className="flex items-center gap-3 text-xs md:text-sm font-medium">
            <button
              onClick={() => setActiveTab('discover')}
              className={`px-3 py-1.5 rounded-lg transition ${
                activeTab === 'discover' ? 'bg-[#1A432E] text-white' : 'text-[#63605D] hover:text-[#1A432E]'
              }`}
            >
              Keşfet
            </button>
            <button
              onClick={() => setActiveTab('host')}
              className={`px-3 py-1.5 rounded-lg transition ${
                activeTab === 'host' ? 'bg-[#1A432E] text-white' : 'text-[#63605D] hover:text-[#1A432E]'
              }`}
            >
              Ev Sahibi Ol (Host)
            </button>
            <button
              onClick={() => setActiveTab('social')}
              className={`px-3 py-1.5 rounded-lg transition ${
                activeTab === 'social' ? 'bg-[#1A432E] text-white' : 'text-[#63605D] hover:text-[#1A432E]'
              }`}
            >
              Sosyal Şablon Kiti
            </button>
            <button
              onClick={() => setActiveTab('checkout')}
              className={`px-3 py-1.5 rounded-lg transition ${
                activeTab === 'checkout' ? 'bg-[#1A432E] text-white' : 'text-[#63605D] hover:text-[#1A432E]'
              }`}
            >
              Örnek Rezervasyon (Demo)
            </button>
          </nav>
        </div>
      </header>

      {/* Sayfa İçeriği */}
      <main>
        {activeTab === 'discover' && (
          <div>
            <HeroSearch />
            <div className="max-w-6xl mx-auto px-6 py-12">
              <div className="flex items-center justify-between mb-8">
                <div>
                  <h2 className="font-serif text-2xl text-[#1A432E]">Öne Çıkan Buluşmalar</h2>
                  <p className="text-xs text-[#63605D] mt-1">Yerel ustaların, şeflerin ve rehberlerin hazırladığı seçkin deneyimler.</p>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {sampleExperiences.map((exp) => (
                  <ExperienceCard key={exp.id} {...exp} />
                ))}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'host' && (
          <div className="py-6">
            <HostOnboardingWizard />
          </div>
        )}

        {activeTab === 'social' && (
          <div className="py-10 px-4">
            <SocialTemplateGenerator
              experienceTitle="Urla Bağlarında Şef Sofrası & Doğal Şarap Tadımı"
              hostName="Şef Zeynep Kaya"
              category="Gastronomi"
              priceTry={2000}
              location="Urla, İzmir"
              pathwayCode="P0"
              tursabNo="16978"
              onDownload={(fmt) => alert(`${fmt.toUpperCase()} formatında DDS filigranlı şablon hazırlandı!`)}
            />
          </div>
        )}

        {activeTab === 'checkout' && (
          <div className="max-w-xl mx-auto py-10 px-4">
            <LORAKSCheckoutUyum
              listingTitle="Urla Bağlarında Doğal Şarap & Zeytinyağı Tadımı"
              listingPrice={1850}
              pathwayCode="P2"
              tursabAgencyName="LORAKS Seyahat Acentası"
              tursabLicenceNo="16978"
              onPaymentSuccess={(id) => alert(`Ödeme başarılı! Sipariş No: ${id}`)}
            />
          </div>
        )}
      </main>

      {/* Alt Bilgi */}
      <footer className="mt-20 border-t border-[#EBE7DC] py-8 text-center text-xs text-[#63605D]">
        <p>© 2026 LORAKS — Kendine Zaman Tanı. Tüm hakları saklıdır.</p>
        <p className="mt-1 text-[11px] text-[#8FAF8C]">TÜRSAB A Grubu Seyahat Acentesi Güvencesiyle</p>
      </footer>
    </div>
  );
};
