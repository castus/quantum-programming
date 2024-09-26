from qiskit_braket_provider import BraketLocalBackend
qpu_backend = BraketLocalBackend()

def run(qc, shots=100):
    qpu_task = qpu_backend.run(qc, shots=shots)
    data = qpu_task.result()
    print(data.get_counts())
    return qpu_task
