import pygame
from pygame.locals import *
from circuit import Circuit
from deck import Deck
from QOperators import *
from mouseManager import MouseManager
from welcome import *
from level import Level

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

def draw_beveled_rect(surface, rect, color, bevel_amount):
    pygame.draw.rect(surface, color, rect)
    highlight_color = [min(c + bevel_amount, 255) for c in color]
    shadow_color = [max(c - bevel_amount, 0) for c in color]

    pygame.draw.polygon(surface, highlight_color, [
        rect.topleft, rect.topright,
        (rect.topright[0], rect.topright[1] + bevel_amount),
        (rect.topleft[0], rect.topleft[1] + bevel_amount)
    ])

    pygame.draw.polygon(surface, highlight_color, [
        rect.topleft, rect.bottomleft,
        (rect.bottomleft[0] + bevel_amount, rect.bottomleft[1]),
        (rect.topleft[0] + bevel_amount, rect.topleft[1])
    ])

    pygame.draw.polygon(surface, shadow_color, [
        rect.bottomleft, rect.bottomright,
        (rect.bottomright[0], rect.bottomright[1] - bevel_amount),
        (rect.bottomleft[0], rect.bottomleft[1] - bevel_amount)
    ])

    pygame.draw.polygon(surface, shadow_color, [
        rect.topright, rect.bottomright,
        (rect.bottomright[0] - bevel_amount, rect.bottomright[1]),
        (rect.topright[0] - bevel_amount, rect.topright[1])
    ])

def run_main_menu():
    main_menu = MainMenu(dis)
    return main_menu.run()

game_started = run_main_menu()

if game_started:
    level = Level([[0.7, 0.7], [0, 1], [1, 0], [1, 0]], [[1, 0], [1, 0], [1, 1], [0, 1]], [
        QOperators.HADAMARD,
        QOperators.PAULIX,
        QOperators.CNOT,
        QOperators.SWAP,
        QOperators.PAULIZ,
        QOperators.TOFFOLI
    ], 3)

    dis.fill(BACKGROUND_COLOR)
    pygame.display.flip()
    myCircuit = level.circuit
    myDeck = level.deck
    

    circRects = myCircuit.get_wire_shapes()
    back = myCircuit.get_background_shape()
    deckRects = myDeck.get_background_shape()
    myDeck.set_tiles()
    boxes_back = myCircuit.get_boxes_back_shape()
    mouseManager = MouseManager(level)
    

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
        deck_color = (50, 50, 50)
        bevel_amount = 5
        draw_beveled_rect(dis, deckRects, deck_color, bevel_amount)
        for i in range(len(myDeck.tiles)):
            myDeck.tiles[i].draw(dis)

        for i in range(len(boxes_back)):
            pygame.draw.rect(dis, (255, 190, 40), boxes_back[i], width=2, border_radius=10)

        myCircuit.draw_boxes(dis)
        level.draw_inputs(dis)
        level.draw_outputs(dis)
        
        for i in range(len(level.lines)):
            pygame.draw.rect(dis, (0, 0, 0), level.lines[i])
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    quit()
