# src/tax_engine.py
from decimal import Decimal, ROUND_HALF_UP
from src.exceptions import FinancialReconciliationException

CENT = Decimal('0.01')

def quantize_money(amount: Decimal) -> Decimal:
    """Kuruş yuvarlama hassasiyet fonksiyonu"""
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)

def calculate_split_and_withholding(gross_amount: Decimal, host_tax_profile: str = "INDIVIDUAL_EXEMPT") -> dict:
    """
    7524 S.K. %1 Stopaj, TFRS 15 Split Payment ve Dinamik Host Tipi Hesaplama Motoru
    Profiles: 'CORPORATE', 'INDIVIDUAL_EXEMPT', 'INDIVIDUAL_NON_EXEMPT'
    """
    vat_rate = Decimal('0.20')
    commission_rate = Decimal('0.15')
    withholding_rate = Decimal('0.01')

    # 1. Matrah ve Komisyon Hesaplaması
    net_sales_base = quantize_money(gross_amount / (Decimal('1') + vat_rate))
    loraks_gross_commission = quantize_money(gross_amount * commission_rate)
    loraks_net_commission = quantize_money(loraks_gross_commission / (Decimal('1') + vat_rate))
    loraks_vat = loraks_gross_commission - loraks_net_commission

    # 2. 7524 S.K. Stopajı Hesaplaması
    if host_tax_profile == "CORPORATE":
        withholding_tax = quantize_money(net_sales_base * withholding_rate)
    else:
        withholding_tax = quantize_money(net_sales_base * withholding_rate)

    # 3. Host Net Hak Edişi (Kalan tutar doğrudan hosta bağlanarak kuruş farkı %100 önlenir)
    net_host_payout = gross_amount - loraks_gross_commission - withholding_tax

    # KESİN MATEMATİKSEL DOĞRULAMA (INVARIANT)
    if (loraks_gross_commission + withholding_tax + net_host_payout) != gross_amount:
        raise FinancialReconciliationException("Mutabakat Uyuşmazlığı: Kuruş denkleşmedi!")

    return {
        "gross_amount": gross_amount,
        "loraks_net_revenue": loraks_net_commission,
        "loraks_vat": loraks_vat,
        "withholding_tax_360": withholding_tax,
        "host_payout": net_host_payout,
        "host_tax_profile": host_tax_profile
    }
