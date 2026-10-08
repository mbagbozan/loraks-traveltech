-- ==============================================================================
-- LORAKS TRAVELTECH PLATFORM — DATABASE DDL SCHEMA
-- Dual-Entity Architecture & Compliance-Engine Infrastructure
-- Compliant with: Law 1618 (TÜRSAB), Law 6326 (TUREB), Law 6563 (ETAHS),
-- Law 6493 (PSP & Zero Unlicensed Holds), Law 7524 & Decree 9284 (1% Withholding),
-- KVK m. 13 (Arms-Length Intercompany Cost-Plus), GVK m. 9 (Esnaf Muafiyeti Cap),
-- 4733 S.K. (TAPDK Home Dining Alcohol Ban), TFRS 15 (Agent Recognition)
-- Version: v3.2 Production Ready
-- ==============================================================================

-- 1. MERCHANTS (Dual-Entity Corporate & Host Registered Entities)
CREATE TABLE IF NOT EXISTS merchants (
    merchant_id VARCHAR(50) PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    tax_number VARCHAR(11) NOT NULL UNIQUE,
    tax_office VARCHAR(100) NOT NULL,
    merchant_type VARCHAR(50) NOT NULL, -- 'PLATFORM_MARKETPLACE', 'LICENSED_TRAVEL_AGENCY', 'HOST'
    tursab_licence_no VARCHAR(20) NULL,  -- e.g., '16978' for Licensed Agency, NULL for pure host/platform
    role_type VARCHAR(20) NOT NULL,      -- 'Agent' (Platform) or 'Principal' (Agency)
    payout_iban VARCHAR(34) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. HOSTS (Experience Creators / Instructors)
CREATE TABLE IF NOT EXISTS hosts (
    host_id VARCHAR(50) PRIMARY KEY,
    merchant_id VARCHAR(50) NOT NULL,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    host_tier VARCHAR(20) DEFAULT 'STANDARD', -- 'FOUNDING_HOST', 'STANDARD', 'PREMIUM'
    is_certified BOOLEAN DEFAULT FALSE,
    hygiene_certified BOOLEAN DEFAULT FALSE,
    first_aid_certified BOOLEAN DEFAULT FALSE,
    gstc_certified BOOLEAN DEFAULT FALSE,
    tax_profile VARCHAR(30) DEFAULT 'INDIVIDUAL_EXEMPT', -- 'CORPORATE', 'INDIVIDUAL_EXEMPT', 'INDIVIDUAL_NON_EXEMPT'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (merchant_id) REFERENCES merchants(merchant_id) ON DELETE RESTRICT
);

-- 3. BUYERS (Travelers / Participants)
CREATE TABLE IF NOT EXISTS buyers (
    buyer_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    identity_number VARCHAR(11) NOT NULL, -- TCKN or Passport for mandatory insurance and e-archive invoice
    phone_number VARCHAR(20) NOT NULL,
    country_code VARCHAR(3) DEFAULT 'TR',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. LISTINGS (Adaptive Experience Offerings Classified by Pathway Engine & Safe Harbor)
CREATE TABLE IF NOT EXISTS listings (
    listing_id VARCHAR(50) PRIMARY KEY,
    host_id VARCHAR(50) NOT NULL,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(50) NOT NULL, -- 'workshop', 'food', 'cultural', 'outdoor', 'tour', 'retreat', 'camp'
    price_try DECIMAL(12, 2) NOT NULL,
    duration_hours INT NOT NULL,
    pathway_code VARCHAR(10) NOT NULL, -- 'P0', 'P1', 'P2', 'P3', 'P4'
    contracting_entity_id VARCHAR(50) NOT NULL, -- Host merchant for P0/P1, Licensed Agency merchant for P2
    requires_insurance BOOLEAN DEFAULT FALSE,
    mandatory_insurance_cost DECIMAL(12, 2) DEFAULT 0.00, -- 1618 S.K. Zorunlu Sigorta (BSMV tabi, KDV'den istisna)
    status VARCHAR(30) DEFAULT 'DRAFT', -- 'DRAFT', 'IN_REVIEW', 'PUBLISHED', 'QUARANTINED', 'SUSPENDED'
    
    -- Safe Harbor & RegTech Safeguard Columns (v3.2)
    is_multi_stop BOOLEAN DEFAULT FALSE,
    has_tourist_guide_license BOOLEAN DEFAULT FALSE,
    tureb_license_no VARCHAR(50) NULL,
    non_guiding_warranty_accepted BOOLEAN DEFAULT FALSE, -- Senaryo A (TUREB 6326)
    overnight BOOLEAN DEFAULT FALSE,                     -- Senaryo B (Konvoy Kampı -> Otomatik P2)
    venue_type VARCHAR(50) DEFAULT 'studio',             -- 'home', 'studio', 'outdoor'
    alcohol_served BOOLEAN DEFAULT FALSE,                -- Senaryo F (TAPDK 4733 S.K.)
    allergen_declaration_accepted BOOLEAN DEFAULT FALSE, -- Senaryo F (Gıda Alerjen Beyanı)
    
    classification_evidence JSON NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (host_id) REFERENCES hosts(host_id) ON DELETE RESTRICT,
    FOREIGN KEY (contracting_entity_id) REFERENCES merchants(merchant_id) ON DELETE RESTRICT
);

-- 5. BOOKINGS
CREATE TABLE IF NOT EXISTS bookings (
    booking_id VARCHAR(50) PRIMARY KEY,
    buyer_id VARCHAR(50) NOT NULL,
    listing_id VARCHAR(50) NOT NULL,
    booking_date TIMESTAMP NOT NULL,
    participant_count INT DEFAULT 1,
    total_amount_try DECIMAL(12, 2) NOT NULL,
    status VARCHAR(30) DEFAULT 'PENDING', -- 'PENDING', 'CONFIRMED', 'COMPLETED', 'CANCELLED'
    qr_checkin_code VARCHAR(64) UNIQUE NOT NULL,
    is_checked_in BOOLEAN DEFAULT FALSE,
    checked_in_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (buyer_id) REFERENCES buyers(buyer_id) ON DELETE RESTRICT,
    FOREIGN KEY (listing_id) REFERENCES listings(listing_id) ON DELETE RESTRICT
);

-- 6. BOOKING PAYMENTS (Payment Ledger & PSP Escrow State)
CREATE TABLE IF NOT EXISTS booking_payments (
    payment_id VARCHAR(50) PRIMARY KEY,
    booking_id VARCHAR(50) NOT NULL UNIQUE,
    idempotency_key VARCHAR(64) NOT NULL UNIQUE,
    payment_token VARCHAR(100) NOT NULL,
    total_gross_amount DECIMAL(12, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'TRY',
    status VARCHAR(30) DEFAULT 'IN_ESCROW', -- 'IN_ESCROW', 'SETTLED', 'REFUNDED', 'DISPUTED'
    settled_at TIMESTAMP NULL,
    refunded_at TIMESTAMP NULL,
    cancellation_reason VARCHAR(100) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE RESTRICT
);

-- 7. PAYOUT SPLITS & 1% TAX WITHHOLDING (Law 7524 / Decree 9284 & KVK m. 13)
CREATE TABLE IF NOT EXISTS payout_splits (
    split_id VARCHAR(50) PRIMARY KEY,
    payment_id VARCHAR(50) NOT NULL,
    recipient_merchant_id VARCHAR(50) NOT NULL,
    split_type VARCHAR(30) NOT NULL, -- 'PLATFORM_COMMISSION', 'SUPPLIER_PAYOUT', 'TAX_WITHHOLDING'
    gross_split_amount DECIMAL(12, 2) NOT NULL,
    tax_withholding_amount DECIMAL(12, 2) DEFAULT 0.00,
    net_payout_amount DECIMAL(12, 2) NOT NULL,
    pos_fee_absorbed DECIMAL(12, 2) DEFAULT 0.00, -- KVK m. 13: Ciroyu yazan tüzel kişilikte yalıtılır
    invoice_type VARCHAR(50) NOT NULL, -- 'B2B_COMMISSION_INVOICE', 'B2C_TRAVEL_PACKAGE_INVOICE'
    invoice_status VARCHAR(30) DEFAULT 'PENDING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (payment_id) REFERENCES booking_payments(payment_id) ON DELETE CASCADE,
    FOREIGN KEY (recipient_merchant_id) REFERENCES merchants(merchant_id) ON DELETE RESTRICT
);

-- 8. LORAKS CIRCLE WALLET (Non-Cashable Loyalty & Discount Ledger - 6493 S.K. Uyumlu)
CREATE TABLE IF NOT EXISTS wallet_balances (
    wallet_id VARCHAR(50) PRIMARY KEY,
    buyer_id VARCHAR(50) NOT NULL UNIQUE,
    available_points DECIMAL(12, 2) DEFAULT 0.00,
    pending_points DECIMAL(12, 2) DEFAULT 0.00,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (buyer_id) REFERENCES buyers(buyer_id) ON DELETE RESTRICT
);

-- 9. WALLET TRANSACTIONS (ACID Ledger of Earned / Spent Points)
CREATE TABLE IF NOT EXISTS wallet_transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    wallet_id VARCHAR(50) NOT NULL,
    points DECIMAL(12, 2) NOT NULL,
    transaction_type VARCHAR(20) NOT NULL, -- 'EARN', 'SPEND', 'REFUND', 'EXPIRE'
    reference_type VARCHAR(50) NOT NULL,   -- 'INVITATION', 'BOOKING_REWARD', 'DISCOUNT'
    reference_id VARCHAR(50) NOT NULL,
    description VARCHAR(255) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (wallet_id) REFERENCES wallet_balances(wallet_id) ON DELETE RESTRICT
);

-- 10. GVK m. 9 ESNAF MUAFIYETI HASILAT TAVANI TAKIBI (Senaryo D)
CREATE TABLE IF NOT EXISTS host_annual_turnovers (
    turnover_id VARCHAR(50) PRIMARY KEY,
    host_id VARCHAR(50) NOT NULL,
    tax_year INT NOT NULL,
    cumulative_gmv DECIMAL(12, 2) DEFAULT 0.00,
    annual_cap DECIMAL(12, 2) DEFAULT 1100000.00, -- 2026 GVK m.9 Esnaf Muafiyeti Hasılat Tavanı
    is_capped BOOLEAN DEFAULT FALSE,
    warning_notified BOOLEAN DEFAULT FALSE,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (host_id) REFERENCES hosts(host_id) ON DELETE RESTRICT,
    UNIQUE(host_id, tax_year)
);

-- 11. KVK m. 13 ŞİRKETLER ARASI EMSAL HİZMET VE YAZILIM FATURALANDIRMASI
CREATE TABLE IF NOT EXISTS intercompany_invoices (
    invoice_id VARCHAR(50) PRIMARY KEY,
    issuer_merchant_id VARCHAR(50) NOT NULL,     -- LORAKS TEKNOLOJİ A.Ş.
    recipient_merchant_id VARCHAR(50) NOT NULL,  -- LORAKS SEYAHAT ACENTASI A.Ş.
    billing_period VARCHAR(7) NOT NULL,          -- Örn: '2026-10'
    pricing_method VARCHAR(50) NOT NULL,         -- 'COST_PLUS', 'TURNOVER_ROYALTY'
    allocated_shared_costs DECIMAL(12, 2) NOT NULL,
    base_amount_net DECIMAL(12, 2) NOT NULL,     -- Maliyet + %10 Emsal Kâr
    vat_rate DECIMAL(4, 2) DEFAULT 0.20,
    vat_amount DECIMAL(12, 2) NOT NULL,
    total_invoice_amount DECIMAL(12, 2) NOT NULL,
    status VARCHAR(30) DEFAULT 'ISSUED',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (issuer_merchant_id) REFERENCES merchants(merchant_id) ON DELETE RESTRICT,
    FOREIGN KEY (recipient_merchant_id) REFERENCES merchants(merchant_id) ON DELETE RESTRICT
);

-- 12. REGTECH SAFE HARBOR & SOZLESME DENETİM KAYITLARI (Senaryo A, C, F)
CREATE TABLE IF NOT EXISTS safe_harbor_audit_logs (
    audit_id SERIAL PRIMARY KEY,
    entity_type VARCHAR(30) NOT NULL, -- 'LISTING', 'CHAT_MESSAGE', 'PAYOUT'
    entity_id VARCHAR(50) NOT NULL,
    rule_applied VARCHAR(50) NOT NULL, -- 'TUREB_6326', 'TAPDK_4733', 'OFF_PLATFORM_VUK', 'GVK_9_CAP'
    action_taken VARCHAR(50) NOT NULL, -- 'MASKED', 'APPROVED_DISCLAIMER', 'BLOCKED', 'QUARANTINED'
    details JSON NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
