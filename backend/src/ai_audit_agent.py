# src/ai_audit_agent.py

NLP_P2_MASKING_KEYWORDS = [
    "otobüs", "konaklama", "geceleme", "transfer", "pantheon", "kapadokya",
    "rehber eşliğinde", "servis kalkış noktası", "kalkış saati", 
    "araç içi ikram", "örenyeri giriş bileti", "otel check-in", "konaklamalı paket"
]

def scan_listing_for_p2_masking(listing_text: str) -> bool:
    """
    P0 Atölye olarak girilmiş ancak gizli P2 Paket Tur içeren ilanları %100 taranarak yakalar.
    """
    normalized_text = listing_text.lower()
    for kw in NLP_P2_MASKING_KEYWORDS:
        if kw in normalized_text:
            return True  # P2 Maskeleme Tespiti Yapıldı!
    return False
