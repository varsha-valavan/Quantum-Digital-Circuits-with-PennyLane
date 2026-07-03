# ==========================================================
# quantum_mux.py
# Quantum 2:1 Multiplexer using PennyLane
# Author: Varsha V
# ==========================================================

import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# ==========================================================
# DEVICE SETUP
# ==========================================================

# Wires:
# 0 -> Input A
# 1 -> Input B
# 2 -> Select S
# 3 -> Output Y

dev = qml.device("default.qubit", wires=4)

# ==========================================================
# QUANTUM MULTIPLEXER
# ==========================================================

@qml.qnode(dev)
def quantum_mux(a, b, s):

    # Encode inputs

    if a == 1:
        qml.PauliX(wires=0)

    if b == 1:
        qml.PauliX(wires=1)

    if s == 1:
        qml.PauliX(wires=2)

    # Multiplexer Logic

    qml.CNOT(wires=[0, 3])

    qml.Toffoli(wires=[2, 1, 3])

    return qml.probs(wires=3)

# ==========================================================
# INPUT COMBINATIONS
# ==========================================================

inputs = [

    (0,0,0),
    (0,1,0),
    (1,0,0),
    (1,1,0),

    (0,0,1),
    (0,1,1),
    (1,0,1),
    (1,1,1)

]

# ==========================================================
# TRUTH TABLE
# ==========================================================

print("="*60)
print("QUANTUM 2:1 MULTIPLEXER")
print("="*60)

print("\nTruth Table\n")

print(" A  B  S | Y ")
print("----------------")

truth_table = []

for a,b,s in inputs:

    probs = quantum_mux(a,b,s)

    y = int(np.argmax(probs))

    truth_table.append([a,b,s,y])

    print(f" {a}  {b}  {s} | {y}")

# ==========================================================
# CLASSICAL VERIFICATION
# ==========================================================

def classical_mux(a,b,s):

    return (1-s)*a + s*b

print("\n")
print("="*60)
print("CLASSICAL VERIFICATION")
print("="*60)

correct = 0

for a,b,s in inputs:

    quantum_output = int(np.argmax(quantum_mux(a,b,s)))

    classical_output = classical_mux(a,b,s)

    if quantum_output == classical_output:
        correct += 1

    print(
        f"A={a} B={b} S={s} -> "
        f"Quantum={quantum_output} "
        f"Classical={classical_output}"
    )

accuracy = (correct/len(inputs))*100

print("\nAccuracy : {:.2f}%".format(accuracy))

# ==========================================================
# POWER ESTIMATION
# ==========================================================

def basic_power(a,b,s):

    switching = a+b+s

    gate_cost = 6

    return switching*gate_cost


def improved_power(a,b,s):

    switching = a+b+s

    cnot = 1

    toffoli = 5

    depth = 2

    return switching*(cnot+toffoli)*depth

print("\n")
print("="*60)
print("POWER ESTIMATION")
print("="*60)

power_values = []

for a,b,s in inputs:

    power = improved_power(a,b,s)

    power_values.append(power)

    print(
        f"A={a} B={b} S={s} "
        f"Power ≈ {power}"
    )

# ==========================================================
# GRAPH 1
# ==========================================================

labels = []

for a,b,s in inputs:

    labels.append(f"{a}{b}{s}")

plt.figure(figsize=(8,5))

plt.bar(labels,power_values)

plt.title("Power vs Input Combinations")

plt.xlabel("Inputs (ABS)")

plt.ylabel("Estimated Power")

plt.grid(axis="y",alpha=0.3)

plt.tight_layout()

plt.savefig("../images/power_vs_inputs.png")

plt.show()

# ==========================================================
# GRAPH 2
# ==========================================================

grouped = defaultdict(list)

for a,b,s in inputs:

    switching = a+b+s

    grouped[switching].append(
        improved_power(a,b,s)
    )

avg_switch = []

avg_power = []

for key in sorted(grouped.keys()):

    avg_switch.append(key)

    avg_power.append(
        sum(grouped[key])/len(grouped[key])
    )

plt.figure(figsize=(8,5))

plt.plot(
    avg_switch,
    avg_power,
    marker="o",
    linewidth=2
)

plt.title("Average Power vs Switching Activity")

plt.xlabel("Switching Activity")

plt.ylabel("Average Power")

plt.grid(True)

plt.tight_layout()

plt.savefig("../images/avg_power_vs_switching.png")

plt.show()

# ==========================================================
# SAVE RESULTS
# ==========================================================

with open("../results/mux_results.txt","w") as file:

    file.write("Quantum 2:1 Multiplexer Results\n\n")

    file.write("Truth Table\n")

    file.write("--------------------------\n")

    for row in truth_table:

        file.write(
            f"A={row[0]} "
            f"B={row[1]} "
            f"S={row[2]} "
            f"Y={row[3]}\n"
        )

    file.write("\n")

    file.write(f"Accuracy : {accuracy:.2f}%\n")

print("\nResults saved successfully!")

print("Graphs saved in images folder.")

print("Truth table saved in results folder.")

print("\nProject Execution Completed Successfully.")