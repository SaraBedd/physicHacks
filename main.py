import pygame
from pygame.locals import *
from circuit import Circuit
from deck import Deck
from QOperators import *
from mouseManager import MouseManager
from welcome import *

# Constants
SCREEN_SIZE_X = 1000
SCREEN_SIZE_Y = 700
GAME_NAME = "QWANDLE"

BACKGROUND_COLOR = (50, 50, 50)

HEADER_SIZE_X = SCREEN_SIZE_X
HEADER_SIZE_Y = 100
CIRCUIT_SIZE_X = SCREEN_SIZE_X
CIRCUIT_SIZE_Y = 400
DECK_SIZE_X = SCREEN_SIZE_X
DECK_SIZE_Y = 100

clock = pygame.time.Clock()

pygame.init()
dis = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
pygame.display.set_caption(GAME_NAME)
game_over = False

def run_main_menu():
    main_menu = MainMenu(dis)
    return main_menu.run()

game_started = run_main_menu()

if game_started:
    dis.fill(BACKGROUND_COLOR)
    pygame.display.flip()
    myCircuit = Circuit(4, 4)
    myDeck = Deck([
        QOperators.HADAMARD,
        QOperators.PAULIX,
        QOperators.CNOT,
        QOperators.SWAP,
        QOperators.PAULIZ
    ])

    circRects = myCircuit.get_wire_shapes()
    back = myCircuit.get_background_shape()
    deckRects = myDeck.get_background_shape()
    myDeck.set_tiles()
    boxes_back = myCircuit.get_boxes_back_shape()
    mouseManager = MouseManager(myDeck, myCircuit)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                mouseManager.manage(pos)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mouseManager.reset()

        pygame.draw.rect(dis, (121, 121, 121), back)
        for i in range(len(circRects)):
            pygame.draw.rect(dis, (0, 255, 0), circRects[i])
        pygame.draw.rect(dis, (255, 0, 0), deckRects)
        for i in range(len(myDeck.tiles)):
            myDeck.tiles[i].draw(dis)

        for i in range(len(boxes_back)):
            pygame.draw.rect(dis, (255, 190, 40), boxes_back[i], width=2, border_radius=10)

        myCircuit.draw_boxes(dis)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    quit()
