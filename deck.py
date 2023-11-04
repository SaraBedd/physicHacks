import pygame 
from tile import Tile
from QOperators import *

DECK_TOP = 550
DECK_LEFT = 50
DECK_WIDTH = 900
DECK_HEIGHT = 100

TILE_SIZE = 80

class Deck:
    def __init__(self, operators):
        self.operators = operators
        self.tiles = []

    def get_background_shape(self):
        return pygame.Rect(DECK_LEFT, DECK_TOP, DECK_WIDTH, DECK_HEIGHT)
    
    def set_tiles(self):
        tile_spacing = (DECK_WIDTH - len(self.operators) * TILE_SIZE) / (len(self.operators) + 1)
        self.tiles.clear()
        for i in range(len(self.operators)):
            self.tiles.append(Tile(self.operators[i], 
                                   [
                                       DECK_LEFT + (i + 1) * tile_spacing + i * TILE_SIZE,
                                       DECK_TOP + (DECK_HEIGHT - TILE_SIZE) / 2
                                   ]
                                   ))
            

    
