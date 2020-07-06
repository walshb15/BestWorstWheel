import pygame
from math import sin, cos, atan2, pi, radians, degrees
from section import Section
from wheel import Wheel
from button import Button
from inputfield import InputField
import random
import sqlite3

def main():
    pygame.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    white = (255, 255, 255)
    black = (0, 0, 0)
    movies = ["Who Killed Captain Alex", "Killer Bean Forever", "Backstroke of the West", "Shriek of the Mutilated"]
    #movies = ["Troll 2", "The Room", "Miami Connection"]
    #movies = ["Troll 2", "The Room", "Miami Connection", "Manos: The Hands of Fate", "Sharknado", "Birdemic", "Ghost Shark"]
    running = True
    spinning = False
    #Note, display size currently affects how fast the circle spins
    screen = pygame.display.set_mode((700, 700), pygame.HWSURFACE)
    screen.fill(white)
    surface = pygame.display.get_surface()
    width, height = surface.get_size()
    center = (int(width / 2), int(height / 2))
    radius = int(width / 3)
    circumfrence = 2 * radius * pi
    if len(movies) > 0:
        arclen = degrees(circumfrence / len(movies))
    else:
        arclen = 360
    #Central angle in degrees
    theta = arclen / radius
    chord = 2 * radius * sin(radians(theta) / 2)
    #The current angle of rotation
    angle = radians(0)
    pygame.display.flip()
    pygame.display.set_caption("Wheel of the Worst!")
    wheel = Wheel(center, radius, movies)
    speed = random.randint(10, 50)
    slowdown = random.randint(1, 7) / 1000
    #Points of the arrow that will point to the winning item
    tri_points = [(350, 115), (330, 95), (370, 95)]
    #Spin button
    spinButton = Button("SPIN", (width-125, 25), (100, 50), (0, 255, 0),
                        (247, 255, 5), (0, 135, 23), "Comic Sans MS", 30, black)
    textInputer = InputField((center[0]-150, height-75), (300, 50), "Comic Sans MS", 30)
    #Game loop
    while running:
        mousePos = pygame.mouse.get_pos()
        if spinning and len(movies) > 0:
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
        #Draw the buttons
        spinButton.draw(surface, black)
        textInputer.draw(surface)
        #update the display
        pygame.display.update()
        #Handle if the user hits the X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEMOTION:
                spinButton.mouseHover(mousePos)
                textInputer.mouseHover(mousePos)
            #If the user clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #If the user clicked while hovering over the button
                if spinButton.mouseHover(mousePos):
                    spinButton.click()
                    angle = radians(0)
                    speed = random.randint(10, 50)
                    slowdown = random.randint(1, 7) / 1000
                    spinning = True
                if textInputer.mouseHover(mousePos):
                    textInputer.click()
                else:
                    textInputer.release()
            #Change the color of buttons back when mouse is released
            if event.type == pygame.MOUSEBUTTONUP:
                spinButton.release()
            if event.type == pygame.KEYDOWN:
                if textInputer.isClicked():
                    textInputer.keyInput(event.unicode)

main()
