import pygame
from uteis.style import WHITE

class ConfigTela:
    def configsIniciais(self):
        DISPLAY = pygame.display.set_mode([840, 480])
        pygame.display.set_caption('Ninja 2D')
        DISPLAY.fill(WHITE)

    def __init__(self):
        pygame.init()
        self.configsIniciais()


    DISPLAY = property