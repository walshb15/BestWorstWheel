import pygame
from math import sin, cos, atan2, pi, radians


def main():
    screen = pygame.display.set_mode((700, 700))
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)
    surface = pygame.display.get_surface()
    width, height = surface.get_size()
    center = (int(width / 2), int(height / 2))
    radius = int(width / 3)
    circle = pygame.draw.circle(surface, black, center, radius, 1)
    angle = radians(0)
    endPoint = (center[0] + radius * cos(angle), center[1] + radius * sin(-angle))
    line = pygame.draw.line(surface, black, center, endPoint)
    pygame.display.flip()
    pygame.display.set_caption("Wheel of the Worst!")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

main()
