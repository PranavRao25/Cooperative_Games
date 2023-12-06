from imports import *

"""
    We calculate the total 
"""

def angleRange(the1, the2):  # create a parameterization of angles that will violate the inequality
    return [[i] for i in np.linspace(the1, the2, 1024)]


angle = angleRange(0, 2*np.pi)
obsv = SparsePauliOp(['XX']) - SparsePauliOp(['XZ']) + SparsePauliOp(['ZX']) + SparsePauliOp(['ZZ'])  # create operator for chsh witness
thetha = Parameter('θ')

epr = QuantumRegister(2, 'epr')
qc = QuantumCircuit(epr)
qc.append(bell(), epr)
qc.ry(thetha, 1)
# qc.draw('mpl')

estimator1 = Estimator()
job = estimator1.run([qc]*len(angle), observables=[obsv]*len(angle), parameter_values=angle)
exps1 = job.result().values

plt.plot(angle, exps1, marker='x', ls='-', color='green')
plt.plot(angle, [2]*len(angle), ls='--', color='red', label='Classical Bound')
plt.plot(angle, [-2]*len(angle), ls='--', color='red')
plt.xlabel('angle (rad)')
plt.ylabel('CHSH Witness')
plt.legend(loc=4)
