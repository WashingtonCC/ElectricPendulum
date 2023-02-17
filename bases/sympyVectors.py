from sympy.physics.vector.vector import Vector
from sympy.physics.vector import ReferenceFrame

A = ReferenceFrame("A")

v1 = 2 * A.x
v2 = A.x + A.y

print(v1.angle_between(v2))

print(v1.magnitude)
print(Vector.magnitude(v2))
