import pygame
from QOperators import *

CIRCUIT_TOP = 150
CIRCUIT_LEFT = 200
CIRCUIT_MAX_X = 600
CIRCUIT_MAX_Y = 300
WIRE_WIDTH = 3
BOX_WIDTH = 30
BOX_BACK_WIDTH = 60

class Circuit:
    def __init__(self, n_signals, n_columns):
        self.n_signals = n_signals
        self.n_columns = n_columns
        self.boxes = []
        self.gates = []
        self.set_boxes_shapes()


    def get_background_shape(self):
        return pygame.Rect(CIRCUIT_LEFT, CIRCUIT_TOP, CIRCUIT_MAX_X, CIRCUIT_MAX_Y)
    

    def get_boxes_back_shape(self):
        column_spacer = (BOX_BACK_WIDTH - BOX_WIDTH) / 2
        boxes_back = []
        box_spacing = CIRCUIT_MAX_X / (self.n_columns + 1)
        wire_spacing = CIRCUIT_MAX_Y / (self.n_signals + 1)
        box_back_height = (self.n_signals - 1) * wire_spacing + BOX_WIDTH + 2 * column_spacer 
        for i in range(self.n_columns):
            boxes_back.append(
                pygame.Rect(
                        CIRCUIT_LEFT + (i + 1) * box_spacing - (BOX_BACK_WIDTH / 2),
                        CIRCUIT_TOP + wire_spacing - BOX_WIDTH / 2 - column_spacer,
                        BOX_BACK_WIDTH,
                        box_back_height
                        )
                    )
        return boxes_back


    def set_boxes_shapes(self):
        boxes = []
        box_spacing = CIRCUIT_MAX_X / (self.n_columns + 1)
        wire_spacing = CIRCUIT_MAX_Y / (self.n_signals + 1)
        for i in range(self.n_columns):
            for j in range(self.n_signals):
                boxes.append(
                    pygame.Rect(
                        CIRCUIT_LEFT + (i + 1) * box_spacing  - BOX_WIDTH / 2,
                        CIRCUIT_TOP + (j + 1) * wire_spacing - BOX_WIDTH / 2, 
                        BOX_WIDTH,
                        BOX_WIDTH
                        )
                    )
        self.boxes = boxes
        self.gates = [QOperators.NOP for i in range(len(boxes))]


    def draw_boxes(self, dis):
        for i in range(len(self.boxes)):
            if self.gates[i] == QOperators.NOP:
                pygame.draw.rect(dis, (255, 255, 255), self.boxes[i])
            else:
                pygame.draw.rect(dis, OP_COLOR[self.gates[i]], self.boxes[i])

    def get_wire_shapes(self):
        shapes = []
        wire_spacing = (CIRCUIT_MAX_Y - self.n_signals * WIRE_WIDTH) / (self.n_signals + 1)
        for i in range(self.n_signals):
            shapes.append(
                pygame.Rect(
                    CIRCUIT_LEFT,
                    CIRCUIT_TOP + (i + 1) * wire_spacing + i * WIRE_WIDTH, 
                    CIRCUIT_MAX_X,
                    WIRE_WIDTH
                    )
                )
        return shapes
    