import pygame
from math import sin, cos, atan2, pi, radians, degrees
from section import Section
from wheel import Wheel
from button import Button
from inputfield import InputField
import random
import sqlite3

def updateWheelSize(screen):
    '''
    Function to update variables relating to the size of the wheel

    screen: The screen which you will use to get the size and calculate
        its center
    '''
    width, height = screen.get_size()
    center = (int(width / 2), int(height / 2))
    radius = int(width / 3)
    circumfrence = 2 * radius * pi
    return width, height, center, radius, circumfrence

def updateCalculations(movies, circumfrence, radius):
    '''
    Function to calculate the arc length, angle between wheel items,
    and the chord length between the items on the wheel.

    movies: The list of items to use
    circumfrence: The circumfrence of the circle
    radius: The radius of the circle
    '''
    if len(movies) > 0:
        arclen = degrees(circumfrence / len(movies))
    else:
        arclen = 360
    #Central angle in degrees
    theta = arclen / radius
    chord = 2 * radius * sin(radians(theta) / 2)
    return arclen, theta, chord

def getFromDatabase(connection):
    '''
    Function to get the items stored in the databse

    connection: The SQLite connection to pull from

    returns: A list of values from the database
    '''
    return list(connection.execute("SELECT title FROM movies;"))

def addToDatabase(connection, item):
    '''
    Function to add an item to the database

    connection: SQLite connection to use
    item: The item to add to the table
    '''
    connection.execute("INSERT INTO movies (title) VALUES (?);", (item,))
    connection.commit()

def deleteFromDatabase(connection, item):
    '''
    Function to delete an item from the database

    connection: The SQLite connection to use
    item: The item to delete from the table
    '''
    connection.execute('''DELETE FROM movies WHERE title = (?);''', (item,))
    connection.commit()
    
def main():
    #SQLite connection
    conn = sqlite3.connect("./wheel.db")
    #conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    #Create table to hold the items if one does not already exist.
    #Prevent it from accepting duplicate titles
    c.execute('''CREATE TABLE IF NOT EXISTS movies(title TEXT,
                    CONSTRAINT no_duplicates UNIQUE (title));''')
    pygame.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    white = (255, 255, 255)
    black = (0, 0, 0)
    #Grab the items currently in the database
    movies = getFromDatabase(conn)
    print("MOVIES:", movies)
    running = True
    spinning = False
    #Note, display size currently affects how fast the circle spins
    screen = pygame.display.set_mode((700, 700), pygame.HWSURFACE|pygame.RESIZABLE)
    screen.fill(white)
    surface = pygame.display.get_surface()
    width, height, center, radius, circumfrence = updateWheelSize(screen)
    #Perform initial circle calculations
    arclen, theta, chord = updateCalculations(movies, circumfrence, radius)
    #The current angle of rotation
    angle = radians(0)
    pygame.display.flip()
    pygame.display.set_caption("Wheel of the Worst!")
    wheel = Wheel(center, radius, movies)
    speed = random.randint(10, 50)
    slowdown = random.randint(1, 7) / 1000
    print("SPEED:", speed)
    print("SLOWDOWN:", slowdown)
    #Spin button
    spinButton = Button("SPIN", (width-125, 25), (100, 50), (0, 255, 0),
                        (247, 255, 5), (0, 135, 23), "Comic Sans MS", 30, black)
    textInputer = InputField((center[0]-150, height-75), (300, 50), "Comic Sans MS", 30)
    addButton = Button("Add Item", (center[0] + 175, height-75), (125, 50), (0, 255, 0),
                       (247, 255, 5), (0, 135, 23), "Comic Sans MS", 20, black)
    delButton = Button("Delete Item", (center[0] - 300, height-75), (125, 50), (255, 0, 0),
                       (247, 255, 5), (128, 0, 0), "Comic Sans MS", 20, black)
    #Game loop
    while running:
        #Points of the arrow that will point to the winning item
        tri_points = [(center[0], center[1] - radius - 10),
                       (center[0] - 10, center[1] - radius - 30),
                       (center[0] + 10, center[1] - radius - 30)]
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
        #Draw the wheel and the sections within it
        wheel.draw(surface, black, angle, radians(theta))
        #Draw the buttons
        spinButton.draw(surface, (width-125, 25), black)
        addButton.draw(surface, (center[0] + 175, height-75), black)
        delButton.draw(surface, (center[0] - 300, height-75) ,black)
        textInputer.draw(surface, (center[0]-150, height-75))
        #update the display
        pygame.display.update()
        #Handle user events such as key presses or clicks
        for event in pygame.event.get():
            #Handle if the user hits the X button
            if event.type == pygame.QUIT:
                conn.close()
                pygame.quit()
                running = False
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.HWSURFACE|pygame.RESIZABLE)
                width, height, center, radius, circumfrence = updateWheelSize(screen)
                arclen, theta, chord = updateCalculations(movies, circumfrence, radius)
                wheel.setCenter(center)
                wheel.setRadius(radius)
            #If the user is moving the mouse around, check
            #if they are hovering over any of the buttons
            if event.type == pygame.MOUSEMOTION:
                spinButton.mouseHover(mousePos)
                addButton.mouseHover(mousePos)
                delButton.mouseHover(mousePos)
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
                    print("ANGLE:", angle)
                    print("SPEED:", speed)
                    print("SLOWDOWN:", slowdown)
                if addButton.mouseHover(mousePos):
                    addButton.click()
                    addText = textInputer.getText()
                    #If the add text is not just whitespace, add it
                    if addText.strip() != "":
                        try:
                            addToDatabase(conn, addText)
                            movies.clear()
                            movies += getFromDatabase(conn)
                            arclen, theta, chord = updateCalculations(movies, circumfrence, radius)
                            wheel.addItem(movies[-1])
                            textInputer.clearText()
                        except sqlite3.IntegrityError:
                            #Item already exists in the table
                            print("Already in table")
                            pass
                if delButton.mouseHover(mousePos):
                    delButton.click()
                    remText = textInputer.getText()
                    #If the remove text is not just whitespace, remove it
                    if remText.strip() != "":
                        deleteFromDatabase(conn, remText)
                        movies.clear()
                        movies += getFromDatabase(conn)
                        arclen, theta, chord = updateCalculations(movies, circumfrence, radius)
                        wheel.deleteItem(remText)
                        textInputer.clearText()
                if textInputer.mouseHover(mousePos):
                    textInputer.click()
                else:
                    #Release the text inputer if the user clicked anywhere
                    #outside of it
                    textInputer.release()
            #Change the color of buttons back when mouse is released
            if event.type == pygame.MOUSEBUTTONUP:
                spinButton.release()
                addButton.release()
                delButton.release()
            #Key events
            if event.type == pygame.KEYDOWN:
                #if the user pressed a key while the text inputer is active
                if textInputer.isClicked():
                    #Input that key
                    textInputer.keyInput(event.unicode)

main()
