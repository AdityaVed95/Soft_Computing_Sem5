import numpy as np
import math
import matplotlib.pyplot as plt

def net_calculation(weight_vector,input_vector):
    net = 0 
    for i in range (input_vector.size):
        net = net + input_vector[i]*weight_vector[i]
    
    return net

def identity_activation_fxn(net):
    return net
    
def binary_step_fxn(net_vector):
    f_net_vector = np.array([])
    
    for i in net_vector:
        if i >= 0:
            f_net_vector = np.append(f_net_vector,1)
        
        else:
            f_net_vector = np.append(f_net_vector,0)
    
    return f_net_vector


def bipolar_step_fxn(net):
    
    if net >= 0:
        return 1
    
    else:
        return -1   
    
def binary_sigmoidal_activation_fxn(net_vector):
    
    f_net_vector = np.array([])
    
    for i in net_vector:
        f_net_vector = np.append(f_net_vector, 1/(1+ math.e**(-i) ) )    
        
    return f_net_vector

def bipolar_sigmoidal_activation_fxn(net):
    return np.tanh(net)

def Rectified_Linear_Unit_activation_fxn(net):
    if net >= 0:
        return net
    else:
        return 0

[10,20,30], [1,2,3]
[40,50,60], [4,5,6]

def main():
    input_vector = np.random.randint(-1000,1000,size = (250,4))
    # print(input_vector)
    weight_vector = np.random.uniform(-1,1,1000)
    weight_vector = weight_vector.reshape(250,4)
    # print(weight_vector)
    net_vector = np.array([])
    
    
    for i in range (250):
        net_calc = net_calculation(weight_vector[i],input_vector[i])
        net_vector = np.append(net_vector,net_calc)
        
    print(net_vector)
    
    # f_net_vector = binary_step_fxn(net_vector)
    # plt.scatter(net_vector,f_net_vector,c=net_vector,cmap='viridis')
    # plt.show()
    
    f_net_vector = binary_sigmoidal_activation_fxn(net_vector)
    plt.scatter(net_vector,f_net_vector,c=net_vector,cmap='viridis')
    plt.show()
    

if __name__ == "__main__":
    main()
    