import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import matplotlib.pyplot as plt
from geodesics_photons import integrate_photon_geodesic

# Parâmetros físicos
M = 1.0
E = 1.0
L = 5.5

# Condições iniciais
t0 = 0.0
r0 = 30.0
phi0 = -np.pi/4
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

# Converter para coordenadas cartesianas
x = r * np.cos(phi)
y = r * np.sin(phi)

plt.figure()

plt.plot(x, y, label="trajetória do fóton")

# Buraco negro
plt.scatter([0], [0], label="buraco negro")

# Horizonte de eventos
circle = plt.Circle((0,0), 2*M, fill=False, linestyle="--")
plt.gca().add_patch(circle)

plt.gca().set_aspect("equal")

plt.xlabel("x")
plt.ylabel("y")

plt.title("Desvio gravitacional da luz em Schwarzschild")

plt.legend()
plt.grid(True)

plt.show()