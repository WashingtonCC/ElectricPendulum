### udpate():
# velocity.add(acceleration)
# location.add(velocity)

#positive is down/right, negative is up/left
import pygame
import math
from abc import ABC, abstractmethod

class Vector:
    def __init__(self, x_component, y_component):
        self.x_component = x_component
        self.y_component = y_component
    
    # def __add__: I think x.add(z) is more descriptive

    def add(self, other_vector):
        self.x_component += other_vector.x_component
        self.y_component += other_vector.y_component


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


class Mover:
    def __init__(self, pos_vector, v_vector, a_vector, m, g_force): # *args = forces acting on the object
        self.pos = pos_vector
        self.v = v_vector
        self.a = a_vector
        self.m = m
        self.g_force = g_force.calculate(m)
    
    def update(self):
        # f = self.gravity_force_vector()
        self.a.x_component = self.g_force.x_component / self.m
        self.a.y_component = self.g_force.y_component / self.m

        self.v.add(self.a)

        self.pos.add(self.v)

    def draw(self, bg):
        bg.fill((0,0,0))
        pygame.draw.circle(bg, (255,255,255), (self.pos.x_component, self.pos.y_component), 10)
        pygame.display.update()


width = 800
height = 400
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
mover = Mover(Vector(width/2, 0), Vector(0, 0), Vector(0, 0), 10, GravityForce(0, 0)) # THE MASS DOES NOT AFFECT THE SPEED (MOVEMENT) HERE, WHICH IS ABSOLUTELLY RIGHT. (F = ma)

while True:
    clock.tick(1) # IT WORKS WITH 1 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    mover.update()
    mover.draw(screen)