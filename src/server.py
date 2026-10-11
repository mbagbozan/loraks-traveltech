"""
LORAKS TRAVELTECH — LOCAL COMPLIANCE & API SERVER
Lightweight standard library HTTP server providing live REST endpoints and Dashboard UI
Version: v3.2 Production Ready
"""

import http.server
import socketserver
import json
import os
import sys
from decimal import Decimal

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from pathway_engine import PathwayEngine
from payment_engine import PaymentEngine
from wallet_ledger import WalletLedger
from safe_harbor_filters import SafeHarborComplianceFilter
from ai_audit_agent import scan_listing_for_p2_masking, scan_offplatform_payment
from intercompany_billing import IntercompanyBillingEngine
from exceptions import ComplianceViolationException, InvalidPathwayException

PORT = 8080

payment_engine = PaymentEngine()
wallet_ledger = WalletLedger()

# Seed wallet with demo points
wallet_ledger.credit_points("BUYER-DEMO", 250.00, "SYSTEM_SEED", "INIT", "Hoş geldin LORAKS Puanı")

class LoraksApiHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            html_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html")
            with open(html_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        if self.path == "/api/wallet":
            wallet = wallet_ledger.get_or_create_wallet("BUYER-DEMO")
            self.send_json_response(200, {
                "buyer_id": "BUYER-DEMO",
                "wallet": wallet,
                "transactions": wallet_ledger.transactions
            })
            return

        if self.path == "/api/health":
            self.send_json_response(200, {
                "status": "HEALTHY",
                "service": "LORAKS Compliance & FinTech Core",
                "version": "v3.2-PRODUCTION"
            })
            return

        self.send_error(404, "Not Found")

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")
        try:
            data = json.loads(body) if body else {}
        except Exception:
            data = {}

        if self.path == "/api/classify":
            result = PathwayEngine.classify(data)
            self.send_json_response(200, result)
            return

        if self.path == "/api/calculate-split":
            gross = float(data.get("gross_amount", 1000.00))
            pathway = data.get("pathway_code", "P0")
            is_direct = data.get("is_direct_link", False)
            result = payment_engine.calculate_split(gross, pathway, is_direct)
            self.send_json_response(200, result)
            return

        if self.path == "/api/charge":
            booking_id = data.get("booking_id", f"BK-{os.urandom(4).hex().upper()}")
            gross = float(data.get("gross_amount", 1000.00))
            idemp_key = data.get("idempotency_key", f"idemp_{os.urandom(6).hex()}")
            pathway = data.get("pathway_code", "P0")
            result = payment_engine.process_charge(booking_id, gross, idemp_key, pathway, data.get("buyer_info"))
            self.send_json_response(200, result)
            return

        if self.path == "/api/settle":
            payment_id = data.get("payment_id")
            try:
                result = payment_engine.settle_payment(payment_id, verified_by_qr=True)
                self.send_json_response(200, result)
            except Exception as e:
                self.send_json_response(400, {"error": str(e)})
            return

        if self.path == "/api/cancel-and-refund":
            payment_id = data.get("payment_id")
            reason = data.get("reason", "GUEST_OR_WEATHER_CANCELLATION")
            try:
                result = payment_engine.cancel_and_refund(payment_id, reason=reason)
                self.send_json_response(200, result)
            except Exception as e:
                self.send_json_response(400, {"error": str(e)})
            return

        # =====================================================================
        # RECENT COMPLIANCE ENDPOINTS (v3.2 Production Ready)
        # =====================================================================
        if self.path == "/api/audit-listing":
            text = data.get("listing_text", "")
            if not text:
                text = f"{data.get('title', '')} {data.get('description', '')}"
            p2_masked = scan_listing_for_p2_masking(text)
            off_platform = scan_offplatform_payment(text)
            self.send_json_response(200, {
                "text_scanned": text,
                "p2_masking_detected": p2_masked,
                "off_platform_audit": off_platform,
                "compliance_status": "FLAGGED_FOR_REVIEW" if (p2_masked or off_platform["detected"]) else "PASSED"
            })
            return

        if self.path == "/api/chat-sanitize":
            message = data.get("message", "")
            result = SafeHarborComplianceFilter.scan_and_mask_chat_message(message)
            self.send_json_response(200, result)
            return

        if self.path == "/api/safe-harbor-check":
            try:
                # 1. Multi-stop TUREB check
                turing_result = SafeHarborComplianceFilter.evaluate_multi_stop_turing_lock(data)
                # 2. Overnight camp P2 lock
                is_p2_locked = SafeHarborComplianceFilter.enforce_overnight_p2_lock(data)
                # 3. Supper club alcohol & allergen check
                supper_result = SafeHarborComplianceFilter.validate_supper_club_and_alcohol(data)

                self.send_json_response(200, {
                    "status": "APPROVED",
                    "turing_audit": turing_result,
                    "overnight_p2_lock": is_p2_locked,
                    "supper_club_audit": supper_result
                })
            except ComplianceViolationException as cve:
                self.send_json_response(400, {
                    "status": "VIOLATION",
                    "error_type": "ComplianceViolationException",
                    "message": str(cve)
                })
            except Exception as ex:
                self.send_json_response(400, {"status": "ERROR", "message": str(ex)})
            return

        if self.path == "/api/gvk9-check":
            try:
                cumulative_gmv = Decimal(str(data.get("cumulative_annual_gmv", 0.0)))
                new_booking = Decimal(str(data.get("new_booking_amount", 0.0)))
                annual_cap = Decimal(str(data.get("annual_cap", "1100000.00")))

                result = SafeHarborComplianceFilter.check_gvk9_exemption_cap(
                    cumulative_annual_gmv=cumulative_gmv,
                    new_booking_amount=new_booking,
                    annual_cap=annual_cap
                )
                self.send_json_response(200, result)
            except ComplianceViolationException as cve:
                self.send_json_response(400, {
                    "status": "EXCEEDED_BLOCKED",
                    "error_type": "ComplianceViolationException",
                    "message": str(cve)
                })
            return

        if self.path == "/api/intercompany-invoice":
            try:
                p2_turnover = Decimal(str(data.get("p2_gross_turnover", "100000.00")))
                shared_costs = Decimal(str(data.get("allocated_shared_costs", "20000.00")))
                method = data.get("method", "COST_PLUS")

                result = IntercompanyBillingEngine.calculate_monthly_intercompany_invoice(
                    p2_gross_turnover=p2_turnover,
                    allocated_shared_costs=shared_costs,
                    method=method
                )
                self.send_json_response(200, result)
            except ComplianceViolationException as cve:
                self.send_json_response(400, {
                    "status": "VIOLATION",
                    "error_type": "ComplianceViolationException",
                    "message": str(cve)
                })
            except Exception as ex:
                self.send_json_response(400, {"status": "ERROR", "message": str(ex)})
            return

        self.send_error(404, "Endpoint Not Found")

    def send_json_response(self, code: int, payload: dict):
        body = json.dumps(
            payload,
            default=lambda o: float(o) if isinstance(o, Decimal) else str(o),
            ensure_ascii=False,
            indent=2
        ).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), LoraksApiHandler) as httpd:
        print(f"🚀 LORAKS TravelTech Server Canlıda: http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
