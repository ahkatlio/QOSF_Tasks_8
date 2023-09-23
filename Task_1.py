from math import gcd
from qiskit import QuantumCircuit, Aer, execute

def find_the_primes_numbers(N, primes):
    # Choose a random integer a between 1 and N-1
    a = 2  # We can choose any number here, but 2 is a good choice for small numbers

    # Create a quantum circuit with log2(N) qubits
    num_qubits = N.bit_length()
    qc = QuantumCircuit(num_qubits*2, num_qubits)

    # Apply Hadamard gates to the first num_qubits qubits
    for i in range(num_qubits):
        qc.h(i)

    # Apply the function f(x) = a^x mod N
    for i in range(num_qubits):
        qc.x(i + num_qubits)
        for j in range(2**i):
            qc.swap(i, i + num_qubits)
            qc.append(QFT(num_qubits), range(num_qubits))
            qc.measure(range(num_qubits), range(num_qubits))

    # Run the circuit on a simulator
    backend = Aer.get_backend('qasm_simulator')
    counts = execute(qc, backend).result().get_counts()

    # Find the period r of the function f(x) = a^x mod N
    r = int(max(counts, key=counts.get), 2)

    # Calculate x and y
    x = pow(a, r//2, N)
    y = N // gcd(N, x-1)

    # Check if x+y=N and x and y are prime
    if x + y == N and x in primes and y in primes:
        return f"{x},{y}"
    else:
        return "No prime factors found"

def QFT(num_qubits):
    qc = QuantumCircuit(num_qubits)
    for i in range(num_qubits):
        for j in range(i):
            qc.cu1(2 * math.pi / (2 ** (i - j)), j, i)
        qc.h(i)
    return qc