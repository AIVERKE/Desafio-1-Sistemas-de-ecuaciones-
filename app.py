import numpy as np

# Matriz de coeficientes
A = np.array([[0.52, 0.30, 0.18],
              [0.20, 0.50, 0.30],
              [0.25, 0.20, 0.55]])

# Vector de resultados
B = np.array([4800, 5810, 5690])

# Cálculo de la inversa de la matriz A
A_inv = np.linalg.inv(A)

# Multiplicación de la inversa por el vector de resultados para obtener las cantidades
X = np.dot(A_inv, B)

print("La cantidad de metros cúbicos a transportar desde cada cantera es:")
print(f"Cantera 1: {X[0]:.2f} m³")
print(f"Cantera 2: {X[1]:.2f} m³")
print(f"Cantera 3: {X[2]:.2f} m³")
