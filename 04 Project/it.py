import sympy as sp

# Define symbols
s, t = sp.symbols('s t')

# Define system parameters
m = 2  # Mass (kg)
b = 0.5  # Damping coefficient (Ns/m)
k = 4  # Spring constant (N/m)
F = 4 / (s**2 + 4**2)  # Laplace transform of external force F(t)

# Laplace transform of the equation of motion
X = sp.Function('X')(s)
eqn = m * s**2 * X + b * s * X + k * X - F

# Solve for X(s)
X_s = sp.solve(eqn, X)[0]

# Inverse Laplace transform to find displacement x(t) in time domain
x_t = sp.inverse_laplace_transform(X_s, s, t)
x_t_simplified = sp.simplify(x_t)

# Display the displacement expression
print("Displacement (in meters) as a function of time:")
print(x_t_simplified)
