import React, { useState } from 'react';

export interface LORAKSCheckoutProps {
  grossAmount: number;
  pathwayCode: 'P0' | 'P1' | 'P2' | 'P3' | 'P4';
  tursabBelgeNo: string;
  acenteUnvani: string;
  onPaymentSubmit: () => void;
  isLoading?: boolean;
}

export const LORAKSCheckoutUyum: React.FC<LORAKSCheckoutProps> = ({
  grossAmount,
  pathwayCode,
  tursabBelgeNo,
  acenteUnvani,
  onPaymentSubmit,
  isLoading = false
}) => {
  const [mssApproved, setMssApproved] = useState(false);
  const [ptsApproved, setPtsApproved] = useState(false);

  const isP2Travel = pathwayCode === 'P2';
  // If P2 travel, both MSS and PTS are legally required. If P0/P1, only MSS is required.
  const isFormValid = isP2Travel ? (mssApproved && ptsApproved) : mssApproved;

  return (
    <div style={{
      maxWidth: '640px',
      margin: '0 auto',
      padding: '24px',
      backgroundColor: '#FDFCF8',
      border: '1px solid #E5E7EB',
      borderRadius: '16px',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      boxShadow: '0 4px 20px rgba(0, 0, 0, 0.05)',
      color: '#1F2937'
    }}>
      {/* Brand Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '20px', borderBottom: '1px solid #E5E7EB', paddingBottom: '16px' }}>
        <div>
          <h2 style={{ margin: 0, fontSize: '20px', fontWeight: 700, color: '#1A432E' }}>LORAKS Güvenceli Rezervasyon</h2>
          <p style={{ margin: '4px 0 0', fontSize: '13px', color: '#6B7280' }}>Modern Anadolu Ev Sahipliği ve Yasal Tüketici Kalkanı</p>
        </div>
        <div style={{
          backgroundColor: '#ECFDF5',
          border: '1px solid #10B981',
          padding: '6px 12px',
          borderRadius: '9999px',
          fontSize: '12px',
          fontWeight: 600,
          color: '#065F46'
        }}>
          Pathway: {pathwayCode}
        </div>
      </div>

      {/* TÜRSAB DDS Badge (Only for P2 Licensed Travel or Platform Verification) */}
      <div style={{
        backgroundColor: '#FFFFFF',
        border: '1px solid #D1D5DB',
        borderRadius: '12px',
        padding: '16px',
        marginBottom: '20px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between'
      }}>
        <div style={{ flex: 1, paddingRight: '16px' }}>
          <div style={{ fontSize: '11px', textTransform: 'uppercase', letterSpacing: '0.05em', color: '#6B7280', fontWeight: 600 }}>
            T.C. Kültür ve Turizm Bakanlığı Denetimi
          </div>
          <div style={{ fontSize: '14px', fontWeight: 600, color: '#111827', marginTop: '2px' }}>
            {acenteUnvani}
          </div>
          <div style={{ fontSize: '12px', color: '#4B5563', marginTop: '2px' }}>
            {isP2Travel 
              ? 'Seyahat ve tur operasyonu TÜRSAB A Grubu lisansı güvencesiyle icra edilmektedir.'
              : 'Atölye ve deneyim sağlayıcı kimliği LORAKS platformu tarafından doğrulanmıştır.'}
          </div>
        </div>
        <div style={{
          backgroundColor: '#1A432E',
          color: '#FFFFFF',
          padding: '10px 14px',
          borderRadius: '8px',
          textAlign: 'center',
          minWidth: '90px'
        }}>
          <div style={{ fontSize: '10px', fontWeight: 700, letterSpacing: '0.1em' }}>TÜRSAB</div>
          <div style={{ fontSize: '15px', fontWeight: 800 }}>{tursabBelgeNo}</div>
        </div>
      </div>

      {/* Mandatory Insurance Notice (For P2) */}
      {isP2Travel && (
        <div style={{
          backgroundColor: '#FEF3C7',
          border: '1px solid #F59E0B',
          borderRadius: '10px',
          padding: '12px 14px',
          marginBottom: '20px',
          fontSize: '12px',
          color: '#92400E',
          display: 'flex',
          alignItems: 'flex-start',
          gap: '8px'
        }}>
          <span style={{ fontSize: '16px' }}>🛡️</span>
          <div>
            <strong>1618 Sayılı Kanun Gereği Zorunlu Sigorta:</strong> Bu deneyim için adınıza 
            <em> Zorunlu Paket Tur (Mesleki Sorumluluk) Sigortası</em> poliçesi düzenlenecektir. Poliçeniz ödeme sonrası e-posta adresinize iletilir.
          </div>
        </div>
      )}

      {/* Amount Summary */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '14px 18px',
        backgroundColor: '#F3F4F6',
        borderRadius: '10px',
        marginBottom: '20px'
      }}>
        <span style={{ fontSize: '14px', fontWeight: 500, color: '#374151' }}>Ödenecek Toplam Tutar:</span>
        <span style={{ fontSize: '20px', fontWeight: 800, color: '#1A432E' }}>
          {grossAmount.toLocaleString('tr-TR', { minimumFractionDigits: 2 })} TL
        </span>
      </div>

      {/* Compliance Checkboxes */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '24px' }}>
        <label style={{ display: 'flex', alignItems: 'flex-start', gap: '10px', cursor: 'pointer', fontSize: '13px', color: '#4B5563' }}>
          <input
            type="checkbox"
            checked={mssApproved}
            onChange={(e) => setMssApproved(e.target.checked)}
            style={{ marginTop: '2px', accentColor: '#1A432E' }}
          />
          <span>
            <a href="/legal/distance-sales" target="_blank" rel="noreferrer" style={{ color: '#1A432E', fontWeight: 600, textDecoration: 'underline' }}>
              Mesafeli Satış Sözleşmesi
            </a>'ni ve İptal/İade Şartlarını okudum, onaylıyorum. (Mesafeli Sözleşmeler Yön. m. 15/1-g uyarınca belirli tarihli etkinliklerde cayma hakkı istisnasını kabul ediyorum).
          </span>
        </label>

        {isP2Travel && (
          <label style={{ display: 'flex', alignItems: 'flex-start', gap: '10px', cursor: 'pointer', fontSize: '13px', color: '#4B5563' }}>
            <input
              type="checkbox"
              checked={ptsApproved}
              onChange={(e) => setPtsApproved(e.target.checked)}
              style={{ marginTop: '2px', accentColor: '#1A432E' }}
            />
            <span>
              <a href="/legal/package-tour" target="_blank" rel="noreferrer" style={{ color: '#1A432E', fontWeight: 600, textDecoration: 'underline' }}>
                Paket Tur Sözleşmesi
              </a> şartlarını ve {acenteUnvani} acentesinin yasal sorumluluk kapsamını kabul ediyorum.
            </span>
          </label>
        )}
      </div>

      {/* Submit Button */}
      <button
        onClick={onPaymentSubmit}
        disabled={!isFormValid || isLoading}
        style={{
          width: '100%',
          padding: '14px',
          backgroundColor: isFormValid && !isLoading ? '#1A432E' : '#9CA3AF',
          color: '#FFFFFF',
          border: 'none',
          borderRadius: '10px',
          fontSize: '15px',
          fontWeight: 700,
          cursor: isFormValid && !isLoading ? 'pointer' : 'not-allowed',
          transition: 'background-color 0.2s ease',
          boxShadow: isFormValid ? '0 4px 12px rgba(26, 67, 46, 0.3)' : 'none'
        }}
      >
        {isLoading ? 'İşleminiz Gerçekleştiriliyor...' : `Güvenle Öde (${grossAmount.toLocaleString('tr-TR', { minimumFractionDigits: 2 })} TL)`}
      </button>

      {/* PCI DSS Footnote */}
      <div style={{ textAlign: 'center', marginTop: '14px', fontSize: '11px', color: '#9CA3AF' }}>
        🔒 256-Bit SSL Şifreleme · PCI DSS Seviye 1 Uyumlu Lisanslı Ödeme Altyapısı · TCMB Güvenli Havuz
      </div>
    </div>
  );
};
