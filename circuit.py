import pygame

CIRCUIT_TOP = 150
CIRCUIT_LEFT = 200
CIRCUIT_MAX_X = 600
CIRCUIT_MAX_Y = 300
WIRE_WIDTH = 3
BOX_WIDTH = 80

class Circuit:
    def __init__(self, n_signals, n_columns, inputs, outputs):
        self.n_signals = n_signals
        self.n_columns = n_columns
        self.boxes = []

    def get_background_shape(self):
        return pygame.Rect(CIRCUIT_LEFT, CIRCUIT_TOP, CIRCUIT_MAX_X, CIRCUIT_MAX_Y)
    

    def get_boxes_shapes(self):
        boxes = []
        box_spacing = (CIRCUIT_MAX_X - self.n_columns * BOX_WIDTH) / (self.n_columns + 1)
        for i in range(self.n_columns):
            for j in range(self.n_signals):
                boxes.append(
                    pygame.Rect(
                        CIRCUIT_LEFT + (i + 1) * box_spacing + i * BOX_WIDTH,
                        CIRCUIT_TOP + (j + 1) * box_spacing, 
                        BOX_WIDTH,
                        BOX_WIDTH
                        )
                    )
        return boxes




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

    
    


        