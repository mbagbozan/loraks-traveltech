# src/pathway_engine.py
from src.exceptions import ComplianceViolationException

class PathwayEngine:
    def determine_payment_gateway(self, listing_details: dict) -> dict:
        """
        1618 Sayılı TÜRSAB ve 6326 Sayılı TUREB Uyumlu Otomatik POS Yönlendirme Motoru
        """
        has_transport = listing_details.get('has_transport', False)
        has_accommodation = listing_details.get('has_accommodation', False)
        is_multi_day = listing_details.get('is_multi_day', False)
        has_guided_tour = listing_details.get('has_guided_tour', False)  # TUREB 6326 S.K. Rehberlik Tetikleyicisi

        # Eğer ulaşım, konaklama, rehberlik veya çok günlük seyahat varsa OTOMATİK P2'DİR
        if has_transport or has_accommodation or is_multi_day or has_guided_tour:
            listing_details['pathway_code'] = 'P2'
            
            # SERT YAZILIM KİLİDİ: P2 İşleminde Teknoloji POS'u ÇAĞRILAMAZ!
            gateway_config = {
                "merchant_id": "ACENTA_IYZICO_MERCHANT_ID",
                "contract_type": "PACKAGE_TOUR_CONTRACT_PTS",
                "seller_title": "LORAKS SEYAHAT ACENTASI A.Ş.",
                "tursab_licence_no": "2387",
                "mandatory_insurance_required": True
            }
            return gateway_config
            
        else:
            listing_details['pathway_code'] = 'P0'
            gateway_config = {
                "merchant_id": "TEKNOLOJI_IYZICO_MERCHANT_ID",
                "contract_type": "MARKETPLACE_USER_AGREEMENT",
                "seller_title": "LORAKS TEKNOLOJİ A.Ş.",
                "mandatory_insurance_required": False
            }
            return gateway_config
