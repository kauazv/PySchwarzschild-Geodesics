import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent[1]))

import numpy as np
import matplotlib.pyplot as plt
from geodesics_massive import integrate_geodesic

M = 1.0
E = 0.95
L = 3.8

r0 = 10.0
phi0 = 0.0
t0 = 0.0
r_dot0 = 0.0

y0 = [t0, r0, phi0, r_dot0]
tau_span = (0.0, 300.0)

solution = integrate_geodesic(
    tau_span=tau_span,
    y0=y0,
    M=M,
    E=E,
    L=L
)

r = solution.y[1]
phi = solution.y[2]