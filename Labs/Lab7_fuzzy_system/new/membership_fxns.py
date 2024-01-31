import numpy as np 
import matplotlib.pyplot as plt

def fxn(x):
    if x <= 4:
        return 0
    elif x>4 and x<=6:
        return x/6
    elif x>6 and x<=8:
        return 1
    elif x>8 and x<10:
        return x/10
    else:
        return 0
    

x = 4.1025641
y = fxn(x)
print(y)

x = np.linspace(0,10,40)

# # Vectorize the function to handle numpy arrays
# vfxn = np.vectorize(fxn)


# y = vfxn(x)

# print(x)
# print(y)


# plt.plot(x, y, label='fxn(x)')
# plt.title('Plot of fxn(x)')
# plt.xlabel('x', color='#1C2833')
# plt.ylabel('fxn(x)', color='#1C2833')
# plt.legend(loc='upper left')
# plt.grid()
# plt.show()


# y_complement = 