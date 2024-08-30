from randomqc import VQE

qc3 = VQE()
tket3 = qc3.to('pytket')
print(tket3)
# Sample Output:
# [Rx(0.501217) q[0]; Rx(1.88348) q[1]; Ry(1.63825) q[0]; Ry(1.90287) q[1]; CX q[0], q[1]; Rx(1.68886) q[0]; Rx(0.516951) q[1]; Ry(0.82392) q[0]; Ry(0.584921) q[1]; CX q[0], q[1]; Rx(0.73289) q[0]; Rx(0.46376) q[1]; Ry(0.686261) q[0]; Ry(0.292793) q[1]; H q[0]; ]

qc4 = VQE(nb_qubits=2, nb_su2_gates=1, entanglement='linear', reps=3)
tket4 = qc4.to('pytket')
print(tket4)
# Sample Output:
# [Rx(1.17985) q[0]; Rx(1.59042) q[1]; CX q[0], q[1]; Rx(0.986453) q[0]; Rx(0.260294) q[1]; CX q[0], q[1]; Rx(0.781044) q[0]; Rx(1.19931) q[1]; CX q[0], q[1]; Rx(1.46526) q[0]; Rx(1.31492) q[1]; ]