from sympy.physics.vector import ReferenceFrame
from sympy.physics.vector.vector import Vector


A = ReferenceFrame("A")
v1 = A.x + A.y
v2 = 5 * A.x + 3 * A.y

print(v2.to_matrix(A)[0])
