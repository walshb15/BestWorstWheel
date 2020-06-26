import pygame
from math import sin, cos, atan2, pi, radians, degrees
from section import Section


def main():
    pygame.init()
    movies = ["Troll 2", "The Room", "Miami Connection"]
    spinning = False
    screen = pygame.display.set_mode((700, 700))
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)
    surface = pygame.display.get_surface()
    width, height = surface.get_size()
    center = (int(width / 2), int(height / 2))
    radius = int(width / 3)
    circumfrence = 2 * radius * pi
    arclen = degrees(circumfrence / len(movies))
    #Central angle in degrees
    theta = arclen / radius
    chord = 2 * radius * sin(radians(theta) / 2)
    print("Theta:", theta)
    print("Chord:", chord)
    print("Diameter:", radius*2)
    angle = radians(0)
    pygame.display.flip()
    pygame.display.set_caption("Wheel of the Worst!")
    running = True
    #Game loop
    while running:
        if spinning:
            #Modify the angle so that the sections will rotate
            angle += radians(0.1)
        #Reset the screen
        screen.fill(white)
        #Draw the circle that will house the sections
        pygame.draw.circle(surface, black, center, radius, 1)
        #Create and draw a section
        testSection = Section(center, radius)
        testSection.draw(surface, black, angle, chord)
        #update the display
        pygame.display.update()

        #Handle if the user hits the X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

main()
