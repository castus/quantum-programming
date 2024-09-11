from qiskit_braket_provider import BraketLocalBackend
qpu_backend = BraketLocalBackend()

def run(qc):
    qpu_task = qpu_backend.run(qc, shots=100)
    data = qpu_task.result()
    print(data.get_counts())
