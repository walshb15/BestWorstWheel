import pygame
from math import sin, cos, atan2, pi, radians, degrees
from section import Section
from wheel import Wheel


def main():
    pygame.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    white = (255, 255, 255)
    black = (0, 0, 0)
    textsurface = myfont.render("Troll 2", False, black)
    rotsurface = textsurface
    #movies = ["Troll 2", "The Room", "Miami Connection"]
    movies = ["Troll 2", "The Room", "Miami Connection", "Manos: The Hands of Fate", "Sharknado", "Birdemic"]
    spinning = True
    #Note, display size currently affects how fast the circle spins
    screen = pygame.display.set_mode((700, 700), pygame.HWSURFACE)
    screen.fill(white)
    surface = pygame.display.get_surface()
    width, height = surface.get_size()
    center = (int(width / 2), int(height / 2))
    textrect = textsurface.get_rect()
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
        #textRot = center
        if spinning:
            #Modify the angle so that the sections will rotate
            angle += radians(0.1)
            #rotsurface = pygame.transform.rotozoom(textsurface, degrees(angle), 1)
            rotsurface, textrect = rotate(textsurface, angle, center)
        #Reset the screen
        screen.fill(white)
        #Create and draw a section
        wheel.draw(surface, black, angle, radians(theta))
        #textsurface = myfont.render("WHEEL OF THE WORST!", False, (0, 0, 0))
        #screen.blit(rotsurface,(center[0] - textrect.width / 2, center[1] - textrect.height / 2))
        meme = textrect.topleft
        e1 = (meme[0] + (radius / 2) * cos(angle + radians(theta)), meme[1] + (radius / 2) * sin(-angle - radians(theta)))
        screen.blit(rotsurface, e1)
        #update the display
        pygame.display.update()
        #Handle if the user hits the X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

def rotate(surface, a, pos):
    '''
    Function to rotate a surface in a centered manner at a
    specified position
    
    surface: the surface to rotate
    a: The angle to rotate by
    pos: The position to rotate at
    '''
    angle = degrees(a)
    rotated_offset.rotate(angle)
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=pos)
    return rotated_surface, rotated_rect

main()
