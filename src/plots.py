# ==========================================================
# plots.py
# Visualization Module
# Author: Varsha V
# ==========================================================

import matplotlib.pyplot as plt

# Sample Data

switching = [0, 1, 2, 3]
average_power = [0, 12, 24, 36]

plt.figure(figsize=(8,5))

plt.plot(
    switching,
    average_power,
    marker="o",
    linewidth=2
)

plt.title("Average Power vs Switching Activity")

plt.xlabel("Switching Activity")

plt.ylabel("Average Power")

plt.grid(True)

plt.tight_layout()

plt.savefig("../images/average_power.png")

plt.show()

# ---------------------------------------------------------

inputs = [
    "000",
    "001",
    "010",
    "011",
    "100",
    "101",
    "110",
    "111"
]

power = [
    0,
    12,
    12,
    24,
    12,
    24,
    24,
    36
]

plt.figure(figsize=(8,5))

plt.bar(inputs, power)

plt.title("Power vs Input Combinations")

plt.xlabel("Input")

plt.ylabel("Power")

plt.tight_layout()

plt.savefig("../images/power_inputs.png")

plt.show()

print("Graphs generated successfully.")