import pygame
import math
import random

"""Colors"""
white = [255,255,255]
black = [0,0,0]
red = [255,0,0]
blue = [0,0,255]
green = [0,255,0]

"""Initializing and setup pygame"""
pygame.init()
pygame.display.set_caption("Double Pendulum Simulation")
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width,screen_height])
screen.fill(white)
pygame.display.update()
myFont = pygame.font.SysFont("comicsansms",20)
text = myFont.render("Click to Start",1,black)
pygame.draw.circle(screen, black, (300,300), 5)
screen.blit(text, (250, 70))

clock = pygame.time.Clock()
clock.tick(0)
crashed = False
start = False

"""Pendulum Variables"""
"""Changeable Variables"""
origin = (300,300)
r1, r2 = 100, 100
m1, m2 = 10, 10
g = 1
ang1, ang2 = random.uniform(0,2*math.pi) , random.uniform(0,2*math.pi)

"""Do not Change"""
a1vel, a2vel = 0, 0
a1accel, a2accel = 0, 0
paths1, paths2 = [], []

"""Calculating initial x and y coordinates for both objects"""
x1 = int(r1 * math.sin(ang1))
y1 = int(r1 * math.cos(ang1))
x2 = int(r2 * math.sin(ang2))
y2 = int(r2 * math.cos(ang2))
object1 = [origin[0] + x1, origin[1] + y1]
object2 = [object1[0] + x2, object1[1] + y2]

"""Drawing function"""
def draw(list1, list2, color1, color2, color3, color4, object1pos, object2pos, mass1, mass2):
    for dots in list1:
        pygame.draw.circle(screen, color1, dots, 1)
    for dots in list2:
        pygame.draw.circle(screen, color2, dots, 1)
    pygame.draw.line(screen, color3, origin, object1pos, 3)
    pygame.draw.line(screen, color3, object1pos, object2pos, 3)
    pygame.draw.circle(screen, color4, object1pos, mass1)
    pygame.draw.circle(screen, color4, object2pos, mass2)
    pygame.display.update()

draw(paths1,paths2,blue,green,black,red,object1,object2,m1,m2)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = True
        if event.type == pygame.QUIT:
            crashed = True
    if not start:
        continue
    else:
        clock.tick(60)
        """Calculating x and y coordinates for both objects"""
        x1 = int(r1 * math.sin(ang1))
        y1 = int(r1 * math.cos(ang1))
        x2 = int(r2 * math.sin(ang2))
        y2 = int(r2 * math.cos(ang2))
        object1 = [origin[0] + x1, origin[1] + y1]
        object2 = [object1[0] + x2, object1[1] + y2]

        """Equations for Velocity and Acceleration"""
        a1vel += a1accel
        a2vel += a2accel
        ang1 += a1vel
        ang2 += a2vel

        """Can introduce a slight reduction to act as air resistance"""
        """
        a1vel = a1vel * 0.999
        a2vel = a2vel * 0.999
        """

        """Combining equations for the Equation of Motion for object 1"""
        eqp1 = -g * (2 * m1 + m2) * math.sin(ang1)
        eqp2 = -m2 * g * math.sin(ang1 - 2 * ang2)
        eqp3 = -2 * math.sin(ang1 - ang2) * m2
        eqp4 = (a2vel ** 2) * r2 + (a1vel ** 2) * r1 * math.cos(ang1 - ang2)
        eqden = r1 * (2 * m1 + m2 - m2 * math.cos(2 * ang1 - 2 * ang2))
        a1accel = (eqp1 + eqp2 + (eqp3 * eqp4)) / eqden

        """Combining Equations for the equation of motion for object 2"""
        eqp5 = 2 * math.sin(ang1 - ang2)
        eqp6 = (a1vel ** 2) * r1 * (m1 + m2)
        eqp7 = g * (m1 + m2) * math.cos(ang1)
        eqp8 = (a2vel ** 2) * r2 * m2 * math.cos(ang1 - ang2)
        eqden2 = r2 * (2 * m1 + m2 - m2 * math.cos(2 * ang1 - 2 * ang2))
        a2accel = eqp5 * (eqp6 + eqp7 + eqp8) / eqden2

        """Removes clutter from excessive trailing dots"""
        paths1.append(object1)
        paths2.append(object2)
        if len(paths1) >= 300:
            paths1.remove(paths1[0])
        if len(paths2) >= 300:
            paths2.remove(paths2[0])

        """Calls Draw Function"""
        draw(paths1,paths2,blue,green,black,red,object1,object2,m1,m2)

        """Updates Frames"""
        pygame.display.update()
        screen.fill(white)

pygame.quit()
quit()