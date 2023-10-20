import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt


# [0, 10]
start = 0
stop = 10 + 0.001
step = 0.25
x = np.arange(start, stop, step)
print(x)

# Triangular membership function
trimf = fuzz.trimf(x, [0, 5, 10])
plt.title("Triangular")
plt.plot(x, trimf )

# Trapezoidal membership function
trapmf = fuzz.trapmf(x, [0, 2, 8, 10])
plt.title("Trapezoidal")
plt.plot(x, trapmf)

# Gaussian function
mean = 5.0
sigma = 1.25
gaussmf = fuzz.gaussmf(x, mean, sigma)
plt.title("Gaussian")
plt.plot(x,gaussmf )

# Generalized
width = 2.0
slope = 4.0
center = 5.0
gbellmf = fuzz.gbellmf(x, width, slope, center)
plt.title("Generalized")
plt.plot(x,gbellmf )


# Sigmoid membership function
center = 5.0
width_control = 2.0
sigmf = fuzz.sigmf(x, center, width_control)
plt.title("Membership functions")
plt.plot(x,sigmf )

plt.legend()

plt.show()