from sympy.physics.vector import ReferenceFrame

A = ReferenceFrame("A")
v1 = A.x + A.y
v2 = 2 * A.x + 3 * A.y

print()
