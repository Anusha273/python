import numpy as np
from scipy.stats import spearmanr

# Data from the table
distance = np.array([50, 175, 250, 375, 425, 585, 720, 810, 875, 950])
price = np.array([1.80, 1.25, 2.00, 1.00, 1.10, 1.20, 0.80, 0.60, 1.05, 0.85])

# Calculate Spearman's Rank Correlation Coefficient
correlation, _ = spearmanr(distance, price)

# Print the result
print(f"Spearman's Rank Correlation Coefficient: {correlation:.4f}")
