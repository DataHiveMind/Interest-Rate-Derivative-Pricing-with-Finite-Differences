# tests/test_bond_pricer.py
import unittest
import sys
import os

# Add src to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from models.vasicek import VasicekModel
from pricers.bond_pricer import BondPricer
from utils.grid import create_grid

class TestBondPricer(unittest.TestCase):

    def test_zcb_pricing(self):
        """
        Test the pricing of a zero-coupon bond.
        This is a basic test to ensure the code runs without errors.
        A more robust test would compare against an analytical solution.
        """
        model = VasicekModel(kappa=0.1, theta=0.05, sigma=0.01)
        grid = create_grid(r0=0.03, r_max=0.2, T=1.0, num_r_steps=100, num_t_steps=50)
        pricer = BondPricer(model, grid)
        price = pricer.price_zcb(T=1.0, K=100, r0=0.03)

        self.assertIsInstance(price, float)
        self.assertGreater(price, 0)
        # Expected price for a bond with positive interest rate is less than face value
        self.assertLess(price, 100)

if __name__ == '__main__':
    unittest.main()