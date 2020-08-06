import pygame

#This class represents buttons that are shown on screen.
class Button:
    def __init__(self, text, pos, size, idleColor, hoverColor, clickColor,
                 font, fontcolor):
        '''
        Constructor

        text: The label for the button
        pos: The position (x, y)
        size: The size (width, height)
        idleColor: The color of the button when not clicked and not hovered
        hoverColor: The color when the mouse is hovering over the button
        clickColor: The color when the button is clicked
        font: The name of the font that will be used
        fontsize: The font size
        fontColor: The color of the font
        '''
        self.text = text
        self.position = pos
        self.center = (pos[0] + size[0] / 2, pos[1] + size[1] / 2)
        self.size = size
        #Variable to check if the mouse is hovering
        self.onPosition = False
        self.iColor = idleColor
        self.hColor = hoverColor
        self.cColor = clickColor
        self.font = font
        self.textsurface = self.font.render(self.text, True, fontcolor)
        #Variable to check if the button has been clicked
        self.clicked = False

    def draw(self, surface, pos, outline=None):
        '''
        Function to draw the button

        surface: The surface to draw the button on
        outline: Color the outline of the button should have (None for no outline)
        pos: The position to draw at
        '''
        self.position = pos
        self.center = (pos[0] + self.size[0] / 2, pos[1] + self.size[1] / 2)
        #IF the button is clicked, draw the button with the clicked color
        if self.clicked:
            pygame.draw.rect(surface, self.cColor, (self.position[0], self.position[1],
                                                        self.size[0], self.size[1]))
        #If the button is not clicked
        else:
            #If the house is hovering, draw hover color
            if self.onPosition:
                pygame.draw.rect(surface, self.hColor, (self.position[0], self.position[1],
                                                        self.size[0], self.size[1]))
            #Not clicked and not hovering, draw idle color
            else:
                pygame.draw.rect(surface, self.iColor, (self.position[0], self.position[1],
                                                        self.size[0], self.size[1]))
        #Dimensions/position to center the text
        textRect = self.textsurface.get_rect()
        textPos = (self.center[0] - textRect.width / 2,
                   self.center[1] - textRect.height / 2)
        #Draw text to the surface
        surface.blit(self.textsurface, textPos)
        #If there is an outline, draw it
        if outline:
            pygame.draw.rect(surface, outline, (self.position[0], self.position[1],
                                                self.size[0], self.size[1]), 2)

    
    def click(self):
        self.clicked = True

    def release(self):
        self.clicked = False

    def isClicked(self):
        return self.clicked

    def mouseHover(self, pos):
        '''
        Function to check if the mouse is hovering over the button

        pos: The position of the mouse
        '''
        #Check if the mouse position is within the bounds of the button
        if self.position[0] <= pos[0] and pos[0] <= self.position[0] + self.size[0]:
            if self.position[1] <= pos[1] and pos[1] <= self.position[1] + self.size[1]:
                #Return true if yes
                self.onPosition = True
                return True
        self.onPosition = False
        return False
