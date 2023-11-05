from enum import Enum
import pygame
import os

class QOperators(Enum):
    HADAMARD = 1
    PAULIX = 2
    PAULIY = 3
    PAULIZ = 4
    SWAP = 5
    TOFFOLI = 6
    CNOT = 7
    NOP = 8

NUM_SIGNALS = {
    QOperators.HADAMARD : 1,
    QOperators.PAULIX : 1,
    QOperators.PAULIY : 1,
    QOperators.PAULIZ : 1,
    QOperators.SWAP : 2,
    QOperators.TOFFOLI : 3,
    QOperators.CNOT : 2
    }

OP_COLOR = {
    QOperators.HADAMARD : (125, 132, 145),
    QOperators.PAULIX : (125, 132, 80),
    QOperators.PAULIY : (125, 50, 145),
    QOperators.PAULIZ : (179, 132, 145),
    QOperators.SWAP : (124, 12, 15),
    QOperators.TOFFOLI : (125, 200, 145),
    QOperators.CNOT : (75, 132, 15)
}

OP_ICON = {
    QOperators.HADAMARD : "hadamard_icon.png",
    QOperators.PAULIX : "pauli_x_icon.png",
    QOperators.PAULIY : "pauli_y_icon.png",
    QOperators.PAULIZ : "pauli_z_icon.png",
    QOperators.SWAP : "swap_icon.png",
    QOperators.TOFFOLI : "toffoli_icon.png",
    QOperators.CNOT : "controlled_not_icon.png"
}

OP_ICON_IMAGE = {
    QOperators.HADAMARD : pygame.image.load(os.path.join('assets/icons', OP_ICON[QOperators.HADAMARD])),
    QOperators.PAULIX : pygame.image.load(os.path.join('assets/icons', OP_ICON[QOperators.PAULIX])),
    QOperators.PAULIY : pygame.image.load(os.path.join('assets/icons', OP_ICON[QOperators.PAULIY])),
    QOperators.PAULIZ : pygame.image.load(os.path.join('assets/icons', OP_ICON[QOperators.PAULIZ])),
    QOperators.SWAP : pygame.image.load(os.path.join('assets/icons', OP_ICON[QOperators.SWAP])),
    QOperators.TOFFOLI : pygame.image.load(os.path.join('assets/icons', OP_ICON[QOperators.TOFFOLI])),
    QOperators.CNOT : pygame.image.load(os.path.join('assets/icons', OP_ICON[QOperators.CNOT])),
    20 : pygame.image.load(os.path.join('assets/icons', "O_full_icon.png")),
    21 : pygame.image.load(os.path.join('assets/icons', "O_empty_icon.png")),
    22 : pygame.image.load(os.path.join('assets/icons', "X_icon.png")),

}

TRANSLATE = {
    QOperators.HADAMARD : "SNOT",
    QOperators.PAULIX : "X",
    QOperators.PAULIY : "Y",
    QOperators.PAULIZ : "Z",
    QOperators.SWAP : "SWAP",
    QOperators.TOFFOLI : "TOFFOLI",
    QOperators.CNOT : "CNOT"
}

def get_icon(op, number):
    if op == QOperators.HADAMARD:
        return OP_ICON_IMAGE[QOperators.HADAMARD]
    elif op == QOperators.PAULIX:
        return OP_ICON_IMAGE[QOperators.PAULIX]
    elif op == QOperators.PAULIY:
        return OP_ICON_IMAGE[QOperators.PAULIY]
    elif op == QOperators.PAULIZ:
        return OP_ICON_IMAGE[QOperators.PAULIZ]
    elif op == QOperators.CNOT:
        if number == 1:
            return OP_ICON_IMAGE[20]
        elif number == 2: 
            return OP_ICON_IMAGE[21]
    elif op == QOperators.SWAP:
        return OP_ICON_IMAGE[22]
    elif op == QOperators.TOFFOLI:
        if number == 1:
            return OP_ICON_IMAGE[20]
        elif number == 2:
            return OP_ICON_IMAGE[20]
        elif number == 3:
            return OP_ICON_IMAGE[21]
