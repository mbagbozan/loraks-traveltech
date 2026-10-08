"""
AUTOMATED TEST SUITE FOR LORAKS PATHWAY ENGINE
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from pathway_engine import PathwayEngine

class TestPathwayEngine(unittest.TestCase):

    def test_p0_direct_workshop(self):
        """P0: Fixed-venue ceramics workshop, traveler arrives self."""
        listing = {
            "title": "Kadıköy Çömlek Atölyesi",
            "category": "workshop",
            "venue_type": "fixed_private",
            "transport_arranged": "none",
            "transport_operator": "none",
            "accommodation_included": False,
            "overnight": False,
            "services_bundled": ["instruction", "clay_materials"],
            "single_inclusive_price": True
        }
        res = PathwayEngine.classify(listing)
        self.assertEqual(res["pathway_code"], "P0")
        self.assertEqual(res["contracting_party"], "ORGANISER_DIRECT")
        self.assertTrue(res["can_publish"])
        self.assertFalse(res["requires_insurance"])

    def test_p1_verified_food_with_cert(self):
        """P1: Food tasting workshop with valid hygiene certificate."""
        listing = {
            "title": "Gaziantep Ev Yemekleri Atölyesi",
            "category": "food",
            "venue_type": "fixed_private",
            "transport_arranged": "none",
            "has_hygiene_cert": True,
            "participant_count": 12
        }
        res = PathwayEngine.classify(listing)
        self.assertEqual(res["pathway_code"], "P1")
        self.assertTrue(res["can_publish"])
        self.assertEqual(res["contracting_party"], "ORGANISER_DIRECT")

    def test_p2_licensed_travel_overnight_camp(self):
        """P2: Overnight nature camp with transport (Law 1618 regulated territory)."""
        listing = {
            "title": "Kaz Dağları 2 Günlük Yoga & Doğa Kaçamağı",
            "category": "retreat",
            "transport_arranged": "included_in_price",
            "transport_operator": "licensed_transport_company",
            "accommodation_included": True,
            "overnight": True,
            "services_bundled": ["guide", "transport", "accommodation", "yoga"]
        }
        res = PathwayEngine.classify(listing)
        self.assertEqual(res["pathway_code"], "P2")
        self.assertEqual(res["contracting_party"], "LICENSED_TRAVEL_AGENCY")
        self.assertTrue(res["can_publish"])
        self.assertTrue(res["requires_insurance"])
        self.assertIn("TÜRSAB", res["badge"])

    def test_p3_restricted_missing_guide_license(self):
        """P3: Tour at heritage site without guide license (Remediable guidance)."""
        listing = {
            "title": "Tarihi Sultanahmet Yürüyüşü",
            "category": "cultural",
            "heritage_or_protected_site": True,
            "has_tourist_guide_license": False
        }
        res = PathwayEngine.classify(listing)
        self.assertEqual(res["pathway_code"], "P3")
        self.assertFalse(res["can_publish"])
        self.assertTrue(res.get("guidance_mode", False))
        self.assertIn("guidance_incubator", res)
        self.assertTrue(len(res["remediation_steps"]) > 0)

    def test_p4_prohibited_illegal_passenger_transport(self):
        """P4: Transport in organizer's own unlicensed vehicle for hire with Fast-Track options."""
        listing = {
            "title": "Şahsi Arabamla Sapanca Turu",
            "category": "tour",
            "transport_arranged": "included_in_price",
            "transport_operator": "organiser_own_vehicle"
        }
        res = PathwayEngine.classify(listing)
        self.assertEqual(res["pathway_code"], "P4")
        self.assertFalse(res["can_publish"])
        self.assertEqual(res["contracting_party"], "NONE")
        self.assertIn("fast_track_options", res)
        self.assertEqual(len(res["fast_track_options"]), 2)

if __name__ == "__main__":
    unittest.main()
