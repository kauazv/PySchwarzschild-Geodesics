import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import matplotlib.pyplot as plt
from geodesics_photons import integrate_photon_geodesic

M = 1.0
E = 1.0

impact_parameters = np.linspace(6.0, 15.0, 20)

deflection_angles = []

for L in impact_parameters:

    t0 = 0.0
    r0 = 50.0
    phi0 = -np.pi/2
    r_dot0 = -0.2

    y0 = [t0, r0, phi0, r_dot0]

    tau_span = (0.0, 300.0)

    sol = integrate_photon_geodesic(
        tau_span=tau_span,
        y0=y0,
        M=M,
        E=E,
        L=L
    )

    phi = sol.y[2]

    # ângulo total percorrido
    delta_phi = phi[-1] - phi[0]

    # deflexão relativa à linha reta
    deflection = delta_phi - np.pi

    deflection_angles.append(deflection)

impact_parameters = np.array(impact_parameters)
deflection_angles = np.array(deflection_angles)

plt.figure()

plt.plot(impact_parameters, deflection_angles, label="Simulação")

# previsão teórica fraca
theory = 4*M/impact_parameters

plt.plot(impact_parameters, theory, "--", label="Aproximação GR")

plt.xlabel("Parâmetro de impacto")
plt.ylabel("Ângulo de deflexão")

plt.title("Deflexão gravitacional da luz")

plt.legend()
plt.grid(True)

plt.show()