import pygame
from math import sin, cos, atan2, pi, radians
from section import Section

#This class draws the wheel and sets up all the sections
class Wheel:
    def __init__(self, c, r, items):
        self.center = c
        self.radius = r
        self.sections = list()
        self.items = items
        for i in self.items:
            newSection = Section(i, self.center, self.radius, len(self.items))
            self.sections.append(newSection)

    def addItem(self, i):
        newSection = Section(i, self.center, self.radius, len(self.items))
        self.sections.append(newSection)

    def draw(self, surface, outline, angle, dist):
        '''
        Draw the circle that will house the sections

        surface: The surface to draw to
        outline: What color the circle should be
        angle: The current angle of rotation for the wheel
        dist: The angle that represents the distance between sections
        '''
        pygame.draw.circle(surface, outline, self.center, self.radius, 1)
        if len(self.items) > 0:
            for num, i in enumerate(self.items):
                if len(self.items) > 1:
                    e1 = (self.center[0] + self.radius * cos(angle + dist * num), self.center[1] + self.radius * sin(-angle - dist * num))
                    pygame.draw.line(surface, outline, self.center, e1)
                self.sections[num].draw(surface, angle, dist, num)
