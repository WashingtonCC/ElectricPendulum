import pygame
import math


width = 800
height = 400
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

Q = 10 ** (3.517)
k = 9 * 10 ** (-9)
g = 9.8

# 1 METER = 400PX
scale = 400

axis = (width/2, 100)
radius = 5

l = .4
l0 = .1

q = Q
q0 = Q

t = 0
dt = 0.01

theta0 = math.pi/6

class Bob:
    def __init__(self):
        self.theta = theta0
        self.thetadt = 0

        self.x = l * math.sin(self.theta)*scale + axis[0]
        self.y = -l * math.cos(self.theta)*scale + axis[1]

        self.m = .005
        self.q = Q

    def draw(self):
        pygame.draw.lines(
            screen, (50, 50, 50), False, (axis, (self.x, self.y))
        )
        pygame.draw.circle(
            screen,
            (100, 100, 100),
            (self.x, self.y),
            radius,
        )
        pygame.draw.circle(screen, (100,100,100), (axis[0], l*scale + l0*scale + axis[1]), radius,)


def update():
    p.draw()
    # pygameZoom.render(screen, (100, 100))
    pygame.display.update()


def render_info(text, position):
    font = pygame.font.SysFont("Arial", 16, True, False)
    surface = font.render(text, True, (0,0,0))
    screen.blit(surface, position)


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

    p.x = l * math.sin(p.theta) * scale + axis[0]
    p.y = l * math.cos(p.theta) * scale + axis[1]
    t = t + dt

    render_info(f"Initial distance between bodies: {l0} m", [10, 10])
    render_info(f"Pendulum length: {l} m", [10, 30])
    render_info("Charge of each body: {:e} C".format(Q), [10, 50])
    render_info(f"theta: {round(p.theta*180/math.pi)} º", [10, 70])
    render_info(f"Initial theta: {round(theta0*180/math.pi)} º", [10, 90])
    render_info(f"Mass: {p.m} kg", [10, 110])
    render_info(f"Scale: 1m = {scale} px", [10, 150])

    update()
    screen.fill((255, 255, 255))
