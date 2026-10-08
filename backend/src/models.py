# src/models.py
"""
LORAKS Core Data Models (Dataclasses)
Sistemin tüm veri yapıları, tipleri ve durum makineleri.
"""
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional, List, Dict, Any

class PathwayCode(str, Enum):
    P0 = "P0"  # Sabit Mekan Atölye / Gastronomi / Zanaat (Acente gerekmez)
    P1 = "P1"  # Mekan Destekli Sosyal Deneyim / Salon Etkinliği
    P2 = "P2"  # Paket Tur / Doğa / Seyahat / Transfer / Rehberli Gezi (A Grubu Acente Zorunlu)
    P3 = "P3"  # B2B Kurumsal Offsite / Şirket İnzivası
    P4 = "P4"  # Kapalı Devre / Özel Davetli Topluluk

class MerchantEntity(str, Enum):
    TEKNOLOJI_AS = "LORAKS_TEKNOLOJI_AS"
    ACENTA_AS = "LORAKS_ACENTA_AS"

class HostTaxProfile(str, Enum):
    INDIVIDUAL_EXEMPT = "INDIVIDUAL_EXEMPT"          # GVK Madde 9 Esnaf Muaflığı (Vergisiz/Deftersiz)
    INDIVIDUAL_NON_EXEMPT = "INDIVIDUAL_NON_EXEMPT"  # Vergi mükellefi olmayan (Gider Pusulası)
    YOUNG_ENTREPRENEUR = "YOUNG_ENTREPRENEUR"        # GVK Mük. 20 Genç Girişimci İstisnası
    CORPORATE = "CORPORATE"                          # Şahıs Şirketi / Ltd / A.Ş. (e-Fatura Mükellefi)

class BookingStatus(str, Enum):
    PENDING_PAYMENT = "PENDING_PAYMENT"
    IN_ESCROW = "IN_ESCROW"                          # Para havuzda, etkinlik bekleniyor (Zero-Tax)
    CHECKED_IN = "CHECKED_IN"                        # QR okutuldu, hizmet ifa edildi (Vergi Tetiklendi)
    SETTLED = "SETTLED"                              # Hak ediş ödendi, e-arşiv/e-fatura kesildi
    CANCELLED_PRE_CHECKIN = "CANCELLED_PRE_CHECKIN"  # Sıfır vergi iadesi
    CANCELLED_POST_CHECKIN = "CANCELLED_POST_CHECKIN"# Düzeltme beyannamesi gerektiren iade

@dataclass
class Listing:
    id: str
    host_id: str
    title: str
    description: str
    gross_price: Decimal
    has_transport: bool = False
    has_accommodation: bool = False
    is_multi_day: bool = False
    has_guided_tour: bool = False  # TUREB 6326 S.K.
    venue_address: Optional[str] = None
    capacity: int = 10
    pathway_code: Optional[PathwayCode] = None
    is_approved: bool = False
    compliance_flags: List[str] = field(default_factory=list)

@dataclass
class HostProfile:
    id: str
    full_name: str
    tax_profile: HostTaxProfile
    tc_or_vkn: str
    iban: str
    has_esnaf_muafiyeti_doc: bool = False
    is_young_entrepreneur: bool = False

@dataclass
class BookingTransaction:
    booking_id: str
    listing_id: str
    guest_id: str
    gross_amount: Decimal
    pathway_code: PathwayCode
    merchant_entity: MerchantEntity
    pos_commission_rate: Decimal = Decimal('0.028')  # %2,8 POS komisyon oranı
    status: BookingStatus = BookingStatus.PENDING_PAYMENT
    pos_fee_amount: Decimal = Decimal('0.00')
    ledger_records: List[Dict[str, Any]] = field(default_factory=list)

    def record_ledger_entry(self, account_code: str, amount: Decimal, company: str):
        self.ledger_records.append({
            "account_code": account_code,
            "amount": amount,
            "company": company
        })
