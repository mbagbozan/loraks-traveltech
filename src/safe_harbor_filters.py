"""
LORAKS TRAVELTECH — SAFE HARBOR & REGTECH COMPLIANCE FILTER ENGINE
Version: v3.2 Production Ready

Implements hardcoded software safeguards for the 5 critical gray-area liability traps:
1. Senaryo A (Balat / TUREB 6326 S.K.): Multi-stop walking without certified guide license requires explicit non-guiding warranty.
2. Senaryo B (Konvoy Kampı / 1618 S.K.): Overnight / camping is ALWAYS locked to P2 agency shield, regardless of transport provider.
3. Senaryo C (Platform Dışı Ödeme / VUK & 6563 S.K.): Scans listing texts and masks chat messages for off-platform payment triggers (IBAN, cash, phone).
4. Senaryo D (GVK m.9 Esnaf Muafiyeti Hasılat Tavanı): Tracks cumulative GMV and enforces threshold warnings at 80% and blocks booking at 100%.
5. Senaryo F (Supper Club / Evde Yemek & TAPDK): Absolute ban on alcohol in home venues; allergen declaration requirement.
"""

from decimal import Decimal
from typing import Dict, Any, List, Optional
import re
from src.exceptions import ComplianceViolationException

class SafeHarborComplianceFilter:
    # 2026 GVK m.9 Esnaf Muafiyeti Varsayılan Yıllık Hasılat Limiti (TL)
    GVK9_ANNUAL_EXEMPTION_CAP_2026 = Decimal('1100000.00')

    # Off-platform payment detection keywords
    OFF_PLATFORM_PATTERNS = [
        (re.compile(r'(?<!\[)\b(?:iban|havale|eft)(?:[\'a-zçğıöşü]*)?\b(?!\])', re.IGNORECASE), "IBAN/Banka transferi"),
        (re.compile(r'(?<!\[)\bşoför(?:[\'a-zçğıöşü]*)?\b(?!\])', re.IGNORECASE), "Şoföre ödeme"),
        (re.compile(r'(?<!\[)\belden\b(?!\])', re.IGNORECASE), "Elden ödeme"),
        (re.compile(r'(?<!\[)\bnakit(?:[\'a-zçğıöşü]*)?\b(?!\])', re.IGNORECASE), "Nakit ödeme"),
        (re.compile(r'(?<!\[)\bkapıda\s+(?:ödeme|ödersiniz|nakit)\b(?!\])', re.IGNORECASE), "Kapıda ödeme"),
        (re.compile(r'(?<!\[)\bayrıca\s+ödenecektir\b(?!\])', re.IGNORECASE), "Ayrıca ödenecektir"),
        (re.compile(r'(?<!\[)\bekstra\s+transfer\s+ücreti\b(?!\])', re.IGNORECASE), "Ekstra transfer ücreti"),
        (re.compile(r'(?<!\[)\bhesaba\s+gönder(?:[\'a-zçğıöşü]*)?\b(?!\])', re.IGNORECASE), "Hesaba gönder"),
    ]

    @classmethod
    def evaluate_multi_stop_tureb_lock(cls, listing: Dict[str, Any]) -> Dict[str, Any]:
        """
        Senaryo A: Çok duraklı sokak gezilerinde (multi_stop) TUREB 6326 S.K. kontrolü.
        Eğer host kokartlı değilse; açık ve bağlayıcı 'Rehberlik Yapılmayacaktır' taahhüdü zorunludur.
        Aksi takdirde P2 Seyahat Acentesine sevk edilir veya reddedilir.
        """
        is_multi_stop = listing.get("is_multi_stop", False) or listing.get("multi_stop", False)
        has_guide_license = listing.get("has_tourist_guide_license", False) or bool(listing.get("tureb_license_no"))
        non_guiding_warranty = listing.get("non_guiding_warranty_accepted", False)

        if is_multi_stop and not has_guide_license:
            if not non_guiding_warranty:
                raise ComplianceViolationException(
                    "TUREB 6326 S.K. İhlal Riski: Çok duraklı açık alan gezilerinde kokart numarası girilmeli "
                    "veya 'Etkinlik boyunca tarihi/kültürel rehberlik yapılmayacağı, sadece teknik eğitim verileceği' "
                    "taahhüdü dijital olarak onaylanmalıdır."
                )
            return {
                "status": "APPROVED_WITH_LEGAL_DISCLAIMER",
                "disclaimer_text": "Bu etkinlik yalnızca teknik atölye niteliğindedir; tur rehberliği hizmeti içermez.",
                "safe_harbor_logged": True
            }

        return {"status": "COMPLIANT", "safe_harbor_logged": True}

    # Backward compatibility alias
    evaluate_multi_stop_turing_lock = evaluate_multi_stop_tureb_lock

    @classmethod
    def enforce_overnight_p2_lock(cls, listing: Dict[str, Any]) -> bool:
        """
        Senaryo B: Katılımcı kendi aracıyla gelse dahi GECELEME/KAMP varsa İSTİSNASIZ P2'dir (1618 S.K.).
        """
        has_overnight = listing.get("overnight", False) or listing.get("accommodation_included", False) or (listing.get("category") == "camp")
        if has_overnight:
            return True # P2 Kapsamına kilitlenmelidir!
        return False

    @classmethod
    def scan_and_mask_chat_message(cls, message_text: str) -> Dict[str, Any]:
        """
        Senaryo C: Misafir-Host mesajlaşmasında IBAN, telefon ve elden nakit kelimelerini maskeleme motoru.
        Desteklenen formatlar:
        - IBAN: Boşluklu, boşluksuz, noktalı, tireli tüm TR... IBAN'ları.
        - Telefon: +90, 0, parantezli (05xx), (5xx), noktalı ve tireli tüm Türkiye cep numaraları.
        - Kayıt Dışı: Türkçe ek almış (IBANıma, şoförümüze, nakitle vb.) platform dışı ödeme çağrıları.
        """
        violation_detected = False
        reasons = []

        # 1. IBAN Taraması (TR ile başlayan 26 haneli, aralarında boşluk, nokta veya tire bulunabilir)
        iban_pattern = r'\bTR[\s.-]*(?:\d[\s.-]*){24}\b'
        if re.search(iban_pattern, message_text, re.IGNORECASE):
            violation_detected = True
            reasons.append("IBAN paylaşımı tespit edildi.")
            message_text = re.sub(iban_pattern, "[GÜVENLİK NEDENİYLE GİZLENMİŞ IBAN]", message_text, flags=re.IGNORECASE)

        # 2. Telefon Numarası Taraması (05xx, +905xx, (05xx), (5xx), noktalı, tireli, boşluklu)
        phone_pattern = r'(?:\+?90[\s.-]*)?(?:\(?\s*0\s*\)?[\s.-]*)?(?:\(?\s*5\d{2}\s*\)?|5\d{2})[\s.-]*\d{3}[\s.-]*\d{2}[\s.-]*\d{2}'
        if re.search(phone_pattern, message_text):
            violation_detected = True
            reasons.append("Telefon numarası paylaşımı tespit edildi.")
            message_text = re.sub(phone_pattern, "[GÜVENLİK NEDENİYLE GİZLENMİŞ TELEFON]", message_text)

        # 3. Elden Nakit / Kayıt Dışı Ödeme Kelimeleri (Türkçe ek duyarlı)
        for pattern, label in cls.OFF_PLATFORM_PATTERNS:
            if pattern.search(message_text):
                violation_detected = True
                reasons.append(f"Platform dışı ödeme ifadesi: '{label}'")
                message_text = pattern.sub("[KAYIT DIŞI İŞLEM UYARISI]", message_text)

        return {
            "violation_detected": violation_detected,
            "reasons": reasons,
            "sanitized_message": message_text
        }

    @classmethod
    def check_gvk9_exemption_cap(
        cls,
        cumulative_annual_gmv: Decimal,
        new_booking_amount: Decimal,
        annual_cap: Decimal = GVK9_ANNUAL_EXEMPTION_CAP_2026
    ) -> Dict[str, Any]:
        """
        Senaryo D: GVK m.9 Esnaf Muaflığı Kümülatif Hasılat Sayacı (Exemption Cap Tracker).
        """
        projected_gmv = cumulative_annual_gmv + new_booking_amount
        ratio = projected_gmv / annual_cap

        if projected_gmv > annual_cap:
            raise ComplianceViolationException(
                f"GVK m.9 Limit Aşımı: Yıllık esnaf muafiyeti hasılat tavanı ({annual_cap:,.2f} TL) aşıldı! "
                "Yasal mevzuat gereği şahıs şirketi e-Fatura mükellefiyetine geçene kadar yeni rezervasyon alımı askıya alınmıştır."
            )
        elif ratio >= Decimal('0.80'):
            return {
                "status": "WARNING_APPROACHING_LIMIT",
                "ratio_used": float(round(ratio * 100, 2)),
                "remaining_quota": annual_cap - projected_gmv,
                "warning_message": (
                    f"Dikkat: Yıllık esnaf muafiyeti sınırınızın %{ratio*100:.1f}'ine ulaştınız. "
                    "Sınır aşıldığında rezervasyonlarınız durdurulacaktır. LORAKS Vitrin SMMM ile şirketleşme başlatabilirsiniz."
                )
            }
        else:
            return {
                "status": "WITHIN_LIMIT",
                "ratio_used": float(round(ratio * 100, 2)),
                "remaining_quota": annual_cap - projected_gmv
            }

    @classmethod
    def validate_supper_club_and_alcohol(cls, listing: Dict[str, Any]) -> Dict[str, Any]:
        """
        Senaryo F: Evde yemek ve alkol kuralı (TAPDK ve Gıda Hijyeni).
        - venue_type == 'home' ise ASLA alkol seçilemez (TAPDK yasağı).
        - Yemek atölyelerinde alerjen beyan formu zorunludur.
        """
        venue_type = listing.get("venue_type", "studio")
        alcohol_served = listing.get("alcohol_served", False)
        category = listing.get("category", "workshop")
        allergen_form_provided = listing.get("allergen_declaration_accepted", False)

        # SERT YAZILIM KISITI: Evde para karşılığı alkol sunumu kanunen YASAKTIR!
        if venue_type == "home" and alcohol_served:
            raise ComplianceViolationException(
                "TAPDK 4733 S.K. İhlali: Ev veya konut ortamında para karşılığı alkollü içki servisi yapılamaz! "
                "Alkol servisi yalnızca TAPDK ruhsatlı ticari işletmelerde gerçekleştirilebilir."
            )

        if category == "food" and not allergen_form_provided:
            raise ComplianceViolationException(
                "Gıda Güvenliği & Tüketici Kanunu Kısıtı: Yemek etkinliklerinde katılımcı 'Gıda Alerjen ve Sağlık Beyan Formu' "
                "onaylanmadan etkinlik yayınlanamaz."
            )

        return {
            "status": "APPROVED",
            "tapdk_cleared": True,
            "allergen_policy_applied": True
        }
