import pygame
from circuit import Circuit
from circuit import BOX_WIDTH
from deck import Deck
import os
from QOperators import *

INPUT_SIZE = 40

INPUTS_TOP = 150
INPUTS_LEFT = 100
INPUTS_MAX_X = 100
INPUTS_MAX_Y = 300

ACTUAL_OUT_TOP = 150
ACTUAL_OUT_LEFT = 700
ACTUAL_OUT_MAX_X = 100
ACTUAL_OUT_MAX_Y = 300

EXPECTED_OUT_TOP = 150
EXPECTED_OUT_LEFT = 900
EXPECTED_OUT_MAX_X = 100
EXPECTED_OUT_MAX_Y = 300


class Level:
    def __init__(self, inputs, outputs, gates, nb_columns):
        self.inputs = inputs
        self.outputs = outputs
        self.gates = gates
        self.nb_columns = nb_columns
        self.actual_outputs = self.inputs

        self.circuit = Circuit(len(self.inputs), self.nb_columns)
        self.deck = Deck(gates)
        self.zero_icon = pygame.transform.scale(pygame.image.load(os.path.join('assets/icons', "0_icon.png")), (INPUT_SIZE, INPUT_SIZE))
        self.one_icon = pygame.transform.scale(pygame.image.load(os.path.join('assets/icons', "1_icon.png")), (INPUT_SIZE, INPUT_SIZE))
        self.lines = []

    
    def draw_inputs(self, dis):
        input_spacing = INPUTS_MAX_Y / (len(self.inputs) + 1)
        for i in range(len(self.inputs)):
            icon = ''
            if self.inputs[i] == [1, 0]:
                icon = self.zero_icon
            elif self.inputs[i] == [0, 1]: 
                icon = self.one_icon

            dis.blit(icon, pygame.Rect(
            INPUTS_LEFT + INPUTS_MAX_X / 2 - INPUT_SIZE / 2,
            INPUTS_TOP + (i + 1) * input_spacing - INPUT_SIZE / 2,
            INPUT_SIZE,
            INPUT_SIZE
        ))
            
    def draw_outputs(self, dis):
        input_spacing = INPUTS_MAX_Y / (len(self.outputs) + 1)
        for i in range(len(self.outputs)):
            icon = ''
            if self.outputs[i] == [1, 0]:
                icon = self.zero_icon
            elif self.outputs[i] == [0, 1]: 
                icon = self.one_icon

            dis.blit(icon, pygame.Rect(
            EXPECTED_OUT_LEFT + EXPECTED_OUT_MAX_X / 2 - INPUT_SIZE / 2,
            EXPECTED_OUT_TOP + (i + 1) * input_spacing - INPUT_SIZE / 2,
            INPUT_SIZE,
            INPUT_SIZE
        ))
            
    def generate_output(self):
        output = []
        output.append(self.inputs)
        output.append([])
        for i in range(len(self.circuit.orders)):
            if self.circuit.orders[i] == 1:
                output[1].append([self.circuit.gates[i].name, [i % len(self.inputs)]])
        
        for i in range(len(self.circuit.orders)):
            if self.circuit.orders[i] == 2:
                name = self.circuit.gates[i].name
                for x in output[1]:
                    if x[0] == name:
                        x[1].append(i % len(self.inputs))
        
        for i in range(len(self.circuit.orders)):
            if self.circuit.orders[i] == 3:
                name = self.circuit.gates[i].name
                for x in output[1]:
                    if x[0] == name:
                        x[1].append(i % len(self.inputs))
        self.generate_lines()
        print(output)

            
    def generate_lines(self):
        self.lines = []
        for i in range(len(self.circuit.gates)):
            if self.circuit.gates[i] != QOperators.NOP:
                pos = self.circuit.boxes[i].left
                for j in range(len(self.circuit.gates)):
                    if i != j and self.circuit.boxes[j].left == pos:
                        if self.circuit.gates[j] != QOperators.NOP:
                            top = self.circuit.boxes[j].top
                            bottom = self.circuit.boxes[i].top
                            if i < j: 
                                top = self.circuit.boxes[i].top
                                bottom = self.circuit.boxes[j].top
                            
                            self.lines.append(pygame.Rect(
                                pos + BOX_WIDTH / 2,
                                top + BOX_WIDTH / 2,
                                1,
                                bottom - top
                                ))
            


        


    

