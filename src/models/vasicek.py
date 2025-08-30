# src/models/vasicek.py

class VasicekModel:
    """
    Implements the Vasicek short-rate model.
    dr_t = kappa * (theta - r_t) * dt + sigma * dW_t
    """
    def __init__(self, kappa, theta, sigma):
        """
        Initializes the Vasicek model.

        Args:
            kappa (float): Speed of mean reversion.
            theta (float): Long-term mean level.
            sigma (float): Volatility parameter.
        """
        self.kappa = kappa
        self.theta = theta
        self.sigma = sigma

    def drift(self, r):
        """
        Calculates the drift term of the SDE.
        """
        return self.kappa * (self.theta - r)

    def diffusion(self, r):
        """
        Calculates the diffusion term of the SDE.
        """
        # In the Vasicek model, diffusion is constant.
        return self.sigma