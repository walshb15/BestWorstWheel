import pygame

class Button:
    def __init__(self, text, pos, size, idleColor, hoverColor, clickColor,
                 font, fontsize, fontcolor):
        self.text = text
        self.position = pos
        self.center = (pos[0] + size[0] / 2, pos[1] + size[1] / 2)
        self.size = size
        self.onPosition = False
        self.iColor = idleColor
        self.hColor = hoverColor
        self.cColor = clickColor
        self.font = pygame.font.SysFont(font, fontsize)
        self.textsurface = self.font.render(self.text, True, fontcolor)
        self.clicked = False

    def draw(self, surface, outline=None):
        if self.clicked:
            pygame.draw.rect(surface, self.cColor, (self.position[0], self.position[1],
                                                        self.size[0], self.size[1]))
        else:
            if self.onPosition:
                pygame.draw.rect(surface, self.hColor, (self.position[0], self.position[1],
                                                        self.size[0], self.size[1]))
            else:
                pygame.draw.rect(surface, self.iColor, (self.position[0], self.position[1],
                                                        self.size[0], self.size[1]))
        textRect = self.textsurface.get_rect()
        textPos = (self.center[0] - textRect.width / 2,
                   self.center[1] - textRect.height / 2)
        surface.blit(self.textsurface, textPos)
        if outline:
            pygame.draw.rect(surface, outline, (self.position[0], self.position[1],
                                                self.size[0], self.size[1]), 2)

    
    def click(self):
        self.clicked = True

    def release(self):
        self.clicked = False

    def mouseHover(self, pos):
        if self.position[0] <= pos[0] and pos[0] <= self.position[0] + self.size[0]:
            if self.position[1] <= pos[1] and pos[1] <= self.position[1] + self.size[1]:
                self.onPosition = True
                return True
        self.onPosition = False
        return False
