from randomqc import PureRandom

qc1 = PureRandom(nb_qubits=2, nb_gates=4)
qc2 = PureRandom()
qcs = PureRandom.range_gates(2, 2, 101)
tket1 = qc1.to('pytket')
print(tket1)
# Sample Output:
# [Sdg q[0]; T q[1]; CZ q[0], q[1]; CY q[1], q[0]; ]

tket2 = qcs[3].to('pytket') 
print(tket2)
# Sample Output:
# [T q[0]; X q[1]; U1(1.46706) q[1]; CRy(0.374142) q[0], q[1]; ]