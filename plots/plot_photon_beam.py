import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import matplotlib.pyplot as plt
from geodesics_photons import integrate_photon_geodesic

# Parâmetros físicos
M = 1.0
E = 1.0

# diferentes momentos angulares (feixe de luz)
L_values = np.linspace(3.5, 8.0, 12)

plt.figure()

for L in L_values:

    t0 = 0.0
    r0 = 30.0
    phi0 = -np.pi/3
    r_dot0 = -0.5

    y0 = [t0, r0, phi0, r_dot0]
    tau_span = (0.0, 200.0)

    solution = integrate_photon_geodesic(
        tau_span=tau_span,
        y0=y0,
        M=M,
        E=E,
        L=L
    )

    r = solution.y[1]
    phi = solution.y[2]

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y)

# Buraco negro
plt.scatter([0], [0])

# Horizonte
circle = plt.Circle((0,0), 2*M, fill=False)
plt.gca().add_patch(circle)

plt.gca().set_aspect("equal")

plt.title("Feixe de fótons em Schwarzschild")
plt.xlabel("x")
plt.ylabel("y")

plt.grid(True)

plt.show()