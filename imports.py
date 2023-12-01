from qiskit.circuit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.primitives import Estimator, Sampler
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt


def bell():  # creates a bell pair
    epr = QuantumCircuit(2)
    epr.h(0)
    epr.cx(0, 1)
    return epr.to_gate()
