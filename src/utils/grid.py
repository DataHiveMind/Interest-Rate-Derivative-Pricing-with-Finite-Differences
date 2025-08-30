# src/utils/grid.py

from collections import namedtuple

Grid = namedtuple('Grid', ['r0', 'r_max', 'T', 'num_r_steps', 'num_t_steps'])

def create_grid(r0, r_max, T, num_r_steps, num_t_steps):
    """
    Creates a named tuple to hold grid parameters.

    Args:
        r0 (float): Initial short rate.
        r_max (float): Maximum interest rate in the grid.
        T (float): Time to maturity.
        num_r_steps (int): Number of steps in the interest rate dimension.
        num_t_steps (int): Number of steps in the time dimension.

    Returns:
        Grid: A named tuple with grid parameters.
    """
    return Grid(r0, r_max, T, num_r_steps, num_t_steps)
