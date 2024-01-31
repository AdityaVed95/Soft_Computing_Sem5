import numpy as np
import math
import random
learning_rate = 0.3

def bipolarBinarySigmoid(x):
    return ((2*(1+math.exp(-x))**-1)-1)

x1 = np.array([1,-2,0,-1])
x2 = np.array([0,1.5,-0.5,-1])
x3 = np.array([-1,1,0.5,-1])
input_vectors = [x1,x2,x3]
w = np.array([1,-1,0,0.5])
target_output = [1,1,1,1]

for i in range(3):
    x = input_vectors[i]
    net = np.dot(x,w)
    print("\nNet value of ",i,"th iteration is: ",net)
    # print(net)
    o = bipolarBinarySigmoid(net)
    print("Output of neuron is : ",o)
    der = 0.5*(1-(o*o))
    w = learning_rate*(target_output[i]-o)*der*x + w
    print("Updated Weight vector is : ",w)
    print()
