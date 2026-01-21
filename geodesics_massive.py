import numpy as np
from schwarzschild import schwarzschild_factor

def geodesic_equations(tau, y, M, E, L):
    t, r, phi, r_dot = y
    f = schwarzschild_factor(r, M)
    dt_dtau = E / f
    dphi_dtau = L / r ** 2