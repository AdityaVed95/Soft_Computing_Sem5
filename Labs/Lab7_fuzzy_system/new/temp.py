import numpy as np 
import matplotlib.pyplot as plt

def trapezoidal_membership(x):
    if x <= 0:
        return 0
    elif 0 < x < 5:
        return x / 5.0
    elif 5 <= x <= 8:
        return 1
    elif 8 < x:
        return 1 - (x - 8) / (10 - 8) # Here, 10 is an example upper limit. You can adjust it based on the maximum value of x.
    else:
        return 0

# Test the function
# x_values = [0, 3, 5, 6.5, 8, 9]
x_values = np.linspace(0,10,40)
y_values = []
for x in x_values:
    print(f"x={x}, membership={trapezoidal_membership(x)}")
    y_values.append(trapezoidal_membership(x))

# vfxn = np.vectorize(trapezoidal_membership)
# y = vfxn(x_values)
# print(y)

print(y_values)
plt.plot(x_values, y_values)
plt.title('Plot of fxn(x)')
plt.xlabel('x', color='#1C2833')
plt.ylabel('fxn(x)', color='#1C2833')
# plt.legend(loc='upper left')
plt.grid()
plt.show()