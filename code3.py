from randomqc_qiskit import QiskitGates

qiskit_qcs = QiskitGates.get_all()
print(len(qiskit_qcs))
# Outputs:
# 102

# print(qiskit_qcs.keys())
# Outputs:
# dict_keys(['C3XGate', 'C3SXGate', 'C4XGate', 'CCXGate', 'DCXGate', 'CHGate', 'CPhaseGate', 'CRXGate', 'CRYGate', 'CRZGate', 'CSGate', 'CSdgGate', 'CSwapGate', 'CSXGate', 'CUGate', 'CU1Gate', 'CU3Gate', 'CXGate', 'CYGate', 'CZGate', 'CCZGate', 'ECRGate', 'HGate', 'IGate', 'PhaseGate', 'RCCXGate', 'RC3XGate', 'RGate', 'RXGate', 'RXXGate', 'RYGate', 'RYYGate', 'RZGate', 'RZZGate', 'XXMinusYYGate', 'XXPlusYYGate', 'SGate', 'SdgGate', 'SwapGate', 'iSwapGate', 'SXGate', 'SXdgGate', 'TGate', 'TdgGate', 'UGate', 'U1Gate', 'U2Gate', 'U3Gate', 'XGate', 'YGate', 'ZGate', 'QFT', 'AND', 'OR', 'XOR', 'InnerProduct', 'NLocal', 'TwoLocal', 'RealAmplitudes', 'EfficientSU2', 'ExcitationPreserving', 'QAOAAnsatz', 'PauliFeatureMap', 'ZFeatureMap', 'ZZFeatureMap', 'StatePreparation', 'Diagonal', 'MCMT', 'MCMTVChain', 'Permutation', 'PermutationGate', 'GMS', 'GR', 'GRX', 'GRY', 'GRZ', 'MCPhaseGate', 'MCXGate', 'MCXGrayCode', 'MCXRecursive', 'MCXVChain', 'RVGate', 'LinearAmplitudeFunction', 'LinearPauliRotations', 'PolynomialPauliRotations', 'PiecewiseLinearPauliRotations', 'DraperQFTAdder', 'CDKMRippleCarryAdder', 'WeightedAdder', 'IntegerComparator', 'QuadraticForm', 'ExactReciprocal', 'FourierChecking', 'GraphState', 'HiddenLinearFunction', 'IQP', 'QuantumVolume', 'PhaseEstimation', 'GroverOperator', 'PhaseOracle', 'EvolvedOperatorAnsatz', 'PauliEvolutionGate'])

# print(qiskit_qcs['ZZFeatureMap'])
# Sample Output:
# <qiskit.circuit.quantumcircuit.QuantumCircuit at 0x7f7b81690712>