import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import matplotlib.pyplot as plt
from geodesics_photons import integrate_photon_geodesic

# parâmetros físicos
M = 1.0
E = 1.0

# parâmetros do "detector"
impact_parameters = np.linspace(3.5, 10.0, 80)

results = []

for L in impact_parameters:

    t0 = 0.0
    r0 = 30.0
    phi0 = -np.pi / 2
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

    # se o fóton caiu no horizonte
    if solution.status == 1:
        results.append(0)
    else:
        results.append(1)

impact_parameters = np.array(impact_parameters)
results = np.array(results)

plt.figure()

plt.scatter(
    impact_parameters,
    results,
    s=10
)

plt.xlabel("Parâmetro de impacto (L)")
plt.ylabel("Escape (1) ou Captura (0)")

plt.title("Captura de fótons por buraco negro")

plt.grid(True)

plt.show()