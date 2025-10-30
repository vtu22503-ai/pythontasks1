import numpy as np
import matplotlib.pyplot as plt

# Number of experiments
num_flips = 1000
num_rolls = 1000

# --- Coin Flip Simulation ---
# 0 represents Tails, 1 represents Heads
coin_flips = np.random.randint(0, 2, num_flips)

# Counting outcomes
heads = np.count_nonzero(coin_flips == 1)
tails = np.count_nonzero(coin_flips == 0)

# --- Dice Roll Simulation ---
# Values between 1 and 6
dice_rolls = np.random.randint(1, 7, num_rolls)

# Counting occurrences of each face
dice_counts = np.bincount(dice_rolls)[1:]  # ignore index 0

# --- Visualization using Matplotlib ---
plt.figure(figsize=(10, 4))

# Plot for Coin Flips
plt.subplot(1, 2, 1)
plt.bar(['Heads', 'Tails'], [heads, tails], color=['gold', 'lightblue'], edgecolor='black')
plt.title("Coin Flip Simulation (1000 flips)")
plt.ylabel("Count")

# Plot for Dice Rolls
plt.subplot(1, 2, 2)
plt.bar(np.arange(1, 7), dice_counts, color='lightgreen', edgecolor='black')
plt.title("Dice Roll Simulation (1000 rolls)")
plt.xlabel("Dice Face")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# Display results
print("---- Simulation Results ----")
print(f"Heads: {heads}")
print(f"Tails: {tails}")
print("Dice Rolls Frequency:", dice_counts)
