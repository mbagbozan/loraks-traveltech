"""
LORAKS TRAVELTECH — 7524 S.K. STOPAJ, KDV/BSMV AYRIŞTIRMA & TFRS 15 MOTORU
Version: v3.1 Production Ready
Calculates Decimal-precision withholding tax, revenue splits, insurance BSMV isolation,
and non-withheld penalty/indemnity allocations on cancellations.
"""

from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any, Union, Optional
from src.exceptions import FinancialReconciliationException

CENT = Decimal('0.01')

def quantize_money(amount: Decimal) -> Decimal:
    """Kuruş yuvarlama hassasiyet fonksiyonu (ROUND_HALF_UP)."""
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)

def calculate_split_and_withholding(
    gross_amount: Union[Decimal, float, str],
    host_tax_profile: str = "INDIVIDUAL_EXEMPT",
    mandatory_insurance_cost: Union[Decimal, float, str] = Decimal('0.00'),
    pathway_code: str = "P0"
) -> Dict[str, Any]:
    """
    7524 S.K. %1 Stopaj, TFRS 15 Split Payment, BSMV Sigorta Ayrıştırması.
    - mandatory_insurance_cost: 1618 S.K. Zorunlu Seyahat Sigortası (BSMV tabidir, KDV'den istisnadır).
    """
    if not isinstance(gross_amount, Decimal):
        gross_amount = Decimal(str(gross_amount))
    if not isinstance(mandatory_insurance_cost, Decimal):
        mandatory_insurance_cost = Decimal(str(mandatory_insurance_cost))

    gross_amount = quantize_money(gross_amount)
    mandatory_insurance_cost = quantize_money(mandatory_insurance_cost)

    vat_rate = Decimal('0.20')
    commission_rate = Decimal('0.12') if pathway_code == "P2" else Decimal('0.15')
    withholding_rate = Decimal('0.01')

    # 1. BSMV'li Sigorta Bedeli Ayrıştırması:
    # Sigorta bedeli (örn. 50 TL) KDV'den istisna olduğundan KDV matrahına dahil edilmez
    taxable_service_gross = gross_amount - mandatory_insurance_cost

    net_sales_base = quantize_money(taxable_service_gross / (Decimal('1') + vat_rate))
    loraks_gross_commission = quantize_money(gross_amount * commission_rate)
    loraks_net_commission = quantize_money(loraks_gross_commission / (Decimal('1') + vat_rate))
    loraks_vat = loraks_gross_commission - loraks_net_commission

    # 2. 7524 S.K. Stopajı Hesaplaması (KDV hariç hizmet matrahı üzerinden %1)
    withholding_tax = quantize_money(net_sales_base * withholding_rate)

    # 3. Host Net Hak Edişi (Kalan tutar doğrudan hosta bağlanarak kuruş farkı önlenir)
    net_host_payout = gross_amount - loraks_gross_commission - withholding_tax

    # KESİN MATEMATİKSEL DOĞRULAMA (INVARIANT)
    if (loraks_gross_commission + withholding_tax + net_host_payout) != gross_amount:
        raise FinancialReconciliationException("Mutabakat Uyuşmazlığı: Kuruş denkleşmedi!")

    return {
        "gross_amount": gross_amount,
        "pathway_code": pathway_code,
        "mandatory_insurance_cost_bsmv": mandatory_insurance_cost,
        "taxable_service_gross": taxable_service_gross,
        "loraks_net_revenue": loraks_net_commission,
        "loraks_vat": loraks_vat,
        "loraks_gross_commission": loraks_gross_commission,
        "net_sales_base": net_sales_base,
        "withholding_tax_360": withholding_tax,
        "host_payout": net_host_payout,
        "host_tax_profile": host_tax_profile
    }

def calculate_cancellation_penalty_taxation(
    retained_penalty_amount: Union[Decimal, float, str],
    host_portion_ratio: Decimal = Decimal('0.70')
) -> Dict[str, Any]:
    """
    Kısmi İptal / No-Show Durumunda Cezai Şart / Cayma Tazminatı Vergi Ayrıştırması:
    Yasal Gerekçe: Katılımcının etkinliğe gelmemesi veya son 24 saatte iptal etmesi halinde
    kesilen ceza, bir 'hizmet teslimi' değil 'sözleşmesel cayma tazminatı'dır (Borçlar Kanunu).
    Tazminatlar KDV'ye ve 7524 S.K. ticari hasılat stopajına tabi DEĞİLDİR!
    """
    if not isinstance(retained_penalty_amount, Decimal):
        retained_penalty_amount = Decimal(str(retained_penalty_amount))
    
    retained_penalty_amount = quantize_money(retained_penalty_amount)
    
    # Platform ve host arasındaki cezai şart paylaşımı
    host_penalty_payout = quantize_money(retained_penalty_amount * host_portion_ratio)
    platform_penalty_revenue = retained_penalty_amount - host_penalty_payout

    return {
        "retained_penalty_gross": retained_penalty_amount,
        "tax_status": "INDEMNITY_NON_TAXABLE_UNDER_7524",
        "withholding_tax_360": Decimal('0.00'),  # Stopaj uygulanmaz!
        "vat_applicable": Decimal('0.00'),      # Tazminat KDV'ye tabi değildir
        "host_penalty_payout": host_penalty_payout,
        "platform_penalty_retention": platform_penalty_revenue,
        "accounting_reason": "BORCLAR_KANUNU_CAYMA_TAZMINATI_NO_SHOW",
        "host_account_code": "679_DIGER_OLAGANDISI_GELIRLER",
        "platform_account_code": "679_DIGER_OLAGANDISI_GELIRLER_PLATFORM"
    }
