import pandas as pd
from randomqc import PureRandom
from randomqc.variational import VQE
from randomqc_pytket import PyTKETGates

nb_circuits = 50
nb_gates_runs = 50

circuits = []

# Generating pure random quantum circuits
for i in range(nb_circuits):
    circ = PureRandom()
    circ_sdk = circ.to('pytket')
    circuits.append({
        'circuit_name': circ.name, 
        'nb_qubits': circ.nb_qubits,
        'circuit': circ_sdk,
        'qasm2': circ.to('qasm2'),
    })

# Generating PyTKET gates
for i in range(nb_gates_runs):
    gates = PyTKETGates.get_all()
    for name, circ in gates.items():
        circuits.append({
            'circuit_name': f'PyTKET-{name}', 
            'nb_qubits': circ.n_qubits,
            'circuit': circ,
            'qasm2': '[PYTKET]',
        })

# Generating VQE-type random circuits
for i in range(nb_circuits):
    circ = VQE()
    circ_sdk = circ.to('pytket')
    circuits.append({
        'circuit_name': circ.name, 
        'nb_qubits': circ.nb_qubits,
        'circuit': circ_sdk,
        'qasm2': circ.to('qasm2'),
    })

df = pd.DataFrame(circuits)
df.to_pickle('pytket.pkl')