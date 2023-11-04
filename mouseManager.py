import pygame
from deck import Deck
from circuit import Circuit
from circuit import BOX_WIDTH
from QOperators import * 

class MouseManager:
    def __init__(self, deck: Deck, circuit: Circuit):
        self.gate_selected = False
        self.selected_op = QOperators.NOP
        self.number_selects = 0
        self.deck = deck
        self.circuit = circuit

    def manage(self, pos):
        if not(self.gate_selected):
            for i in self.deck.tiles:
                if i.is_in_tile(pos):
                    self.gate_selected = True
                    i.set_select(True)
                    self.number_selects = NUM_SIGNALS[i.operation]
                    self.selected_op = i.operation
        
        elif self.number_selects > 0:
            found = False
            for i in range(len(self.circuit.boxes)):
                curr = self.circuit.boxes[i]
                if pos[0] > curr.left and pos[0] < (curr.left + curr.width):
                    if pos[1] > curr.top and pos[1] < (curr.top + curr.height):
                        found = True
                        self.number_selects = self.number_selects - 1
                        self.circuit.gates[i] = self.selected_op

            if not(found):
                self.reset()

            if self.number_selects == 0:
                for i in range(len(self.deck.tiles)):
                    if self.deck.tiles[i].selected:
                        self.deck.operators.pop(i)
                        self.deck.set_tiles()
                        break
                        
                self.reset()
                

        print(self.number_selects)
    
    def reset(self):
        for i in self.deck.tiles:
            i.set_select(False)
        self.gate_selected = False
        self.selected_op = QOperators.NOP
        self.number_selects = 0
        

