import pygame
from math import sin, cos, atan2, pi, radians

#This class represents each slice of the wheel.
class Section:
    def __init__(self, text, c, r):
        self.name = text
        self.center = c
        self.radius = r

    #Function to draw the text for this section in the appropriate spot
    def draw(self):
        pass
