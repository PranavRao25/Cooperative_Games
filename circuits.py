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


def optimalCHSH():
    epr = QuantumRegister(2, 'epr')
    q = ClassicalRegister(2, 'q')
    a = ClassicalRegister(2, 'a')
    chsh_circ = QuantumCircuit(epr, q, a)

    # Entangled Pair
    chsh_circ.append(bell(), epr)
    chsh_circ.barrier()

    # rotational gates
    with chsh_circ.if_test((q[0], 0)) as else_:  # alice got 0 as question
        chsh_circ.i(0)
    with else_:
        chsh_circ.p(np.pi / 4, 0)

    with chsh_circ.if_test((q[1], 0)) as else_:  # bob got 0 as question
        chsh_circ.p(np.pi / 8, 1)
    with else_:
        chsh_circ.p(-np.pi / 8, 1)

    # measure
    chsh_circ.measure(epr, a)

    return chsh_circ


def chsh(angle):
    epr = QuantumRegister(2, 'epr')
    a = ClassicalRegister(2, 'a')
    chsh = QuantumCircuit(epr, a)

    # Entangled Pair
    chsh.append(bell(), epr)
    chsh.barrier()

    # rotational gates
    chsh.p(angle, 0)

    # measure
    chsh.measure(epr[0], a[0])
    chsh.measure(epr[1], a[1])

    return chsh


def oddCycle(n, qa, qb):
    if n % 2 == 0:
        raise (ValueError('even number'))
    else:
        epr = QuantumRegister(2, 'epr')
        q = ClassicalRegister(n, 'q')
        a = ClassicalRegister(2, 'a')
        angles = []

        odd = QuantumCircuit(epr, q, a)
        odd.append(bell(), epr)
        odd.barrier()

        # rotational gates
        angles.append(((n - 1) * np.pi * qa) / (2 * n) + np.pi / 4 * n)
        angles.append(((n - 1) * np.pi * qb) / (2 * n))

        for i in range(2):
            odd.p(angles[i], epr[i])

        # measure
        for i in range(2):
            odd.measure(epr[i], a[i])

        return odd
