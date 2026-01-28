import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))


import numpy as np
from geodesics_massive import integrate_geodesic

M = 1.0
E = 1.0
L = 0.0

t0 = 0.0
r0 = 10.0
phi0 = 0.0
r_dot0 = 0.0

y0 = [t0, r0, phi0, r_dot0]

tau_span = (0.0, 100.0)

solution = integrate_geodesic(
    tau_span=tau_span,
    y0=y0,
    M=M,
    E=E,
    L=L
)

print("Integração finalizada")
print(f"Passos: {len(solution.t)}")
print (f"r final: {solution.y[1][-1]:.4f}")

if solution.status == 1:
    print("Horizonte atingido com sucesso.")
else:
    print("Horizonte não foi atingido.")