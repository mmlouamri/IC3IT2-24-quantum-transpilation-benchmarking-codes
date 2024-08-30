from benchmarq.transpilation import TranspilationExperiment

# Utility function that check that two unitaries (np.array) are equal up to global phase
from benchmarq.transpilation import assert_allclose_up_to_global_phase

# Utility functions that transform an SDK circuits to a unitary (np.array) 
from benchmarq.transpilation.sdk_utility import pytket_to_unitary, braket_to_unitary 

# Utility functions that calculates the Depth and Gatecount for Pytket and Braket circuits respectively
from benchmarq.transpilation.sdk_utility import pytket_depth, pytket_gatecount, braket_depth, braket_gatecount 
    
class PytketToBraketTranspilationEXP(TranspilationExperiment):
    def check(self, circuit_pytket, circuit_braket):
        try:
           assert_allclose_up_to_global_phase(pytket_to_unitary(circuit_pytket), 
                                              braket_to_unitary(circuit_braket), 
                                              atol=1e-7)
           return 1

        except Exception as e:
            print(e)
            return 0
        
    def metrics(self):
        return {
            'depth': [pytket_depth, braket_depth],
            'gatecount': [pytket_gatecount, braket_gatecount]
        }