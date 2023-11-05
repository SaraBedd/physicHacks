import numpy as np
from numpy import pi
from qutip import Qobj, about, basis, tensor
from qutip_qip.circuit import QubitCircuit
from qutip_qip.operations import (Gate, berkeley, cnot, cphase, csign, fredkin,
                                  gate_sequence_product, globalphase, iswap,
                                  molmer_sorensen, phasegate, qrot, rx, ry, rz,
                                  snot, sqrtiswap, sqrtnot, sqrtswap, swap,
                                  swapalpha, toffoli)
from qutip.qip.circuit import CircuitSimulator
from sympy import Rational, sqrt


def output_list(input_qubit, gates):

    def quantum_object_data_to_nice_object_quantum_data(N, data_to_be_analysed_yeah):
        output_list = []
        for i in range(len(data_to_be_analysed_yeah)):
            binary_representation = bin(data_to_be_analysed_yeah[i][0])
            binary_representation = str(binary_representation[2:]).zfill(N)
            output_list.append((binary_representation, data_to_be_analysed_yeah[i][1]))


        return output_list
    
    N = len(input_qubit)

    q = QubitCircuit(N, reverse_states=False)
    
    for operator in gates:
        if len(operator[1]) > 1:
            if operator[0] == "SWAP":
                q.add_gate(operator[0], targets = operator[1])
            else:
                q.add_gate(operator[0], targets = operator[1][-1], controls = operator[1][:-1])
        else:  
            q.add_gate(operator[0], targets = operator[1])

    basis_states = []
    for qubit in input_qubit:
        basis_states.append(qubit[0]*basis(2,0)+qubit[1]*basis(2,1))
    zero_state = tensor(basis_states)

    result = q.run(state = zero_state)

    non_zero_elements = [(i, value) for i, sublist in enumerate(result) for j, sublist_value in enumerate(sublist) if (value := sublist_value[0]) != 0.0]

    output = quantum_object_data_to_nice_object_quantum_data(N, non_zero_elements)

    output_dict = {}
    output_dict_coef = {}
    for qubits, coefficient in output:
        for i, qubit_value in enumerate(qubits):
            qubit_key = "Qubit {}".format(i + 1)
            coefficient_key = "Qubit_coefficient {}".format(i + 1)
            if qubit_key not in output_dict:
                output_dict[qubit_key] = []
                output_dict_coef[coefficient_key] = []
        
            output_dict[qubit_key].append(int(qubit_value))
            output_dict_coef[coefficient_key].append(coefficient)

    for index_qubit, key in enumerate(output_dict):

        if set(output_dict[key]) == {0}:
            output_dict[key] = [1,0]
        elif set(output_dict[key]) == {1}:
            output_dict[key] = [0,1]
        else:
            coefficient_0 = 0
            coefficient_1 = 0
            for index_coeff, i in enumerate(output_dict[key]):
                qubit_coefficient_key = "Qubit_coefficient {}".format(index_qubit + 1)
                if i == 0:
                    coefficient_0 = coefficient_0 + (output_dict_coef[qubit_coefficient_key][i])**2
                else: 
                    coefficient_1 = coefficient_1 + (output_dict_coef[qubit_coefficient_key][i])**2
            coefficient_0 = np.sqrt(coefficient_0)
            coefficient_1 = np.sqrt(coefficient_1)

            output_dict[key] = [coefficient_0, coefficient_1]
        
    return output_dict
   
test = output_list([[1,0],[1,0], [0,1], [1/np.sqrt(2),1/np.sqrt(2)]],[["SNOT", [0]], ["X", [0]], ["SWAP", [0,1]]])

print(test)