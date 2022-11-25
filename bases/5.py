### udpate():
# velocity.add(acceleration)
# location.add(velocity)

#positive is down/right, negative is up/left
import pygame
import math
from abc import ABC, abstractmethod
from timeit import default_timer as timer

class Vector:
    def __init__(self, x_component, y_component):
        self.x_component = x_component/60
        self.y_component = y_component/60
    
    # def __add__: I think x.add(z) is more descriptive

    def add(self, other_vector):
        self.x_component += other_vector.x_component
        self.y_component += other_vector.y_component

    def multiply_by(self, num):
        self.x_component *= num
        self.y_component *= num

    def __getitem__(self, num):
        if num == 0:
            return self.x_component
        if num == 1:
            return self.y_component


class Force(ABC):
    """ Force vector, and a method to calculate it. """
    @abstractmethod
    def calculate(self):
        pass


class GravityForce(Force, Vector):
    def __init__(self, x_component, y_component):
        super().__init__(x_component, y_component)

    def calculate(self, mass):
        force = mass * 9.8
        return Vector(0, force)


class ElectricForce(Force, Vector):
    def __init__(self, x_component, y_component):
        super().__init__(x_component, y_component)
    
    def calculate(self, d, angle, q1, q2):
        #force = 20
        # I need the angle
        force = 8.9 * math.pow(10, 9) * q1 * q2 / math.pow(d, 2)
        f_y = force * math.sin(angle)
        f_x = force * math.cos(angle)
        return Vector(f_x, f_y)


class ChargedMover:
    def __init__(self, pos_vector, v_vector, a_vector, m, g_force, e_force): # *args = forces acting on the object
        self.pos = pos_vector
        self.v = v_vector
        self.a = a_vector
        self.m = m
        self.g_force = g_force.calculate(m)
        self.e_force = e_force
    
    def update(self, t, d_a, q1, q2):
        # f = self.gravity_force_vector()
        e_force = self.e_force.calculate(d_a[0], d_a[1], q1, q2)
        self.a.x_component = (self.g_force.x_component+e_force.x_component) / self.m
        self.a.y_component = (self.g_force.y_component+e_force.y_component) / self.m

        #self.v.add(self.a) ### HERE YOU MULTIPLY a BY 1
        #self.a.multiply_by(timer()-t)
        self.v.add(self.a)
        self.pos.add(self.v)


class StaticCharge:
    def __init__(self, pos, q):
        self.pos = pos
        self.q = q


def distance_angle(obj1, obj2):
    pos1 = obj1.pos
    pos2 = obj2.pos
    d = math.sqrt(math.pow(pos1[0]-pos2[0], 2) + math.pow(pos1[1]-pos2[1], 2))
    angle = math.asin((pos1[1]-pos2[1])/d)
    return [d, angle]


def draw(bg):
    bg.fill((0,0,0))
    pygame.draw.circle(bg, (255,255,255), (mover.pos.x_component, mover.pos.y_component), 10)
    pygame.draw.circle(bg, (255,255,255), (static_charge.pos.x_component, static_charge.pos.y_component), 8)
    pygame.display.update()

width = 800
height = 400
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
mover = ChargedMover(Vector(60*width/2, 0), Vector(0, 0), Vector(0, 0), 10, GravityForce(0, 0), ElectricForce(0, 0))
static_charge = StaticCharge(Vector(60*width/2, 60*(height-20)), 2*math.pow(10, -2))

t = timer()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    mover.update(t, distance_angle(mover, static_charge), static_charge.q, static_charge.q)
    draw(screen)
