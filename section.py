import pygame
from math import sin, cos, atan2, pi, radians, degrees, log

def rotate(surface, a, pos, diff, offset):
    '''
    Function to rotate a surface in a centered manner at a
    specified position
    
    surface: the surface to rotate
    a: The angle to rotate by
    pos: The position to rotate at
    diff: The difference in arc length between each section
    offset: The current section it is currently in (0 to n sections)
    '''
    angle = degrees(a) + degrees(diff) / 2 * (1 + offset*2) + 180
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=pos)
    return rotated_surface, rotated_rect

#This class represents the elemenets inside each slice of the wheel.
class Section:
    def __init__(self, text, c, r, wheel):
        #The text is contained in a tuple due to the parametrized
        #query. Just pull out the data from that tuple at the 0 index
        self.name = text[0]
        self.center = c
        self.radius = r
        #Number of sections
        self.wheel = wheel
        textlen = len(text)
        fontsize = 18
        self.font = pygame.font.SysFont('Comic Sans MS', fontsize)
        self.textsurface = self.font.render(self.name, True, (0, 0, 0))

    def __repr__(self):
        return self.name

    def getName(self):
        return self.name

    #Function to draw the text for this section in the appropriate spot
    def draw(self, surface, angle, theta, offset):
        '''
        Function to draw the section and the text within it

        surface: The surface to draw to
        angle: The current angle of rotation for the wheel
        theta: The angle in radians between each section
        offset: The current section we are on (0 to n sections)
        '''
        center = self.wheel.getCenter()
        radius = self.wheel.getRadius()
        rotsurface, textrect = rotate(self.textsurface, angle, center, theta, offset)
        place = textrect.topleft
        e1 = (place[0] + (radius / 2) * cos(angle + (0.5 + offset) * theta),
              place[1] + (radius / 2) * sin(-angle - (0.5 + offset) * theta))
        #If there is more than one section, draw the text in the middle of each section
        if (self.wheel.getSectionCount() > 1):
            surface.blit(rotsurface, e1)
        #If there is only one section, draw the text at the center of the wheel
        else:
            surface.blit(rotsurface, (center[0] - textrect.width / 2,
                                      center[1] - textrect.height / 2))
