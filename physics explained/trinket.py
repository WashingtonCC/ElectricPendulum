import sympy as sp

t, l, m, g = sp.symbols("t l m g")
theta = sp.symbols("theta", cls=sp.Function)

theta = theta(t)
print(theta)
