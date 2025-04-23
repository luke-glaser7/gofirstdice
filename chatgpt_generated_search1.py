import random
import itertools
import numpy as np
from collections import Counter

# Number of players (5 dice)
num_dice = 5
# Number of faces per die
num_faces = 30
# Total number of permutations (5 players)
total_permutations = np.math.factorial(num_dice)

# Define fairness threshold for the Chi-squared statistic (lower is better)
FAIRNESS_THRESHOLD = 1.0  # Adjust this as needed for "sufficiently fair"

# Generate a candidate set of dice (random faces between 1 and 150)
def generate_candidate_dice_set():
    return [[random.randint(1, 150) for _ in range(num_faces)] for _ in range(num_dice)]

# Simulate a dice roll (return rankings)
def roll_dice(dice_set):
    rolls = [random.choice(die) for die in dice_set]
    rankings = sorted(range(len(rolls)), key=lambda x: rolls[x], reverse=True)
    return tuple(rankings)

# Perform multiple simulations and track permutations
def simulate_and_track(dice_set, num_trials=100000):
    permutation_counts = Counter()
    
    for _ in range(num_trials):
        rankings = roll_dice(dice_set)
        permutation_counts[rankings] += 1
    
    return permutation_counts

# Calculate Chi-squared statistic for fairness
def calculate_fairness(permutation_counts):
    expected_count = sum(permutation_counts.values()) / total_permutations
    chi_squared = sum((observed - expected_count) ** 2 / expected_count for observed in permutation_counts.values())
    return chi_squared

# Main search loop (now stops when fairness threshold is met)
def search_for_fair_dice_sets(num_trials=100000):
    while True:  # Loop until a fair dice set is found
        dice_set = generate_candidate_dice_set()
        permutation_counts = simulate_and_track(dice_set, num_trials)
        fairness = calculate_fairness(permutation_counts)

        print(f"Fairness of this dice set: {fairness}")

        # If fairness is below the threshold, stop and return the dice set
        if fairness < FAIRNESS_THRESHOLD:
            print(f"Fair dice set found with fairness {fairness}: {dice_set}")
            return dice_set

# Run the search
if __name__ == "__main__":
    search_for_fair_dice_sets()
