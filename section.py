import pygame
from math import sin, cos, atan2, pi, radians

#This class represents sections on the wheel. They will need to somehow
#dynamically size themselves depending on how many entries there are.

class Section:
    def __init__(self, c, r):
        self.center = c
        self.radius = r

    def draw(self, surface, outline, angle):
        e1 = (self.center[0] + self.radius * cos(angle), self.center[1] + self.radius * sin(-angle))
        e2 = (self.center[0] + self.radius * cos(angle + 33), self.center[1] + self.radius * sin(-angle - 33))
        pygame.draw.line(surface, outline, self.center, e1)
        pygame.draw.line(surface, outline, self.center, e2)
