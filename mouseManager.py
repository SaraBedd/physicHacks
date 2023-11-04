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
        self.modified_gates = []

    def manage(self, pos):
        if not(self.gate_selected):
            for i in range(len(self.circuit.boxes)):
                curr = self.circuit.boxes[i]
                if pos[0] > curr.left and pos[0] < (curr.left + curr.width):
                    if pos[1] > curr.top and pos[1] < (curr.top + curr.height):
                        if self.circuit.gates[i] != QOperators.NOP:
                            self.deck.operators.append(self.circuit.gates[i])
                            self.deck.set_tiles()
                            self.circuit.gates[i] = QOperators.NOP
                            for x in range(len(self.circuit.boxes)):
                                if self.circuit.boxes[x].left == curr.left:
                                    self.circuit.gates[x] = QOperators.NOP
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
                        if self.circuit.gates[i] != QOperators.NOP:
                            break
                        if len(self.modified_gates) > 0:
                            if curr.left != self.modified_gates[-1].left:
                                self.undo_change()
                                break
                        for x in range(len(self.circuit.boxes)):
                            if self.circuit.boxes[x].left == curr.left:
                                if self.circuit.gates[x] != QOperators.NOP and self.circuit.gates[x] != self.selected_op:
                                    self.undo_change()
                                    return
                        found = True
                        self.number_selects = self.number_selects - 1
                        self.circuit.gates[i] = self.selected_op
                        self.modified_gates.append(curr)

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

    
    def undo_change(self):
        for i in self.modified_gates:
            for j in range(len(self.circuit.boxes)):
                if i.left == self.circuit.boxes[j].left and i.top == self.circuit.boxes[j].top:
                    self.circuit.gates[j] = QOperators.NOP
        self.reset()
    
    def reset(self):
        for i in self.deck.tiles:
            i.set_select(False)
        self.gate_selected = False
        self.selected_op = QOperators.NOP
        self.number_selects = 0
        self.modified_gates.clear()
        

