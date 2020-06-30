import pygame
from math import sin, cos, atan2, pi, radians, degrees

def rotate(surface, a, pos):
    '''
    Function to rotate a surface in a centered manner at a
    specified position
    
    surface: the surface to rotate
    a: The angle to rotate by
    pos: The position to rotate at
    '''
    angle = degrees(a)
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=pos)
    return rotated_surface, rotated_rect

#This class represents each slice of the wheel.
class Section:
    def __init__(self, text, c, r):
        self.name = text
        self.center = c
        self.radius = r
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.textsurface = self.font.render(self.name, False, (0, 0, 0))

    #Function to draw the text for this section in the appropriate spot
    def draw(self, surface, angle, theta, offset):
        rotsurface, textrect = rotate(self.textsurface, angle, self.center)
        place = textrect.topleft
        e1 = (place[0] + (self.radius / 2) * cos(angle + (0.5 + offset) * theta),
              place[1] + (self.radius / 2) * sin(-angle - (0.5 + offset) * theta))
        surface.blit(rotsurface, e1)
