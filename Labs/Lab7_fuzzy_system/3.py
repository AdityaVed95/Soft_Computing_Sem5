import numpy as np
import matplotlib.pyplot as plt

# Define the functions for A and B based on the provided image
def mu_A(x):
    if 5 <= x <= 8:
        return 1
    else:
        return 0

def mu_B(x):
    if 4 <= x <= 6:
        return 1 - abs(x - 5)
    else:
        return 0

# Define operations
def union(a, b):
    return max(a, b)

def intersection(a, b):
    return min(a, b)

def complement(a):
    return 1 - a

# Generate x values
x = np.linspace(0, 10, 400)

# Calculate y values for each function and operation
y_A = [mu_A(i) for i in x]
y_B = [mu_B(i) for i in x]
y_union = [union(mu_A(i), mu_B(i)) for i in x]
y_intersection = [intersection(mu_A(i), mu_B(i)) for i in x]
y_complement_A = [complement(mu_A(i)) for i in x]
y_complement_B = [complement(mu_B(i)) for i in x]

# Plotting
plt.figure(figsize=(12, 8))

# A
plt.subplot(2, 3, 1)
plt.plot(x, y_A, 'r')
plt.ylim(-0.1, 1.1)
plt.title('A')

# B
plt.subplot(2, 3, 2)
plt.plot(x, y_B, 'g')
plt.ylim(-0.1, 1.1)
plt.title('B')

# A union B
plt.subplot(2, 3, 3)
plt.plot(x, y_union, 'b')
plt.ylim(-0.1, 1.1)
plt.title('A union B')

# A intersection B
plt.subplot(2, 3, 4)
plt.plot(x, y_intersection, 'b')
plt.ylim(-0.1, 1.1)
plt.title('A intersection B')

# A Complement
plt.subplot(2, 3, 5)
plt.plot(x, y_complement_A, 'r')
plt.ylim(-0.1, 1.1)
plt.title('A Complement')

# B Complement
plt.subplot(2, 3, 6)
plt.plot(x, y_complement_B, 'g')
plt.ylim(-0.1, 1.1)
plt.title('B Complement')

plt.tight_layout()
plt.show()
