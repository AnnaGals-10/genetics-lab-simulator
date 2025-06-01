import numpy as np
import pandas as pd

# 🔧 Constants del sistema (del teu PDF)
m = 0.1         # massa del pèndol (kg)
Mc = 0.135      # massa del carro (kg)
L = 0.2         # longitud fins al centre de massa del pèndol (m)
I = 0.00072     # moment d'inèrcia del pèndol (kg·m²)
B = 0.000078    # fricció angular al pivot (N·m·s)
C = 0.63        # fricció viscosa del carro (N·s/m)
g = 9.81        # acceleració gravitatòria (m/s²)

# 🔣 Càlcul de l'expressió del denominador comú
alpha = I * (Mc + m) + Mc * m * L**2

# 📐 Matriu A (4x4)
A = np.array([
    [0, 0, 1, 0],
    [0, 0, (m**2)*(L**2)*g / alpha, -(I + m*L**2)*C / alpha],
    [0, 0, 0, 1],
    [0, 0, m*g*L*(Mc + m) / alpha, -m*L*C / alpha]
])

# 🚀 Matriu B (4x1)
B_mat = np.array([
    [0],
    [(I + m*L**2) / alpha],
    [0],
    [m*L / alpha]
])

# (Opcional) Visualitzar en forma de taula
AB_combined = np.hstack([A, B_mat])
columns = ['x', 'theta', 'dx', 'dtheta', 'B']
df = pd.DataFrame(AB_combined, columns=columns)

print("Matriu A:")
print(A)
print("\nMatriu B:")
print(B_mat)
