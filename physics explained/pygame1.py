import pygame
import math
#from pygameZoom import PygameZoom


width = 800
height = 400
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pygameZoom = PygameZoom(800, 400)
#pygameZoom.set_background((255, 255, 255))
#pygameZoom.set_zoom_strength(10000)

Q = 2 * 10 ** (-1)
k = 9 * 10 ** (-9)
g = 9.8

# 1 METER = 100PX

l = 2
l0 = 1

q = Q
q0 = Q

t = 0
dt = 0.01

axis = (width/2, 0)


class Bob:
    def __init__(self):
        self.theta = math.pi / 4
        self.thetadt = 0

        self.x = l * math.sin(self.theta)*100 + axis[0]
        self.y = -l * math.cos(self.theta)*100 + axis[1]

        self.m = 0.5
        self.q = Q

    def draw(self):
        pygame.draw.lines(
            screen, (50, 50, 50), False, (axis, (self.x, self.y))
        )
        pygame.draw.circle(
            screen,
            (100, 100, 100),
            (self.x, self.y),
            10,
        )
        pygame.draw.circle(screen, (100,100,100), (axis[0], l*100 + l0*100 + axis[1]), 10,)


def update():
    p.draw()
    # pygameZoom.render(screen, (100, 100))
    pygame.display.update()


p = Bob()

while True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # thetaddt = -g * math.sin(p.theta) / l
    thetaddt = -g * math.sin(p.theta) / l + k * l0 * q * q0 * math.sin(p.theta) / (
       l * p.m * (l**2 - 2 * l * l0 * math.cos(p.theta) + (l + l0) ** 2) ** (3 / 2)
    )
    p.thetadt = p.thetadt + thetaddt * dt
    p.theta = p.theta + p.thetadt * dt

    p.x = l * math.sin(p.theta) * 100 + axis[0]
    p.y = l * math.cos(p.theta) * 100 + axis[1]
    t = t + dt

    #print(p.theta)
    #print(p.x, p.y)
    #print()

    update()
    screen.fill((255, 255, 255))
