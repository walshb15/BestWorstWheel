import pygame
from math import sin, cos, atan2, pi, radians, degrees
from section import Section
from wheel import Wheel


def main():
    pygame.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render("WHEEL OF THE WORST!", False, (0, 0, 0))
    #movies = ["Troll 2", "The Room", "Miami Connection"]
    movies = ["Troll 2", "The Room", "Miami Connection", "Manos: The Hands of Fate", "Sharknado", "Birdemic"]
    spinning = True
    #Note, display size currently affects how fast the circle spins
    screen = pygame.display.set_mode((700, 700), pygame.HWSURFACE)
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
    wheel = Wheel(center, radius, movies)
    #Game loop
    while running:
        textsurface = myfont.render("WHEEL OF THE WORST!", False, (0, 0, 0))
        if spinning:
            #Modify the angle so that the sections will rotate
            angle += radians(0.1)
            textsurface = pygame.transform.rotate(textsurface, degrees(angle))
        #Reset the screen
        screen.fill(white)
        #Create and draw a section
        wheel.draw(surface, black, angle, radians(theta))
        #textsurface = myfont.render("WHEEL OF THE WORST!", False, (0, 0, 0))
        screen.blit(textsurface,center)
        #update the display
        pygame.display.update()
        #Handle if the user hits the X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
main()
