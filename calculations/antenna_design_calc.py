"""
Transmission Line Equations & Parameter Calculations for Inset-Fed Rectangular Microstrip Patch Antenna.
"""
import math

def calculate_patch_dimensions(f0_hz=3.8e9, er=4.4, h_m=1.6e-3):
    c = 3e8
    # 1. Patch Width (W)
    w = (c / (2 * f0_hz)) * math.sqrt(2 / (er + 1))
    
    # 2. Effective Dielectric Constant (ereff)
    ereff = ((er + 1) / 2) + ((er - 1) / 2) * (1 / math.sqrt(1 + 12 * (h_m / w)))
    
    # 3. Extension Length (dL)
    dl = h_m * 0.412 * ((ereff + 0.3) * (w / h_m + 0.264)) / ((ereff - 0.258) * (w / h_m + 0.8))
    
    # 4. Actual Length (L)
    l_eff = c / (2 * f0_hz * math.sqrt(ereff))
    l = l_eff - 2 * dl
    
    return {
        "frequency_ghz": f0_hz / 1e9,
        "width_mm": round(w * 1e3, 2),
        "length_mm": round(l * 1e3, 2),
        "dielectric_constant_er": er,
        "substrate_height_mm": h_m * 1e3
    }

if __name__ == "__main__":
    params = calculate_patch_dimensions()
    print("Microstrip Patch Antenna Theoretical Dimensions:", params)
