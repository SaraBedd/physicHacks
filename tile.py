import pygame
from QOperators import *
import os

TILE_SIZE_X = 80
TILE_SIZE_Y = 80
BORDER_WIDTH = 4

class Tile:
    def __init__(self, operation, pos):
        self.operation = operation
        self.pos = pos
        self.selected = False
        self.icon = pygame.transform.scale(pygame.image.load(os.path.join('assets/icons', OP_ICON[self.operation])), (TILE_SIZE_X, TILE_SIZE_Y))


    def draw(self, dis):
        if self.selected:
            pygame.draw.rect(dis, (0, 0, 255), pygame.Rect(
                self.pos[0] - BORDER_WIDTH,
                self.pos[1] - BORDER_WIDTH,
                TILE_SIZE_X + 2 * BORDER_WIDTH,
                TILE_SIZE_Y + 2 * BORDER_WIDTH
            ), width=BORDER_WIDTH)
        
        dis.blit(self.icon, pygame.Rect(
            self.pos[0],
            self.pos[1],
            TILE_SIZE_X,
            TILE_SIZE_Y
        ))

    def is_in_tile(self, pos):
        if pos[0] > self.pos[0] and pos[0] < (self.pos[0] + TILE_SIZE_X):
            if pos[1] > self.pos[1] and pos[1] < (self.pos[1] + TILE_SIZE_Y):
                return True
        return False
    
    def set_select(self, val):
        self.selected = val

    
    def move(self, pos):
        self.pos = pos