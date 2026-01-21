import numpy as np
from schwarzschild import schwarzschild_factor

def geodesic_equations(tau, y, M, E, L):
    t, r, phi, r_dot = y
    f = schwarzschild_factor(r, M)
    dt_dtau = E / f
    dphi_dtau = L / r ** 2
    r_ddot = (
        - M / r ** 2
        + L ** 2 / r ** 3
        - 3 * M * L ** 2 / r ** 4
    )