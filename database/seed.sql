-- ==============================================================================
-- LORAKS TRAVELTECH PLATFORM — v5.3 PRODUCTION SEED DATA
-- ==============================================================================

-- 1. Dual-Entity Merchants
INSERT INTO merchants (merchant_id, company_name, tax_number, tax_office, merchant_type, tursab_licence_no, role_type, payout_iban)
VALUES 
('MERCH-LORAKS-TECH-AS', 'LORAKS TEKNOLOJİ ANONİM ŞİRKETİ', '6091465699', 'Boğaziçi VD', 'PLATFORM_MARKETPLACE', NULL, 'Agent', 'TR110006200000012345678901'),
('MERCH-LORAKS-OPERASYON-AS', 'LORAKS ORGANİZASYON DANIŞMANLIK HİZMETLERİ A.Ş.', '6091465604', 'Zeytinburnu VD', 'LICENSED_TRAVEL_AGENCY', '2387', 'Principal', 'TR220006200000098765432102'),
('MERCH-HOST-KEREM-ANAGAMA', 'Kerem Usta (Geleneksel Çömlek Atölyesi)', '1112223334', 'Avanos VD', 'HOST', NULL, 'Principal', 'TR330006200000055555555503'),
('MERCH-HOST-MELIS-FLORA', 'Melis Kurt (Etnobotanikçi & Doğa Lideri)', '4445556667', 'Edremit VD', 'HOST', NULL, 'Principal', 'TR440006200000077777777704');

-- 2. Hosts (Zamana Kilitli Bağımsız Sanatkarlar)
INSERT INTO hosts (host_id, merchant_id, full_name, email, phone, host_tier, is_certified, hygiene_certified, first_aid_certified, gstc_certified)
VALUES
('HOST-001', 'MERCH-HOST-KEREM-ANAGAMA', 'Kerem Usta', 'kerem@anagama.art', '+905321112233', 'FOUNDING_MAKER', TRUE, FALSE, TRUE, TRUE),
('HOST-002', 'MERCH-HOST-MELIS-FLORA', 'Melis Kurt', 'melis@kazdaglari.bio', '+905334445566', 'FOUNDING_EXPLORER', TRUE, FALSE, TRUE, TRUE);

-- 3. Listings (Zamana Kilitli Nadir Deneyimler & v5.3 Pathway)
INSERT INTO listings (listing_id, host_id, title, category, price_try, duration_hours, pathway_code, contracting_entity_id, requires_insurance, status)
VALUES
('LIST-001-ANAGAMA', 'HOST-001', '72 Saatlik Anagama Odun Fırını Nöbeti & Seramik Pişirimi', 'atölye_zanaat', 6800.00, 72, 'P2', 'MERCH-LORAKS-OPERASYON-AS', TRUE, 'PUBLISHED'),
('LIST-002-KAZDAGI-FLORA', 'HOST-002', 'Kazdağları Yabani Göknar & Şifalı Flora Keşfi', 'sakli_rotalar', 3400.00, 8, 'P2', 'MERCH-LORAKS-OPERASYON-AS', TRUE, 'PUBLISHED');

-- 4. Sample Buyer
INSERT INTO buyers (buyer_id, first_name, last_name, email, identity_number, phone_number, country_code)
VALUES
('BUYER-001', 'Can', 'Öztürk', 'can.ozturk@example.com', '12345678901', '+905559876543', 'TR');

-- 5. Wallet
INSERT INTO wallet_balances (wallet_id, buyer_id, available_points, pending_points)
VALUES
('WALLET-BUYER-001', 'BUYER-001', 250.00, 0.00);
