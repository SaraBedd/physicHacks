import pygame
from circuit import Circuit
from deck import Deck


class Level:
    def __init__(self, inputs, outputs, gates, nb_columns):
        self.inputs = inputs
        self.outputs = outputs
        self.gates = gates
        self.nb_columns = nb_columns

        self.circuit = Circuit(len(self.inputs), self.nb_columns)
        self.deck = Deck(gates)

