# src/pricers/bond_pricer.py
import numpy as np

class BondPricer:
    """
    Prices bonds using a finite difference grid.
    """
    def __init__(self, model, grid):
        """
        Initializes the pricer.

        Args:
            model: An interest rate model (e.g., Vasicek).
            grid: A finite difference grid object.
        """
        self.model = model
        self.grid = grid
        self.dt = grid.T / grid.num_t_steps
        self.dr = grid.r_max / grid.num_r_steps
        self.r_values = np.linspace(0, grid.r_max, grid.num_r_steps + 1)

    def price_zcb(self, T, K, r0):
        """
        Prices a Zero-Coupon Bond using an explicit finite difference scheme.
        """
        # Initialize grid at maturity
        V = np.full(self.grid.num_r_steps + 1, K)

        # Backward induction through time
        for t_step in range(self.grid.num_t_steps -1, -1, -1):
            V_new = np.zeros_like(V)
            for r_step in range(1, self.grid.num_r_steps):
                r = self.r_values[r_step]
                drift = self.model.drift(r)
                diffusion_sq = self.model.diffusion(r)**2

                # Coefficients from the PDE discretization
                A = 0.5 * self.dt * ((diffusion_sq / self.dr**2) - (drift / self.dr))
                B = 1 - self.dt * (diffusion_sq / self.dr**2) - self.dt * r
                C = 0.5 * self.dt * ((diffusion_sq / self.dr**2) + (drift / self.dr))

                V_new[r_step] = A * V[r_step-1] + B * V[r_step] + C * V[r_step+1]

            # Boundary conditions (simplified)
            V_new[0] = V_new[1]
            V_new[-1] = V_new[-2]
            V = V_new

        # Interpolate to find the price at r0
        price = np.interp(r0, self.r_values, V)
        return price
