import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt
from geodesics_massive import integrate_geodesic

M = 1.0
E = 1.0
L = 0.0

y0 = [0.0, 10.0, 0.0, 0.0]
tau_span = (0.0, 100.0)

solution = integrate_geodesic(
    tau_span=tau_span,
    y0=y0,
    M=M,
    E=E,
    L=L
)

tau = solution.t
r = solution.y[1]

plt.figure()
plt.plot(tau, r)
plt.xlabel("Tempo próprio t")
plt.ylabel("Coordenada radial r")
plt.title("Queda radial em Schwarzschild (L = 0)")
plt.grid(True)
plt.show()