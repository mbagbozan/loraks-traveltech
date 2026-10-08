# src/offline_sync.py
"""
LORAKS Offline-First PWA & QR Doğrulama Motoru (HMAC Time-Based Token)
Doğa kampları, kanyonlar ve çekmeyen koylar için baz istasyonsuz kriptografik bilet doğrulama.
"""
import hmac
import hashlib
import time
import json
from typing import Dict, Any, Tuple

SECRET_KEY = b"LORAKS_OFFLINE_AIRGAP_SECRET_KEY_2026"

class OfflineQRValidator:
    @staticmethod
    def generate_signed_ticket(booking_id: str, guest_id: str, listing_id: str, event_timestamp: int) -> str:
        """
        Bilet satın alındığında gezginin telefonuna indirilen kriptografik QR token.
        İnternet olmasa dahi doğrulanabilir.
        """
        payload = {
            "bid": booking_id,
            "gid": guest_id,
            "lid": listing_id,
            "ts": event_timestamp
        }
        payload_str = json.dumps(payload, sort_keys=True)
        signature = hmac.new(SECRET_KEY, payload_str.encode('utf-8'), hashlib.sha256).hexdigest()
        
        # Bilet paketi: payload + imza
        token = {
            "data": payload,
            "sig": signature[:16]  # Kompakt 16 karakterlik imza
        }
        return json.dumps(token)

    @staticmethod
    def verify_offline_ticket(qr_token_str: str) -> Tuple[bool, Dict[str, Any], str]:
        """
        Host'un telefonundaki LORAKS Host PWA'sı dağ başında (çevrimdışı) bileti okutur.
        Sunucuya gitmeden lokal matematiksel imza doğrulaması yapar.
        """
        try:
            token = json.loads(qr_token_str)
            payload = token["data"]
            provided_sig = token["sig"]
            
            payload_str = json.dumps(payload, sort_keys=True)
            expected_sig = hmac.new(SECRET_KEY, payload_str.encode('utf-8'), hashlib.sha256).hexdigest()[:16]
            
            if hmac.compare_digest(provided_sig, expected_sig):
                return True, payload, "OFFLINE_VALID_CHECKIN_STORED"
            else:
                return False, {}, "INVALID_CRYPTOGRAPHIC_SIGNATURE"
        except Exception as e:
            return False, {}, f"CORRUPTED_QR_TOKEN: {str(e)}"
