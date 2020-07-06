import pygame
import time
from button import Button

#Class for a field to input text into. Derived from button
class InputField(Button):
    def __init__(self, pos, size, font, fontsize):
        '''
        Constructor

        pos: The position of the input field (x, y)
        size: The size of the input field (width, height)
        font: The name of the font to use
        fontsize: The size of the font
        '''
        self.position = pos
        self.size = size
        self.center = (pos[0] + size[0] / 2, pos[1] + size[1] / 2)
        self.font = pygame.font.SysFont(font, fontsize)
        self.text = ""
        self.clicked = False
        #This variable tracks how long it has been since the cursor was last shown
        #If we intitialize it to the current time - 2, it will show up right away
        self.cursorTime = time.time() - 2
        self.drawCursor = False
        self.onPosition = False

    def getText(self):
        return self.text

    def clearText(self):
        self.text = ""

    def draw(self, surface):
        '''
        Function to draw the field. This function is a bit messy, so you may
        want to come back and optimize it later.

        surface: The surface to draw to
        '''
        #Text will be drawn with drawn with an offset of 5 to x and y
        textPos = (self.position[0] + 5,
                   self.position[1] + 5)
        #Get current time
        curTime = time.time()
        #Tracker for which text to show
        textBound = 0
        #Loop until you display a small enough number of characters to not overflow
        #the input box
        while True:
            #Add a cursor onto the end of the drawn text
            textsurface = self.font.render((self.text + '_')[textBound::], True, (0, 0, 0))
            textWidth = self.font.size((self.text + '_')[textBound::])[0]
            if textWidth < self.size[0] - 25:
                break
            else:
                textBound += 1
        #If the box is clicked
        if self.clicked:
            #Draw a black outline with a size of 4
            pygame.draw.rect(surface, (0,0,0), (self.position[0], self.position[1],
                                                        self.size[0], self.size[1]), 4)
            #If the cursor is currently being drawn
            if self.drawCursor:
                #Draw to the surface
                surface.blit(textsurface, textPos)
                #If a second has passed, stop showing the cursor
                if curTime - self.cursorTime >= 1:
                    self.drawCursor = False
                #End this function call here
                return
            #If the cursor is not currently being drawn
            else:
                #If two seconds have passed since it was last drawn
                if curTime - self.cursorTime >= 2:
                    #Tell it to draw the cursor again next time
                    self.cursorTime = curTime
                    self.drawCursor = True
        #If the box is not clicked
        else:
            #If the mouse is hovering over the box
            if self.onPosition:
                #Draw a greenish outline instead of black
                pygame.draw.rect(surface, (0,255,85), (self.position[0], self.position[1],
                                                        self.size[0], self.size[1]), 2)
            #Otherwise draw a black outline with size 2
            else:
                pygame.draw.rect(surface, (0,0,0), (self.position[0], self.position[1],
                                                            self.size[0], self.size[1]), 2)
        #Draw text without cursor to the surface
        textsurface = self.font.render(self.text[textBound::], True, (0, 0, 0))
        surface.blit(textsurface, textPos)

    def click(self):
        Button.click(self)
        self.cursorTime = time.time() - 2

    def keyInput(self, k):
        '''
        Function to handle user key input

        k: The unicode for the key pressed
        '''
        #If the key is a backspace, delete the last character in the text
        if k == '\b':
            if len(self.text) > 0:
                self.text = self.text[:-1]
        #If the key is also not enter or tab, add to text
        elif k != '\r' and k != '\t':
            self.text += k
