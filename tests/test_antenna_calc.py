#!/usr/bin/env python3
"""
Unit Test Suite for Transmission Line Microstrip Patch Equations.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../calculations")))
from antenna_design_calc import calculate_patch_dimensions

class TestAntennaCalculation(unittest.TestCase):

    def test_dimensions_3_8ghz(self):
        res = calculate_patch_dimensions(f0_hz=3.8e9, er=4.4, h_m=1.6e-3)
        self.assertEqual(res["frequency_ghz"], 3.8)
        self.assertAlmostEqual(res["width_mm"], 24.0, delta=1.0)
        self.assertAlmostEqual(res["length_mm"], 18.0, delta=1.5)
        self.assertTrue(res["width_mm"] > res["length_mm"])

if __name__ == "__main__":
    unittest.main()
