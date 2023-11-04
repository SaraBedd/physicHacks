import pygame
from circuit import Circuit
from deck import Deck

# Constants
SCREEN_SIZE_X = 1000
SCREEN_SIZE_Y = 700
GAME_NAME = "QWANDLE"

HEADER_SIZE_X = SCREEN_SIZE_X
HEADER_SIZE_Y = 100
CIRCUIT_SIZE_X = SCREEN_SIZE_X
CIRCUIT_SIZE_Y = 400
DECK_SIZE_X = SCREEN_SIZE_X
DECK_SIZE_Y = 100

pygame.init()
dis=pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
pygame.display.update()
pygame.display.set_caption(GAME_NAME)
game_over=False

myCircuit = Circuit(5, 4, [], [])
myDeck = Deck(["ok", "hey", "lol"])
circRects = myCircuit.get_wire_shapes()
back = myCircuit.get_background_shape()
deckRects = myDeck.get_background_shape()
myDeck.set_tiles()




while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    
    pygame.draw.rect(dis, (121, 121, 121), back)
    for i in range(len(circRects)):
        pygame.draw.rect(dis, (0, 255, 0), circRects[i])
    pygame.draw.rect(dis, (255, 0, 0), deckRects)
    for i in range(len(myDeck.tiles)):
        myDeck.tiles[i].draw(dis)
    pygame.display.flip()
 
pygame.quit()
quit()