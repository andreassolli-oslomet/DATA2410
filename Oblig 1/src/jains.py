import sys
import re


def calculate_jfi(inputs):
    n = len(inputs)  # Length of inputs for N
    total = sum(inputs)  # Sum of inputs
    total_squares = sum(x ** 2 for x in inputs)  # Sum of squares of inputs
    jfi = (total ** 2) / (n * total_squares)  # Jain's Fairness Index calculation
    return jfi  # Return JFI


# Combine command-line arguments into one string
# Extract and convert digit sequences to integers
arguments = [int(x) for x in re.findall(r'\d+', sys.argv[0])]
# Calculate JFI for inputs
calc_jfi = calculate_jfi(arguments)
# Output JFI
print(f"Jains Fairness Index is: {calc_jfi}")
