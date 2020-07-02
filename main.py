import pygame
from math import sin, cos, atan2, pi, radians, degrees
from section import Section
from wheel import Wheel
import random

def main():
    pygame.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    white = (255, 255, 255)
    black = (0, 0, 0)
    #movies = ["Troll 2", "The Room", "Miami Connection"]
    movies = ["Troll 2", "The Room", "Miami Connection", "Manos: The Hands of Fate", "Sharknado", "Birdemic", "Ghost Shark"]
    spinning = True
    #Note, display size currently affects how fast the circle spins
    screen = pygame.display.set_mode((700, 700), pygame.HWSURFACE)
    screen.fill(white)
    surface = pygame.display.get_surface()
    width, height = surface.get_size()
    center = (int(width / 2), int(height / 2))
    radius = int(width / 3)
    circumfrence = 2 * radius * pi
    arclen = degrees(circumfrence / len(movies))
    print("CIRCUMFRENCE:", degrees(circumfrence))
    print("ARCLEN:", arclen)
    #Central angle in degrees
    theta = arclen / radius
    chord = 2 * radius * sin(radians(theta) / 2)
    angle = radians(0)
    pygame.display.flip()
    pygame.display.set_caption("Wheel of the Worst!")
    running = True
    wheel = Wheel(center, radius, movies)
    speed = random.randint(10, 50)
    slowdown = random.randint(1, 7) / 1000
    tri_points = [(350, 115), (330, 95), (370, 95)]
    #Game loop
    while running:
        if spinning:
            #Modify the angle so that the sections will rotate
            angle += radians(speed)
            speed -= slowdown
            if (speed <= 0):
                spinning = False
        #Reset the screen
        screen.fill(white)
        pygame.draw.polygon(surface, (255, 0, 0), tri_points, 0)
        #Create and draw a section
        wheel.draw(surface, black, angle, radians(theta))
        #update the display
        pygame.display.update()
        #Handle if the user hits the X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

main()
