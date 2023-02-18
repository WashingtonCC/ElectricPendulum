import pygame
import math
from timeit import default_timer as timer

from sympy.physics.vector import ReferenceFrame
from sympy.physics.vector.vector import Vector


width = 800
height = 400
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
t = timer()


A = ReferenceFrame("A")
Q = 2 * math.pow(10, -2)  # charge


class Axis:
    def __init__(self, pos):
        self.pos = pos


# AXIS = Axis(2 * A.x + 2 * A.y)
AXIS = Axis(0 * A.x + 0 * A.y)


class ChargedMover:
    def __init__(self, m, q, pos):
        self.pos = pos
        self.v = 0 * A.x + 0 * A.y
        self.a = 0 * A.x + 0 * A.y
        self.m = m
        self.q = q
        self.Fg = m * (A.x + 9.8 * A.y)

    def get_pos(self):
        self.pos += self.v
        return self.pos

    def get_v(self):
        self.v += self.a
        return self.v

    def _get_Fg_plus_T(self):
        # cos angle(pos, axis) P = T
        resultant = math.sin(self.pos.angle_between(AXIS.pos)) * self.Fg
        return resultant

    def _get_Fe(self, other):
        distance = Vector.magnitude(self.pos - other.pos)
        angle = self.pos.angle_between(other.pos)
        magnitude = 8.9 * math.pow(10, 9) * self.q * other.q / math.pow(distance, 2)
        Fe_y = magnitude * math.sin(angle)
        Fe_x = magnitude * math.cos(angle)
        return Fe_x * A.x + Fe_y * A.y

    def get_a(self, other):
        net_force = self._get_Fg_plus_T() + self._get_Fe(other)
        self.a = net_force / self.m
        return self.a

    def draw(self):
        pygame.draw.lines(
            screen,
            (50, 50, 50),
            False,
            (
                (0, 0),
                (
                    math.floor(self.pos.to_matrix(A)[0]),
                    math.floor(self.pos.to_matrix(A)[1]),
                ),
            ),
        )
        pygame.draw.circle(
            screen,
            (100, 100, 100),
            (
                math.floor(self.pos.to_matrix(A)[0]),
                math.floor(self.pos.to_matrix(A)[1]),
            ),
            17,
        )


class StaticCharge:
    def __init__(self, q, pos):
        self.pos = pos
        self.q = q


charged_mover = ChargedMover(10, Q, A.x + A.y)
static_charge = StaticCharge(Q, 0 * A.x + 3 * A.y)


def update():
    charged_mover.draw()
    pygame.display.update()


while True:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    charged_mover.get_a(static_charge)
    charged_mover.get_v()
    charged_mover.get_pos()
    print(charged_mover.pos)

    screen.fill((255, 255, 255))
    update()
