import pygame
from pygame import *
from pygame.locals import *

def init(screen):
    display = screen

def newText(text, font, color, x , y):
    screen.blit(font.render(text, True, color),(x, y))