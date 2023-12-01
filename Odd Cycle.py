from imports import *

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
