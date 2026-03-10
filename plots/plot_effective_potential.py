import numpy as np
import matplotlib.pyplot as plt

# Parâmetros físicos
M = 1.0
L = 3.8

def V_eff(r, M, L):
    return np.sqrt((1 - 2*M/r) * (1 + L**2 / r**2))

r = np.linspace(2.1, 50, 1000)
V = V_eff(r, M, L)

plt.figure()
plt.plot(r, V)
plt.axvline(6*M, linestyle="--", label="ISCO (6M)")
plt.axvline(3*M, linestyle=":", label="Órbita instável (3M)")
plt.xlabel("r")
plt.ylabel("V_eff(r)")
plt.title("Potencial efetivo em Schwarzschild")
plt.legend()
plt.grid(True)
plt.show()