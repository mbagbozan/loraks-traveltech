# src/exceptions.py

class ComplianceViolationException(Exception):
    """KVK m.13 veya TÜRSAB 1618 S.K. ihlalinde fırlatılan temel mevzuat istisnası."""
    pass

class InvalidPathwayException(Exception):
    """Geçersiz veya hatalı Pathway kodu durumunda fırlatılır."""
    pass

class FinancialReconciliationException(Exception):
    """Kuruş mutabakatsızlığı veya bilanço uyuşmazlığında fırlatılır."""
    pass
