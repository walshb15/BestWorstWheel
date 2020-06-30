import pygame
from math import sin, cos, atan2, pi, radians
from section import Section

#This class draws the wheel and sets up all the sections
class Wheel:
    def __init__(self, c, r, i):
        self.center = c
        self.radius = r
        self.sections = list()
        self.items = i
        for i in self.items:
            newSection = Section(i, self.center, self.radius)
            self.sections.append(newSection)

    def draw(self, surface, outline, angle, dist):
        #Draw the circle that will house the sections
        pygame.draw.circle(surface, outline, self.center, self.radius, 1)
        #TEST LINE
        #self.sections[0].draw(surface, angle, dist, 3.5)
        for num, i in enumerate(self.items):
            e1 = (self.center[0] + self.radius * cos(angle + dist * num), self.center[1] + self.radius * sin(-angle - dist * num))
            pygame.draw.line(surface, outline, self.center, e1)
            self.sections[num].draw(surface, angle, dist, num)
