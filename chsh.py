from imports import *

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
