"""
LORAKS TRAVELTECH — INTERCOMPANY BILLING & ARMS-LENGTH SERVICE ENGINE
Compliant with: 5520 Sayılı KVK m. 13 (Transfer Fiyatlandırması ve Emsallere Uygunluk İlkesi)

Yasal Gerekçe:
LORAKS Teknoloji A.Ş., AWS sunucularını, SMS/e-posta altyapısını, yazılım bakımını ve 
müşteri destek ekibini barındırır. Kardeş şirket olan LORAKS Seyahat Acentası A.Ş.'ye (P2)
bu hizmetleri bedelsiz veremez. Her ay emsal maliyet + kâr marjı (%10-15 cost-plus) veya
P2 GMV hacmi üzerinden hesaplanan bir 'Yazılım ve Yönetim Hizmet Bedeli Faturası' düzenlemek zorundadır.
"""

from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any
from src.exceptions import ComplianceViolationException

CENT = Decimal('0.01')

def quantize_money(amount: Decimal) -> Decimal:
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)

class IntercompanyBillingEngine:
    """
    KVK m. 13 Uyumlu Şirketler Arası Hizmet ve Teknoloji Faturalandırma Motoru
    """
    STANDARD_MARKUP = Decimal('0.10')  # %10 Maliyet Artı (Cost-Plus) Yöntemi
    P2_TECH_FEE_RATE = Decimal('0.05') # Veya P2 brüt işlem hacmi üzerinden %5 teknoloji lisans bedeli

    @classmethod
    def calculate_monthly_intercompany_invoice(
        cls,
        p2_gross_turnover: Decimal,
        allocated_shared_costs: Decimal,
        method: str = "COST_PLUS"
    ) -> Dict[str, Any]:
        """
        Acente A.Ş.'ye kesilecek aylık fatura matrahını ve %20 KDV'sini hesaplar.
        """
        if not isinstance(p2_gross_turnover, Decimal):
            p2_gross_turnover = Decimal(str(p2_gross_turnover))
        if not isinstance(allocated_shared_costs, Decimal):
            allocated_shared_costs = Decimal(str(allocated_shared_costs))

        p2_gross_turnover = quantize_money(p2_gross_turnover)
        allocated_shared_costs = quantize_money(allocated_shared_costs)

        # SERT KISIT: Bedelsiz hizmet aktarımı KVK m. 13 uyarınca kanunen yasaktır!
        if p2_gross_turnover > Decimal('0.00') and allocated_shared_costs == Decimal('0.00') and method == "COST_PLUS":
            raise ComplianceViolationException(
                "KVK m.13 İhlali: Teknoloji A.Ş., Acente A.Ş.'ye bedelsiz altyapı sağlayamaz! Masraf paylaşımı zorunludur."
            )

        vat_rate = Decimal('0.20')

        if method == "COST_PLUS":
            # Paylaşılan sunucu/personel maliyeti + %10 emsal kâr marjı
            base_amount = quantize_money(allocated_shared_costs * (Decimal('1') + cls.STANDARD_MARKUP))
        elif method == "TURNOVER_ROYALTY":
            # P2 cirosu üzerinden %5 yazılım kullanım bedeli
            base_amount = quantize_money(p2_gross_turnover * cls.P2_TECH_FEE_RATE)
        else:
            raise ValueError(f"Geçersiz transfer fiyatlandırması yöntemi: {method}")

        kdv_amount = quantize_money(base_amount * vat_rate)
        total_invoice = base_amount + kdv_amount

        return {
            "issuer": "LORAKS TEKNOLOJİ ANONİM ŞİRKETİ",
            "recipient": "LORAKS SEYAHAT ACENTASI ANONİM ŞİRKETİ",
            "invoice_type": "B2B_E_FATURA_YONETIM_VE_YAZILIM_BEDELI",
            "transfer_pricing_method": method,
            "allocated_shared_costs": allocated_shared_costs,
            "base_amount_net": base_amount,
            "vat_rate": vat_rate,
            "vat_amount": kdv_amount,
            "total_invoice_amount": total_invoice,
            "accounting_entries": {
                "teknoloji_as": {
                    "credit_account": "600_YURTICI_SATISLAR_YAZILIM",
                    "credit_vat_account": "391_HESAPLANAN_KDV",
                    "debit_account": "120_ALICILAR_ACENTA_AS"
                },
                "acenta_as": {
                    "debit_account": "770_GENEL_YONETIM_GIDERLERI_YAZILIM",
                    "debit_vat_account": "191_INDIRILECEK_KDV",
                    "credit_account": "320_SATICILAR_TEKNOLOJI_AS"
                }
            }
        }
