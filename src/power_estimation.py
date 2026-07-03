# ==========================================================
# power_estimation.py
# Quantum Power Estimation Module
# Author: Varsha V
# ==========================================================

import matplotlib.pyplot as plt

# ==========================================================
# QUANTUM GATE ENERGY MODEL
# ==========================================================

GATE_ENERGY = {
    "Pauli-X": 0.8e-15,      # Joules
    "CNOT": 1.5e-15,
    "Toffoli": 3.2e-15
}

CLOCK_FREQUENCY = 1e9        # 1 GHz
DELAY_NS = 50                # Estimated Delay (ns)

# ==========================================================
# POWER ESTIMATION FUNCTION
# ==========================================================

def estimate_power(pauli_x, cnot, toffoli):

    total_energy = (
        pauli_x * GATE_ENERGY["Pauli-X"] +
        cnot * GATE_ENERGY["CNOT"] +
        toffoli * GATE_ENERGY["Toffoli"]
    )

    power = total_energy * CLOCK_FREQUENCY
    power_micro = power * 1e6

    pdp = power_micro * DELAY_NS * 1e-3

    return total_energy, power_micro, pdp


# ==========================================================
# SAMPLE ESTIMATION
# ==========================================================

pauli = 8
cnot = 1
toffoli = 1

energy, power, pdp = estimate_power(
    pauli,
    cnot,
    toffoli
)

print("="*60)
print("QUANTUM POWER ESTIMATION")
print("="*60)

print(f"Pauli-X Gates : {pauli}")
print(f"CNOT Gates    : {cnot}")
print(f"Toffoli Gates : {toffoli}")

print(f"\nTotal Energy : {energy:.2e} J")
print(f"Power         : {power:.4f} µW")
print(f"Delay         : {DELAY_NS} ns")
print(f"PDP           : {pdp:.4f} pJ")

# ==========================================================
# ENERGY BREAKDOWN GRAPH
# ==========================================================

labels = ["Pauli-X", "CNOT", "Toffoli"]

values = [
    pauli * GATE_ENERGY["Pauli-X"],
    cnot * GATE_ENERGY["CNOT"],
    toffoli * GATE_ENERGY["Toffoli"]
]

plt.figure(figsize=(7,5))

plt.bar(labels, values)

plt.title("Energy Consumption by Quantum Gates")

plt.ylabel("Energy (Joules)")

plt.tight_layout()

plt.savefig("../images/energy_breakdown.png")

plt.show()

# ==========================================================
# SAVE REPORT
# ==========================================================

with open("../results/power_report.txt", "w") as file:

    file.write("Quantum Power Estimation Report\n")
    file.write("="*50)
    file.write("\n\n")

    file.write(f"Pauli-X Gates : {pauli}\n")
    file.write(f"CNOT Gates    : {cnot}\n")
    file.write(f"Toffoli Gates : {toffoli}\n\n")

    file.write(f"Total Energy : {energy:.2e} J\n")
    file.write(f"Power        : {power:.4f} µW\n")
    file.write(f"Delay        : {DELAY_NS} ns\n")
    file.write(f"PDP          : {pdp:.4f} pJ\n")

print("\nPower report saved successfully.")
print("Graph saved to images folder.")