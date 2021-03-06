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
            newSection = Section(i, self.center, self.radius, self)
            self.sections.append(newSection)

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius

    def setCenter(self, c):
        self.center = c

    def setRadius(self, r):
        self.radius = r

    def getSectionCount(self):
        '''
        Function to get the number of sections on the wheel
        '''
        return len(self.sections)

    def addItem(self, i):
        '''
        Function to add a new section to the wheel

        i: The item title to add to the new section
        '''
        newSection = Section(i, self.center, self.radius, self)
        self.sections.append(newSection)

    def deleteItem(self, item):
        '''
        Function to delete the section that contains a given item

        item: The item to delete
        '''
        toDelete = -1
        for num, j in enumerate(self.sections):
            if j.getName() == item:
                toDelete = num
        if toDelete >= 0:
            self.sections.pop(toDelete)

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
