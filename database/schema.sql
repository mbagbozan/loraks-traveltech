-- ==============================================================================
-- LORAKS TRAVELTECH PLATFORM — DATABASE DDL SCHEMA
-- Dual-Entity Architecture & Compliance-Engine Infrastructure
-- Compliant with: Law 1618 (TÜRSAB), Law 6563 (ETAHS), Law 6493 (PSP),
-- Law 7524 & Decree 9284 (1% Withholding), TFRS 15 (Agent Recognition)
-- ==============================================================================

-- 1. MERCHANTS (Dual-Entity Corporate & Host Registered Entities)
CREATE TABLE IF NOT EXISTS merchants (
    merchant_id VARCHAR(50) PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    tax_number VARCHAR(11) NOT NULL UNIQUE,
    tax_office VARCHAR(100) NOT NULL,
    merchant_type VARCHAR(50) NOT NULL, -- 'PLATFORM_MARKETPLACE', 'LICENSED_TRAVEL_AGENCY', 'HOST'
    tursab_licence_no VARCHAR(20) NULL,  -- e.g., '2387' for Licensed Agency, NULL for pure host/platform
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

-- 4. LISTINGS (Adaptive Experience Offerings Classified by Pathway Engine)
CREATE TABLE IF NOT EXISTS listings (
    listing_id VARCHAR(50) PRIMARY KEY,
    host_id VARCHAR(50) NOT NULL,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(50) NOT NULL, -- 'workshop', 'food', 'cultural', 'outdoor', 'tour', 'retreat'
    price_try DECIMAL(12, 2) NOT NULL,
    duration_hours INT NOT NULL,
    pathway_code VARCHAR(10) NOT NULL, -- 'P0', 'P1', 'P2', 'P3', 'P4'
    contracting_entity_id VARCHAR(50) NOT NULL, -- Host merchant for P0/P1, Licensed Agency merchant for P2
    requires_insurance BOOLEAN DEFAULT FALSE,
    status VARCHAR(30) DEFAULT 'DRAFT', -- 'DRAFT', 'IN_REVIEW', 'PUBLISHED', 'SUSPENDED'
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
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE RESTRICT
);

-- 7. PAYOUT SPLITS & 1% TAX WITHHOLDING (Law 7524 / Decree 9284)
CREATE TABLE IF NOT EXISTS payout_splits (
    split_id VARCHAR(50) PRIMARY KEY,
    payment_id VARCHAR(50) NOT NULL,
    recipient_merchant_id VARCHAR(50) NOT NULL,
    split_type VARCHAR(30) NOT NULL, -- 'PLATFORM_COMMISSION', 'SUPPLIER_PAYOUT', 'TAX_WITHHOLDING'
    gross_split_amount DECIMAL(12, 2) NOT NULL,
    tax_withholding_amount DECIMAL(12, 2) DEFAULT 0.00,
    net_payout_amount DECIMAL(12, 2) NOT NULL,
    invoice_type VARCHAR(50) NOT NULL, -- 'B2B_COMMISSION_INVOICE', 'B2C_TRAVEL_PACKAGE_INVOICE'
    invoice_status VARCHAR(30) DEFAULT 'PENDING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (payment_id) REFERENCES booking_payments(payment_id) ON DELETE CASCADE,
    FOREIGN KEY (recipient_merchant_id) REFERENCES merchants(merchant_id) ON DELETE RESTRICT
);

-- 8. LORAKS CIRCLE WALLET (Non-Cashable Loyalty & Discount Ledger)
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
    reference_type VARCHAR(50) NOT NULL, -- 'INVITATION', 'BOOKING_REWARD', 'DISCOUNT'
    reference_id VARCHAR(50) NOT NULL,
    description VARCHAR(255) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (wallet_id) REFERENCES wallet_balances(wallet_id) ON DELETE RESTRICT
);
