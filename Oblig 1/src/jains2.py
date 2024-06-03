import sys
import re


def convert_to_kbps(value, unit):
    if unit == 'Mbps':
        return value * 1000  # Convert Mbps to Kbps
    elif unit == 'Kbps':
        return value
    else:
        return value


def calculate_jfi(inputs):
    n = len(inputs)  # Length of inputs for N
    total = sum(inputs)  # Sum of inputs
    total_squares = sum(x ** 2 for x in inputs)  # Sum of squares of inputs
    jfi = (total ** 2) / (n * total_squares)  # Jain's Fairness Index calculation
    return jfi  # Return JFI


filename = sys.argv[1]
arguments = []

with open(filename, 'r') as file:
    for line in file:
        # Extract numbers and units
        match = re.search(r'(\d+)\s*(Mbps|Kbps)?', line)
        if match:
            value = int(match.group(1))
            unit = match.group(2) if match.group(2) else 'Kbps'
            # Convert all throughputs to Kbps
            arguments.append(convert_to_kbps(value, unit))

calc_jfi = calculate_jfi(arguments)
print(f"The Jain's fairness index is: {calc_jfi}")
