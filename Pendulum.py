import pygame
import math
pygame.init()
pygame.display.set_caption("Double Pendulum Simulation")
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width,screen_height])
screen.fill([255,255,255])

clock = pygame.time.Clock()
crashed = False
white = [255,255,255]
black = [0,0,0]
red = [255,0,0]
blue = [0,0,255]
"""Pendulum Variables"""
origin = (300,300)
p1, p2 = (0,0)
r1, r2 = 100, 100
m1, m2 = 10, 10
ang1, ang2 = 0, 0
a1vel, a2vel = 0, 0
a1accel, a2accel = 0, 0
g = 1
paths1, paths2 = [], []

pygame.draw.circle(screen, black, origin, 5)
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            origin = (pygame.mouse.get_pos())
        if event.type == pygame.QUIT:
            crashed = True
    """Calculating x and y cordinates for both objects"""
    x1 = int(r1 * math.sin(ang1))
    y1 = int(r1 * math.cos(ang1))
    x2 = int(r2 * math.sin(ang2))
    y2 = int(r2 * math.cos(ang2))
    object1 = (origin[0] + x1, origin[1] + y1)
    object2 = (object1[0] + x2, object1[1] + y2)
    """Equations for Velocity and Acceleration"""
    a1vel += a1accel
    a2vel += a2accel
    ang1 += a1vel
    ang2 += a2vel
    a1vel = a1vel * 0.999
    a2vel = a2vel * 0.999

    """Combining equations for the Equation of Motion for object 1"""
    eqp1 = -g * (2 * m1 + m2) * math.sin(ang1)
    eqp2 = -m2 * g * math.sin(ang1 - 2 * ang2)
    eqp3 = -2 * math.sin(ang1-ang2) * m2
    eqp4 = (a2vel**2) * r2 + (a1vel**2) * r1 * math.cos(ang1 - ang2)
    eqden = r1 * (2 * m1 + m2 - m2 * math.cos(2 * ang1 - 2 * ang2))
    a1accel = (eqp1 + eqp2 + (eqp3 * eqp4)) / eqden
    """Combining Equations for the equation of motion for object 2"""
    eqp5 = 2 * math.sin(ang1-ang2)
    eqp6 = (a1vel**2) * r1 * (m1+m2)
    eqp7 = g * (m1 + m2) * math.cos(ang1)
    eqp8 = (a2vel**2) * r2 * m2 * math.cos(ang1-ang2)
    eqden2 = r2*(2*m1 + m2 - m2*math.cos(2*ang1 - 2*ang2))
    a2accel = eqp5 * (eqp6 + eqp7 +eqp8) / eqden2
    paths1.append(object1)
    paths2.append(object2)
    for dot in paths1:
        pygame.draw.circle(screen, black, dot, 1)
    for dot in paths2:
        pygame.draw.circle(screen, red, dot, 1)
    pygame.draw.line(screen, black, origin, object1, 3)
    pygame.draw.line(screen, black, object1, object2, 3)
    pygame.draw.circle(screen, red, object1, m1)
    pygame.draw.circle(screen, red, object2, m2)
    if len(paths1) >= 300:
        paths1.remove(paths1[0])
    if len(paths2) >= 300:
        paths2.remove(paths2[0])
    pygame.display.update()
    screen.fill(white)

    clock.tick(60)


pygame.quit()
quit()