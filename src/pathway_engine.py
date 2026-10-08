"""
LORAKS TRAVELTECH — CREATOR ENABLEMENT & COMPLIANCE PATHWAY ENGINE
Version: 3.0.0-ENABLEMENT (Macroeconomic Compliance & Creator Journey Core)
"""

from typing import Dict, Any, List
import datetime

class PathwayEngine:
    RULE_VERSION = "v3.0-CREATOR-ENABLEMENT"

    @classmethod
    def classify(cls, listing: Dict[str, Any]) -> Dict[str, Any]:
        """
        Classifies an experience listing into a Creator Enablement Journey:
        - P0 (DIRECT_CRAFT): Single fixed-venue workshop, studio, kitchen or craft.
        - P1 (VERIFIED_EXCELLENCE): Food hygiene, certified tour guide or instructor badge.
        - P2 (REGULATED_JOURNEY): Travel, transport, overnight or multi-day package protected by Agency Shield.
        - P3 (GROWTH_MENTORING): Host missing a document; guided with 1-day business plan and fast-track options.
        - P4 (REQUIRES_LICENSING_ASSISTANCE): Personal transport identified; solved via D2 transport partners and Agency Shield.
        """
        transport_arranged = listing.get("transport_arranged", "none")
        transport_operator = listing.get("transport_operator", "none")
        accommodation_included = listing.get("accommodation_included", False)
        overnight = listing.get("overnight", False)
        services_bundled = listing.get("services_bundled", [])
        single_inclusive_price = listing.get("single_inclusive_price", True)
        category = listing.get("category", "workshop")
        alcohol_served = listing.get("alcohol_served", False)
        heritage_site = listing.get("heritage_or_protected_site", False)
        participant_count = listing.get("participant_count", 10)
        has_guide_license = listing.get("has_tourist_guide_license", False)
        has_hygiene_cert = listing.get("has_hygiene_cert", False)
        has_instructor_cert = listing.get("has_instructor_cert", False)

        reasons = []
        remediation_steps = []

        # =====================================================================
        # 1. P4 — REQUIRES LICENSING ASSISTANCE (Formerly Prohibited)
        # =====================================================================
        if transport_operator == "organiser_own_vehicle" and transport_arranged in ["included_in_price", "optional"]:
            reasons.append("Şahsi araçla ticari transfer yerine lisanslı D2 araç desteği ile güvenli rota açılmaktadır.")
            return {
                "pathway_code": "P4",
                "name": "REQUIRES_LICENSING_ASSISTANCE",
                "contracting_party": "NONE",
                "can_publish": False,
                "reasons": reasons,
                "remediation_steps": ["Ulaşım adımı LORAKS anlaşmalı D2 lisanslı taşıyıcı ağına devredilebilir."],
                "fast_track_options": [
                    {
                        "option_name": "P0_FAST_TRACK",
                        "title": "Ulaşımı Hariç Tutarak Hemen Bugün Satışa Aç (0 Gün Bekleme)",
                        "description": "Misafirlerin buluşma noktasına kendi imkanlarıyla gelmesini sağlayarak atölyenizi anında P0 Doğrudan Zanaat olarak yayınlayabilirsiniz."
                    },
                    {
                        "option_name": "P2_AGENCY_SHIELD",
                        "title": "LORAKS Acente Zırhı ve D2 Araç Desteğiyle Tam Pakete Dönüştür",
                        "description": "Ulaşımı LORAKS D2 lisanslı araçlarımız ve TÜRSAB sigorta şemsiyemizle çözelim; siz 'Konuk Eğitmen' olarak sıfır riskle kazanın."
                    }
                ],
                "badge": "🤝 Lisans & Ulaşım Desteğiyle Hazır",
                "commission_rate": 0.0,
                "requires_insurance": False,
                "rule_version": cls.RULE_VERSION,
                "timestamp": datetime.datetime.utcnow().isoformat()
            }

        # =====================================================================
        # 2. P2 — REGULATED JOURNEY (Agency Umbrella & Compulsory Insurance)
        # =====================================================================
        is_travel_territory = False
        if transport_arranged in ["included_in_price", "optional"]:
            is_travel_territory = True
            reasons.append("Deneyim lisanslı ulaşım/transfer hizmeti içermektedir.")
        
        if accommodation_included or overnight:
            is_travel_territory = True
            reasons.append("Deneyim konaklama veya geceleme içermektedir.")

        tourist_services = {"guide", "transport", "accommodation", "tour"}
        bundled_count = len([s for s in services_bundled if s in tourist_services])
        if bundled_count >= 2 and single_inclusive_price:
            is_travel_territory = True
            reasons.append(f"Birden fazla turistik hizmet ({bundled_count} adet) paket tur kapsamında birleştirilmiştir.")

        if is_travel_territory:
            return {
                "pathway_code": "P2",
                "name": "REGULATED_JOURNEY",
                "contracting_party": "LICENSED_TRAVEL_AGENCY",
                "seller_of_record": "LORAKS ORGANİZASYON DANIŞMANLIK HİZMETLERİ A.Ş. (TÜRSAB No: 16978)",
                "can_publish": True,
                "reasons": reasons,
                "remediation_steps": [
                    "Etkinlik LORAKS Seyahat Acentası yasal kalkanı altına alınmıştır.",
                    "Her katılımcı adına otomatik Zorunlu Paket Tur Sigortası düzenlenir.",
                    "Host ile 'Konuk Eğitmen Sözleşmesi' imzalanarak yasal koruma sağlanır."
                ],
                "badge": "🛡️ TÜRSAB No: 16978 LORAKS Seyahat Acentesi Güvencesiyle",
                "commission_rate": 0.12,
                "requires_insurance": True,
                "invoice_type": "AGENCY_B2C_PACKAGE_TOUR",
                "rule_version": cls.RULE_VERSION,
                "timestamp": datetime.datetime.utcnow().isoformat()
            }

        # =====================================================================
        # 3. P1 / P3 — CREDENTIAL-GATED OR GROWTH MENTORING PATHWAYS
        # =====================================================================
        needs_credentials = False
        if heritage_site and not has_guide_license:
            reasons.append("Tarihi/ören yeri gezisi Kültür ve Turizm Bakanlığı kokartlı Turist Rehberi ile zenginleştirilmelidir.")
            remediation_steps.append("Platform içi Bakanlık kokartlı bir rehber üyemizle ücretsiz eşleşebilirsiniz.")
            needs_credentials = True

        if category == "food" or alcohol_served:
            if not has_hygiene_cert:
                reasons.append("Gıda veya tadım etkinliklerinde Hijyen Belgesi ile satış fiyatı ve güven artırılabilir.")
                remediation_steps.append("İlçe Halk Eğitim'den 1 günde online Hijyen Belgesi alarak Onaylı Mutfak rozeti kazanabilirsiniz.")
                needs_credentials = True

        if category in ["outdoor", "retreat"] and not has_instructor_cert:
            reasons.append("Doğa ve esenlik aktivitelerinde uzmanlık / ilk yardım teyidi tavsiye edilir.")
            remediation_steps.append("İlk Yardım veya uzmanlık belgenizi ekleyerek 'Onaylı Eğitmen' rozetine geçebilirsiniz.")
            needs_credentials = True

        if needs_credentials:
            # P3 Growth Mentoring (Creator Enablement: "Biz polis değil, kuluçkayız")
            return {
                "pathway_code": "P3",
                "name": "GROWTH_MENTORING",
                "contracting_party": "PENDING_VERIFICATION",
                "can_publish": False,
                "guidance_mode": True,
                "reasons": reasons,
                "remediation_steps": remediation_steps,
                "guidance_incubator": {
                    "philosophy": "Biz denetim polisi değil, üreticiyi büyüten iş planı kuluçkasıyız.",
                    "support_services": [
                        "Halk Eğitim 8 saatlik online Hijyen Eğitimi başvuru yönlendirmesi",
                        "Platform içi T.C. Kültür ve Turizm Bakanlığı kokartlı Turist Rehberi eşleştirmesi",
                        "Gelir Vergisi Kanunu Md. 9 Esnaf Muafiyeti danışmanlığı ile vergisiz yasal satış desteği"
                    ],
                    "fast_track_alternative": "İkram veya rehberlik gerektiren kısımları 'serbest zaman / önerilen mola' formatına çevirerek hemen bugün P0 olarak yayınlayabilirsiniz."
                },
                "badge": "🌿 Büyüme & Rehberlik Yolculuğu Açık",
                "commission_rate": 0.15,
                "requires_insurance": False,
                "rule_version": cls.RULE_VERSION,
                "timestamp": datetime.datetime.utcnow().isoformat()
            }

        # If credentials provided or verified: P1 (Verified Excellence)
        if category in ["food", "cultural", "outdoor"] or participant_count > 50:
            return {
                "pathway_code": "P1",
                "name": "VERIFIED_EXCELLENCE",
                "contracting_party": "ORGANISER_DIRECT",
                "seller_of_record": "DOĞRULANMIŞ ORGANİZATÖR",
                "can_publish": True,
                "reasons": ["Uzmanlık, hijyen ve organizasyon standartları doğrulanmıştır."],
                "remediation_steps": [],
                "badge": "✅ LORAKS Onaylı Mutfak & Zanaat Mührü",
                "commission_rate": 0.15,
                "requires_insurance": False,
                "invoice_type": "HOST_DIRECT_INVOICE",
                "rule_version": cls.RULE_VERSION,
                "timestamp": datetime.datetime.utcnow().isoformat()
            }

        # =====================================================================
        # 4. P0 — DIRECT CRAFT (Pure Workshop, Local Arts & Crafts)
        # =====================================================================
        return {
            "pathway_code": "P0",
            "name": "DIRECT_CRAFT",
            "contracting_party": "ORGANISER_DIRECT",
            "seller_of_record": "ORGANİZATÖR",
            "can_publish": True,
            "reasons": ["Sabit mekanlı atölye ve zanaat buluşması; doğrudan yerel üretici güvencesindedir."],
            "remediation_steps": [],
            "badge": "🌱 LORAKS Doğrudan Zanaat & Atölye",
            "commission_rate": 0.15,
            "requires_insurance": False,
            "invoice_type": "HOST_DIRECT_INVOICE",
            "rule_version": cls.RULE_VERSION,
            "timestamp": datetime.datetime.utcnow().isoformat()
        }

    @classmethod
    def determine_payment_gateway(cls, listing_details: Dict[str, Any]) -> Dict[str, Any]:
        """
        1618 Sayılı TÜRSAB ve 6326 Sayılı TUREB Uyumlu Otomatik POS Yönlendirme Motoru
        """
        has_transport = listing_details.get('has_transport', False) or (listing_details.get('transport_arranged') in ["included_in_price", "optional"])
        has_accommodation = listing_details.get('has_accommodation', False) or listing_details.get('accommodation_included', False)
        is_multi_day = listing_details.get('is_multi_day', False) or listing_details.get('overnight', False)
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
