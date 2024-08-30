import pandas as pd

from pytket.extensions.qiskit import qiskit_to_tk
from pytket.extensions.braket import tk_to_braket


from base import PytketToBraketTranspilationEXP

class UsingPyTKET(PytketToBraketTranspilationEXP):
    def __init__(self):
        self.name = 'pytket-braket==0.34.1'
        
    def transpile(self, circuit):
        circ, _, _ =  tk_to_braket(circuit)
        return circ

if __name__ == "__main__":
    initial_circuits = pd.read_pickle('pytket.pkl')
    dftket = UsingPyTKET().run(circuits=initial_circuits, iter=5)
    dftket.to_csv('pytket.csv')