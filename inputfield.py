import pygame
import time
from button import Button

class InputField(Button):
    def __init__(self, pos, size, font, fontsize):
        self.position = pos
        self.size = size
        self.center = (pos[0] + size[0] / 2, pos[1] + size[1] / 2)
        self.font = pygame.font.SysFont(font, fontsize)
        self.text = "TEST"
        self.clicked = False
        self.cursorTime = time.time() - 2
        self.drawCursor = False
        self.onPosition = False

    def getText(self):
        return self.text

    def draw(self, surface):
        textPos = (self.position[0] + 5,
                   self.position[1] + 5)
        curTime = time.time()
        if self.clicked:
            pygame.draw.rect(surface, (0,0,0), (self.position[0], self.position[1],
                                                        self.size[0], self.size[1]), 4)
            if self.drawCursor:
                textsurface = self.font.render(self.text + '_', True, (0, 0, 0))
                surface.blit(textsurface, textPos)
                if curTime - self.cursorTime >= 1:
                    self.drawCursor = False
                return
            else:
                if curTime - self.cursorTime >= 2:
                    self.cursorTime = curTime
                    self.drawCursor = True
        else:
            if self.onPosition:
                pygame.draw.rect(surface, (0,255,85), (self.position[0], self.position[1],
                                                        self.size[0], self.size[1]), 2)
            else:
                pygame.draw.rect(surface, (0,0,0), (self.position[0], self.position[1],
                                                            self.size[0], self.size[1]), 2)
        textsurface = self.font.render(self.text, True, (0, 0, 0))
        surface.blit(textsurface, textPos)

    def click(self):
        Button.click(self)
        self.cursorTime = time.time() - 2

    def keyInput(self, k):
        if k == '\b':
            if len(self.text) > 0:
                self.text = self.text[:-1]
        else:
            self.text += k
