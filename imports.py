from qiskit.circuit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit.primitives import Estimator, Sampler
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit import Parameter
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background') # optional


def bell():  # creates a bell pair
    epr = QuantumCircuit(2)
    epr.h(0)
    epr.cx(0, 1)
    return epr.to_gate()
