import pygame
from pygame.locals import *

import math

def display(screen, width, height):
    """
    Displays an X and Y axis on the surface provided, in white.
    Also displays two 45deg lines in an X shape through the centre of the
    axes.
    """
    centre = (width/2, height/2)
    pygame.draw.line(screen, pygame.Color(255, 255, 255), 
            (width/2, 0), (width/2, height), 1)
    pygame.draw.line(screen, pygame.Color(255, 255, 255),
            (0, height/2), (width, height/2), 1)
    pygame.draw.line(screen, pygame.Color(255, 0, 255),
            (centre[0]-width/4, centre[1]-width/4), 
            (centre[0]+width/4, centre[1]+width/4), 1)
    pygame.draw.line(screen, pygame.Color(255, 0, 255),
            (centre[0]+width/4, centre[1]-width/4),
            (centre[0]-width/4, centre[1]+width/4), 1)
