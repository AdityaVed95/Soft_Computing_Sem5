import numpy as np
import math

def net_calculation(weight_vector,input_vector):
    net = 0 
    for i in range (input_vector.size):
        net = net + input_vector[i]*weight_vector[i]
    
    return net

def identity_activation_fxn(net):
    return net
    
def binary_step_fxn(net):
    
    if net >= 0:
        return 1
    
    else:
        return 0
    
def bipolar_step_fxn(net):
    
    if net >= 0:
        return 1
    
    else:
        return -1   
    
def binary_sigmoidal_activation_fxn(net):
    return 1/(1+ math.e**(-net) ) 

def bipolar_sigmoidal_activation_fxn(net):
    return np.tanh(net)

def Rectified_Linear_Unit_activation_fxn(net):
    if net >= 0:
        return net
    else:
        return 0
    

# def tangential_activation_fxn(net):
#     return 2/(1+math.e**(-2*net)) - 1


    

    
def main():
    input_vector = np.array([10,20,30])
    weight_vector = np.array([1,2,3])
    net = net_calculation(weight_vector,input_vector)
    print("Net value calculated by neuron is : ",net)
    
    print("Output of neuron if we use identity fxn is : ",identity_activation_fxn(net))
    print("Output of neuron if we use binary_step_fxn is : ",binary_step_fxn(net))
    print("Output of neuron if we use bipolar_step_fxn is : ",bipolar_step_fxn(net))
    print("Output of neuron if we use binary_sigmoidal_activation_fxn is : ",binary_sigmoidal_activation_fxn(net))
    print("Output of neuron if we use bipolar_sigmoidal_activation_fxn is : ",bipolar_sigmoidal_activation_fxn(net))
    print("Output of neuron if we use Rectified_Linear_Unit_activation_fxn is : ",Rectified_Linear_Unit_activation_fxn(net))
    
    
if __name__ == "__main__":
    main()