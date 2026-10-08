"""
LORAKS TRAVELTECH — REGTECH NLP & LLM AUDIT AGENT
Version: v3.2 Production Ready
Scans listing descriptions, titles and promotional text for:
1. Masked P2 regulated travel elements (TÜRSAB 1618 S.K.)
2. Off-platform split billing and cash leakage phrases (6563 S.K. & VUK)
"""

from typing import List, Dict, Any

NLP_P2_MASKING_KEYWORDS: List[str] = [
    "otobüs", "konaklama", "geceleme", "transfer", "pantheon", "kapadokya",
    "rehber eşliğinde", "servis kalkış noktası", "kalkış saati", 
    "araç içi ikram", "örenyeri giriş bileti", "otel check-in", "konaklamalı paket"
]

NLP_OFF_PLATFORM_KEYWORDS: List[str] = [
    "elden", "nakit", "şoföre", "ayrıca ödenecektir", "ekstra transfer ücreti",
    "elden nakit", "kapıda ödeme", "kalanını elden", "ücret şoföre verilecektir"
]

def scan_listing_for_p2_masking(listing_text: str) -> bool:
    """
    P0 Atölye olarak girilmiş ancak gizli P2 Paket Tur içeren ilanları %100 taranarak yakalar.
    """
    if not listing_text:
        return False
    normalized_text = listing_text.lower()
    for kw in NLP_P2_MASKING_KEYWORDS:
        if kw in normalized_text:
            return True
    return False

def scan_offplatform_payment(listing_text: str) -> Dict[str, Any]:
    """
    Senaryo C: İlan metninde platform dışı / elden ödeme hilesi tespit motoru.
    """
    if not listing_text:
        return {"detected": False, "matched_keywords": []}
    
    normalized_text = listing_text.lower()
    matched = [kw for kw in NLP_OFF_PLATFORM_KEYWORDS if kw in normalized_text]
    return {
        "detected": len(matched) > 0,
        "matched_keywords": matched,
        "action_required": "QUARANTINE_LISTING" if len(matched) > 0 else "NONE"
    }
