import numpy as np
import math
import random
learning_rate = 0.3

def bipolarBinarySigmoid(x):
    return ((2*(1+math.exp(-x))**-1)-1)

x1 = np.array([1,-2,0,-1])
x2 = np.array([0,1.5,-0.5,-1])
x3 = np.array([-1,1,0.5,-1])
w1 = np.array([1,-1,0,0.5])

net1 = np.dot(x1,w1)
print("\nNet value 1: ",net1)
# print(net)
o = bipolarBinarySigmoid(net1)
print("Output of neuron is : ",o)
der = 0.5*(1-(o*o))
w2 = learning_rate*(1-o)*der*x1 + w1
print("Updated Weight vector is : ",w2)

net2 = np.dot(x2,w2)
print("\nNet value 2: ",net2)
o2 = bipolarBinarySigmoid(net2)
print("Output of neuron is : ",o2)
der2 = 0.5*(1-(o2*o2))

w3 = learning_rate*(1-o2)*der2*x2 + w2
print("Updated Weight vector is : ",w3)

net3 = np.dot(x3,w3)
print("\nNet value 3: ",net3)
o3 = bipolarBinarySigmoid(net3)
print("Output of neuron is : ",o3)
der3 = 0.5*(1-(o3*o3))

w4 = learning_rate*(1-o3)*der3*x3 + w3

print("Updated Weight vector is : ",w4,"\n")