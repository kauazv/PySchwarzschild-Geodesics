import numpy as np
import matplotlib.pyplot as plt

# massa do buraco negro
M = 1.0

# parâmetro de impacto crítico
b_crit = 3 * np.sqrt(3) * M

# ângulo
theta = np.linspace(0, 2*np.pi, 500)

# círculo da sombra
x_shadow = b_crit * np.cos(theta)
y_shadow = b_crit * np.sin(theta)

plt.figure(figsize=(6,6))

plt.fill(x_shadow, y_shadow)

plt.gca().set_aspect("equal")

plt.title("Black Hole Shadow (Schwarzschild)")

plt.xlabel("x")
plt.ylabel("y")

plt.show()