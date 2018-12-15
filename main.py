import os, sys
import pygame
from pygame.locals import *

WINDOWSIZE = (650, 600)
FPS = 60        # frames per second
YELLOW = (255, 255, 0)

if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

pygame.init()

wSurface = pygame.display.set_mode (WINDOWSIZE, 0, 32)
pygame.display.set_caption ("Pacman")