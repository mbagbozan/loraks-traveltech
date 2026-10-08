/**
 * LORAKS TRAVELTECH — SHARED TYPESCRIPT DEFINITIONS
 * Dual-Entity & Pathway-First Compliance Framework
 * Version: v3.2 Production Ready
 */

export type PathwayCode = 'P0' | 'P1' | 'P2' | 'P3' | 'P4';

export interface ListingClassificationInput {
  title: string;
  category: 'workshop' | 'food' | 'cultural' | 'outdoor' | 'tour' | 'retreat' | 'corporate';
  transport_arranged: 'none' | 'included_in_price' | 'optional' | 'recommended_only';
  transport_operator: 'none' | 'licensed_transport_company' | 'organiser_own_vehicle';
  accommodation_included: boolean;
  overnight: boolean;
  services_bundled: string[];
  single_inclusive_price: boolean;
  venue_type: 'fixed_public' | 'fixed_private' | 'moving' | 'multiple' | 'home' | 'studio';
  participant_count: number;
  alcohol_served: boolean;
  heritage_or_protected_site: boolean;
  has_hygiene_cert?: boolean;
  has_tourist_guide_license?: boolean;
  has_instructor_cert?: boolean;
  is_multi_stop?: boolean;
  non_guiding_warranty_accepted?: boolean;
  allergen_declaration_accepted?: boolean;
}

export interface PathwayResult {
  pathway_code: PathwayCode;
  name: string;
  contracting_party: string;
  seller_of_record?: string;
  can_publish: boolean;
  reasons: string[];
  remediation_steps: string[];
  badge: string;
  commission_rate: number;
  requires_insurance: boolean;
  invoice_type?: string;
  rule_version: string;
  timestamp: string;
}

export interface SplitPaymentDetails {
  gross_amount: number;
  pathway_code: PathwayCode;
  commission_rate: number;
  splits: {
    platform_take_rate: {
      recipient: string;
      gross_amount: number;
      net_matrah: number;
      kdv_20: number;
      invoice_type: string;
    };
    tax_withholding_gib: {
      recipient: string;
      amount: number;
      law_reference: string;
    };
    supplier_net_payout: {
      recipient: string;
      net_amount: number;
      payout_condition: string;
    };
  };
  invoicing: {
    b2c_customer_invoice: {
      issuer: string;
      total_amount: number;
      description: string;
    };
    b2b_platform_invoice: {
      issuer: string;
      receiver: string;
      amount: number;
      description: string;
    };
  };
}

export interface ChatSanitizeResult {
  violation_detected: boolean;
  reasons: string[];
  sanitized_message: string;
}

export interface OffPlatformScanResult {
  detected: boolean;
  matched_keywords: string[];
  action_required: 'NONE' | 'QUARANTINE_LISTING';
}

export interface SafeHarborComplianceResult {
  status: 'APPROVED' | 'APPROVED_WITH_LEGAL_DISCLAIMER' | 'REJECTED' | 'WARNING';
  disclaimer_text?: string;
  tapdk_cleared?: boolean;
  allergen_policy_applied?: boolean;
  safe_harbor_logged?: boolean;
  error?: string;
}

export interface Gvk9ExemptionCapResult {
  status: 'WITHIN_LIMIT' | 'WARNING_APPROACHING_LIMIT' | 'EXCEEDED';
  ratio_used: number;
  remaining_quota: number;
  warning_message?: string;
  error?: string;
}

export interface IntercompanyInvoiceResult {
  issuer: string;
  recipient: string;
  invoice_type: string;
  transfer_pricing_method: string;
  allocated_shared_costs: number;
  base_amount_net: number;
  vat_rate: number;
  vat_amount: number;
  total_invoice_amount: number;
  accounting_entries: {
    teknoloji_as: {
      credit_account: string;
      credit_vat_account: string;
      debit_account: string;
    };
    acenta_as: {
      debit_account: string;
      debit_vat_account: string;
      credit_account: string;
    };
  };
}
