from enum import Enum

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