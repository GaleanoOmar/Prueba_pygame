import pygame
import sys

from pygame.constants import QUIT

#Inicializar
pygame.init()

#crear la pantalla
screen = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()