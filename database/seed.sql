-- ==============================================================================
-- LORAKS TRAVELTECH PLATFORM — INITIAL SEED DATA
-- Version: v3.2 Production Ready
-- ==============================================================================

-- 1. Dual-Entity Merchants
INSERT INTO merchants (merchant_id, company_name, tax_number, tax_office, merchant_type, tursab_licence_no, role_type, payout_iban)
VALUES 
('MERCH-LORAKS-TECH-AS', 'LORAKS TEKNOLOJİ ANONİM ŞİRKETİ', '6091465699', 'Boğaziçi VD', 'PLATFORM_MARKETPLACE', NULL, 'Agent', 'TR110006200000012345678901'),
('MERCH-LORAKS-OPERASYON-AS', 'LORAKS ORGANİZASYON DANIŞMANLIK HİZMETLERİ A.Ş.', '6091465604', 'Zeytinburnu VD', 'LICENSED_TRAVEL_AGENCY', '16978', 'Principal', 'TR220006200000098765432102'),
('MERCH-HOST-AYSE-SERAMIK', 'Ayşe Demir Sanat Atölyesi', '1112223334', 'Kadıköy VD', 'HOST', NULL, 'Principal', 'TR330006200000055555555503'),
('MERCH-HOST-BURAK-YOGA', 'Burak Yılmaz (Bireysel Eğitmen)', '4445556667', 'Bodrum VD', 'HOST', NULL, 'Principal', 'TR440006200000077777777704'),
('MERCH-HOST-SELIM-CHEF', 'Selim Kara Butik Mutfak', '5556667778', 'Urla VD', 'HOST', NULL, 'Principal', 'TR550006200000088888888805');

-- 2. Hosts
INSERT INTO hosts (host_id, merchant_id, full_name, email, phone, host_tier, is_certified, hygiene_certified, first_aid_certified, gstc_certified, tax_profile)
VALUES
('HOST-001', 'MERCH-HOST-AYSE-SERAMIK', 'Ayşe Demir', 'ayse@seramik.art', '+905321112233', 'FOUNDING_HOST', TRUE, FALSE, TRUE, FALSE, 'INDIVIDUAL_EXEMPT'),
('HOST-002', 'MERCH-HOST-BURAK-YOGA', 'Burak Yılmaz', 'burak@yoga.live', '+905334445566', 'FOUNDING_HOST', TRUE, FALSE, TRUE, TRUE, 'INDIVIDUAL_NON_EXEMPT'),
('HOST-003', 'MERCH-HOST-SELIM-CHEF', 'Selim Kara', 'selim@butikmutfak.com', '+905352223344', 'FOUNDING_HOST', TRUE, TRUE, FALSE, FALSE, 'CORPORATE');

-- 3. Listings (P0 Workshop, P2 Regulated Travel, P1 Food Tasting, P0 Multi-Stop TUREB Warranty)
INSERT INTO listings (
    listing_id, host_id, title, category, price_try, duration_hours,
    pathway_code, contracting_entity_id, requires_insurance, mandatory_insurance_cost,
    status, is_multi_stop, has_tourist_guide_license, non_guiding_warranty_accepted,
    overnight, venue_type, alcohol_served, allergen_declaration_accepted
)
VALUES
('LIST-001-SERAMIK', 'HOST-001', 'Kadıköy Çömlek & Seramik Atölyesi', 'workshop', 1500.00, 3, 'P0', 'MERCH-HOST-AYSE-SERAMIK', FALSE, 0.00, 'PUBLISHED', FALSE, FALSE, FALSE, FALSE, 'studio', FALSE, FALSE),
('LIST-002-TEKNE-YOGA', 'HOST-002', 'Bodrum Günbatımı Tekne Yoga & Meditasyon', 'outdoor', 2500.00, 5, 'P2', 'MERCH-LORAKS-OPERASYON-AS', TRUE, 50.00, 'PUBLISHED', FALSE, FALSE, FALSE, FALSE, 'outdoor', FALSE, FALSE),
('LIST-003-KAMP-KAZDAGLARI', 'HOST-002', 'Kaz Dağları 2 Günlük Doğa ve Meditasyon Kampı', 'camp', 4500.00, 36, 'P2', 'MERCH-LORAKS-OPERASYON-AS', TRUE, 100.00, 'PUBLISHED', FALSE, FALSE, FALSE, TRUE, 'outdoor', FALSE, FALSE),
('LIST-004-URLA-TADIM', 'HOST-003', 'Urla Zeytinyağı ve Şef Tadım Masası', 'food', 3000.00, 4, 'P1', 'MERCH-HOST-SELIM-CHEF', FALSE, 0.00, 'PUBLISHED', FALSE, FALSE, FALSE, FALSE, 'studio', FALSE, TRUE),
('LIST-005-BALAT-FOTOGRAF', 'HOST-001', 'Balat Sokak Fotoğrafçılığı ve Işık Atölyesi', 'cultural', 1800.00, 4, 'P0', 'MERCH-HOST-AYSE-SERAMIK', FALSE, 0.00, 'PUBLISHED', TRUE, FALSE, TRUE, FALSE, 'outdoor', FALSE, FALSE);

-- 4. Sample Buyer
INSERT INTO buyers (buyer_id, first_name, last_name, email, identity_number, phone_number, country_code)
VALUES
('BUYER-001', 'Can', 'Öztürk', 'can.ozturk@example.com', '12345678901', '+905559876543', 'TR');

-- 5. Wallet
INSERT INTO wallet_balances (wallet_id, buyer_id, available_points, pending_points)
VALUES
('WALLET-BUYER-001', 'BUYER-001', 250.00, 0.00);

-- 6. GVK m.9 Esnaf Muafiyeti Hasılat Tavanı Başlangıç Kaydı (2026)
INSERT INTO host_annual_turnovers (turnover_id, host_id, tax_year, cumulative_gmv, annual_cap, is_capped, warning_notified)
VALUES
('TRN-HOST-001-2026', 'HOST-001', 2026, 420000.00, 1100000.00, FALSE, FALSE);

-- 7. KVK m.13 Şirketler Arası Örnek Fatura (Teknoloji A.Ş. -> Acente A.Ş. Cost-Plus)
INSERT INTO intercompany_invoices (
    invoice_id, issuer_merchant_id, recipient_merchant_id, billing_period,
    pricing_method, allocated_shared_costs, base_amount_net, vat_rate, vat_amount, total_invoice_amount, status
)
VALUES
('INV-INTER-2026-10-01', 'MERCH-LORAKS-TECH-AS', 'MERCH-LORAKS-OPERASYON-AS', '2026-10', 'COST_PLUS', 50000.00, 55000.00, 0.20, 11000.00, 66000.00, 'ISSUED');
