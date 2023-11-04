import pygame

TILE_SIZE_X = 80
TILE_SIZE_Y = 80

class Tile:
    def __init__(self, operation, pos):
        self.operation = operation
        self.pos = pos

    def draw(self, dis):
        pygame.draw.rect(dis, (0, 0, 255), pygame.Rect(
            self.pos[0],
            self.pos[1],
            TILE_SIZE_X,
            TILE_SIZE_Y
        ))
    
    def move(self, pos):
        self.pos = pos