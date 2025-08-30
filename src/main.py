# main.py

from models.vasicek import VasicekModel
from pricers.bond_pricer import BondPricer
from utils.grid import create_grid

def main():
    """
    Main function to run a sample pricing simulation.
    """
    print("Starting Interest Rate Derivative Pricing Simulation...")

    # 1. Model Parameters (Vasicek)
    kappa = 0.1  # Speed of mean reversion
    theta = 0.05 # Long-term mean level
    sigma = 0.01 # Volatility
    r0 = 0.03    # Initial short rate

    # 2. Derivative Parameters (Zero-Coupon Bond)
    T = 1.0      # Maturity in years
    K = 10000      # Face value of the bond

    # 3. Finite Difference Grid Parameters
    num_r_steps = 100
    num_t_steps = 50
    r_max = 0.2 # Maximum interest rate in the grid

    # 4. Create Model
    model = VasicekModel(kappa, theta, sigma)
    print(f"Created Vasicek Model with kappa={kappa}, theta={theta}, sigma={sigma}")

    # 5. Create Grid
    grid = create_grid(r0, r_max, T, num_r_steps, num_t_steps)
    print(f"Created Finite Difference Grid with {num_r_steps} rate steps and {num_t_steps} time steps.")

    # 6. Create Pricer
    bond_pricer = BondPricer(model, grid)
    print("Initialized Bond Pricer.")

    # 7. Price the bond
    price = bond_pricer.price_zcb(T, K, r0)

    print("\n--------------------------------")
    print(f"Pricing Complete:")
    print(f"  Zero-Coupon Bond Price: {price:.2f}")
    print("--------------------------------\n")

if __name__ == "__main__":
    main()
