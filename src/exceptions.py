"""
LORAKS TRAVELTECH — COMPLIANCE & FINANCIAL EXCEPTIONS
Custom Exception classes for strict runtime invariants (KVK m.13, TÜRSAB 1618, TUREB 6326, Law 7524)
"""

class ComplianceViolationException(Exception):
    """KVK m.13 veya TÜRSAB 1618 S.K. ihlalinde fırlatılan temel mevzuat istisnası."""
    pass

class InvalidPathwayException(Exception):
    """Geçersiz veya hatalı Pathway kodu durumunda fırlatılır."""
    pass

class FinancialReconciliationException(Exception):
    """Kuruş mutabakatsızlığı veya bilanço uyuşmazlığında fırlatılır."""
    pass
