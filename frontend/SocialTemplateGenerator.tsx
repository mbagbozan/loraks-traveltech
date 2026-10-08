import React, { useState } from 'react';
import { PathwayCode } from './types';

export interface SocialTemplateProps {
  experienceTitle: string;
  hostName: string;
  category: string;
  priceTry: number;
  location: string;
  pathwayCode: PathwayCode;
  tursabNo?: string;
  imageUrl?: string;
  onDownload?: (format: 'story' | 'post') => void;
}

export const SocialTemplateGenerator: React.FC<SocialTemplateProps> = ({
  experienceTitle = 'Urla Bağlarında Şef Sofrası & Tadım',
  hostName = 'Şef Ayşe Demir',
  category = 'Gastronomi',
  priceTry = 2000,
  location = 'Urla, İzmir',
  pathwayCode = 'P0',
  tursabNo = '16978',
  imageUrl = 'https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?auto=format&fit=crop&w=1200&q=80',
  onDownload
}) => {
  const [format, setFormat] = useState<'story' | 'post'>('story');
  const isP2Travel = pathwayCode === 'P2';

  const isStory = format === 'story';
  const containerWidth = isStory ? '340px' : '380px';
  const containerHeight = isStory ? '600px' : '380px';

  return (
    <div style={{
      maxWidth: '780px',
      margin: '0 auto',
      padding: '28px',
      backgroundColor: '#FDFCF8',
      borderRadius: '20px',
      border: '1px solid #E5E7EB',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      boxShadow: '0 8px 30px rgba(0, 0, 0, 0.04)'
    }}>
      {/* Header Info */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '20px' }}>
        <div>
          <span style={{
            fontSize: '11px',
            fontWeight: 700,
            letterSpacing: '1px',
            textTransform: 'uppercase',
            color: '#C86D51',
            backgroundColor: '#FDF0ED',
            padding: '4px 10px',
            borderRadius: '100px',
            display: 'inline-block',
            marginBottom: '8px'
          }}>
            Muvazaa Kalkanı & Hazır Promosyon Kiti
          </span>
          <h2 style={{ fontSize: '22px', fontWeight: 800, color: '#1A432E', margin: '4px 0 6px' }}>
            Sosyal Medya Tanıtım Görseli
          </h2>
          <p style={{ fontSize: '13px', color: '#6B7280', margin: 0 }}>
            İlanınız onaylandı! Instagram'da paylaşırken yasal koruma sağlayan resmi TÜRSAB DDS logolu şablonu indirin.
          </p>
        </div>

        {/* Format Selector */}
        <div style={{
          display: 'flex',
          backgroundColor: '#F3F4F6',
          borderRadius: '10px',
          padding: '4px',
          gap: '4px'
        }}>
          <button
            onClick={() => setFormat('story')}
            style={{
              padding: '6px 14px',
              fontSize: '12px',
              fontWeight: 600,
              borderRadius: '8px',
              border: 'none',
              cursor: 'pointer',
              backgroundColor: isStory ? '#1A432E' : 'transparent',
              color: isStory ? '#FFFFFF' : '#4B5563',
              transition: 'all 0.2s'
            }}
          >
            Story (9:16)
          </button>
          <button
            onClick={() => setFormat('post')}
            style={{
              padding: '6px 14px',
              fontSize: '12px',
              fontWeight: 600,
              borderRadius: '8px',
              border: 'none',
              cursor: 'pointer',
              backgroundColor: !isStory ? '#1A432E' : 'transparent',
              color: !isStory ? '#FFFFFF' : '#4B5563',
              transition: 'all 0.2s'
            }}
          >
            Post (1:1)
          </button>
        </div>
      </div>

      {/* Visual Canvas Container */}
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '24px',
        backgroundColor: '#F3F4F6',
        borderRadius: '16px',
        marginBottom: '20px'
      }}>
        {/* The Card Template */}
        <div style={{
          width: containerWidth,
          height: containerHeight,
          position: 'relative',
          borderRadius: '16px',
          overflow: 'hidden',
          boxShadow: '0 12px 36px rgba(0,0,0,0.15)',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          backgroundImage: `linear-gradient(to bottom, rgba(26,67,46,0.3) 0%, rgba(26,67,46,0.85) 100%), url(${imageUrl})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          color: '#FFFFFF'
        }}>
          {/* Top Brand Bar */}
          <div style={{
            padding: '16px 20px',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <div style={{
                fontSize: '16px',
                fontWeight: 900,
                letterSpacing: '1.5px',
                color: '#FDFCF8'
              }}>
                LORAKS
              </div>
              <span style={{ fontSize: '10px', opacity: 0.8, color: '#FDFCF8' }}>· Deneyim</span>
            </div>
            <div style={{
              backgroundColor: 'rgba(253, 252, 248, 0.2)',
              backdropFilter: 'blur(8px)',
              padding: '4px 10px',
              borderRadius: '100px',
              fontSize: '10px',
              fontWeight: 600,
              color: '#FDFCF8'
            }}>
              {category}
            </div>
          </div>

          {/* Center Details */}
          <div style={{ padding: '0 20px', marginBottom: isStory ? '20px' : '10px' }}>
            <span style={{
              fontSize: '11px',
              fontWeight: 600,
              color: '#E5A93C',
              display: 'block',
              marginBottom: '4px'
            }}>
              📍 {location} · {hostName}
            </span>
            <h3 style={{
              fontSize: isStory ? '22px' : '18px',
              fontWeight: 800,
              lineHeight: 1.25,
              margin: '0 0 10px',
              textShadow: '0 2px 4px rgba(0,0,0,0.3)'
            }}>
              {experienceTitle}
            </h3>
            <div style={{
              display: 'inline-block',
              backgroundColor: 'rgba(253, 252, 248, 0.95)',
              color: '#1A432E',
              padding: '4px 12px',
              borderRadius: '8px',
              fontSize: '14px',
              fontWeight: 800
            }}>
              {priceTry.toLocaleString('tr-TR')} ₺ / kişi
            </div>
          </div>

          {/* Bottom Unremovable Legal Shield Bar */}
          <div style={{
            backgroundColor: '#1A432E',
            padding: '12px 16px',
            borderTop: '2px solid #8FAF8C',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: '12px'
          }}>
            {/* Left QR Code Mock */}
            <div style={{
              width: '48px',
              height: '48px',
              backgroundColor: '#FFFFFF',
              borderRadius: '6px',
              padding: '3px',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              flexShrink: 0
            }}>
              {/* QR Pattern Representation */}
              <div style={{
                width: '100%',
                height: '100%',
                background: 'repeating-linear-gradient(0deg, #1A432E, #1A432E 3px, #fff 3px, #fff 6px)',
                borderRadius: '3px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
              }}>
                <span style={{ fontSize: '7px', fontWeight: 900, color: '#1A432E', backgroundColor: '#fff', padding: '1px 2px' }}>DDS</span>
              </div>
            </div>

            {/* Right Legal Disclaimer */}
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ fontSize: '10px', fontWeight: 700, color: '#FDFCF8', marginBottom: '2px' }}>
                {isP2Travel 
                  ? `TÜRSAB Lisanslı Seyahat Acentesi Güvencesiyle (No: ${tursabNo})`
                  : `LORAKS Doğrulanmış Bağımsız Atölye Güvencesiyle`}
              </div>
              <div style={{ fontSize: '8.5px', color: '#8FAF8C', lineHeight: 1.2 }}>
                Güvenli ödeme, sigorta ve resmi rezervasyon için QR kodu okutun veya loraks.com üzerinden kayıt olun.
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Value Note & Download Action */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '16px 20px',
        backgroundColor: '#F7F5F0',
        borderRadius: '12px',
        border: '1px solid #E5E7EB'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <span style={{ fontSize: '24px' }}>🛡️</span>
          <div>
            <div style={{ fontSize: '13px', fontWeight: 700, color: '#1A432E' }}>
              Muvazaa ve Belgesiz Tur Riskini Sıfırlar
            </div>
            <div style={{ fontSize: '12px', color: '#6B7280' }}>
              Resmi TÜRSAB DDS filigranı sayesinde sosyal medyadaki paylaşımlarınız yasal güvenceye kavuşur.
            </div>
          </div>
        </div>

        <button
          onClick={() => onDownload && onDownload(format)}
          style={{
            backgroundColor: '#1A432E',
            color: '#FFFFFF',
            border: 'none',
            padding: '10px 20px',
            borderRadius: '10px',
            fontSize: '13px',
            fontWeight: 700,
            cursor: 'pointer',
            boxShadow: '0 4px 12px rgba(26,67,46,0.2)',
            display: 'flex',
            alignItems: 'center',
            gap: '8px'
          }}
        >
          <span>📥</span>
          <span>Görseli İndir ({isStory ? 'Story' : 'Post'})</span>
        </button>
      </div>
    </div>
  );
};
export default SocialTemplateGenerator;
