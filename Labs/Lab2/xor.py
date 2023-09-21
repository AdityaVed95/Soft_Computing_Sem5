import numpy as np

def net_calculation(weight_vector,input_vector,bias,weight_of_bias):
    net = 0 
    for i in range (len(input_vector)):
        net = net + input_vector[i]*weight_vector[i]
    
    net = net + bias * weight_of_bias
    return net

def binary_step_fxn(net):
    
    if net >= 1:
        return 1
    
    else:
        return 0
    
def main():
    # [[0,0],[0,1],[1,0],[1,1]]
    # 1,2,2,3
    
    print("\n\nGive value of x1 :  ")
    x1 = int(input())
    print("Give value of x2 :  ")
    x2 = int(input())
        
    input_vector1 = [x1,x2]
    weight_vector1 = [1,-1]
    
    input_vector2 = [x1,x2]
    weight_vector2 = [-1,1]
    
    bias  = 1
    weight_of_bias = 0
    
    
    net1 = net_calculation(weight_vector1,input_vector1,bias,weight_of_bias)
    out1 = binary_step_fxn(net1)
    
    print("\nOutput of 1st neuron of 1st layer is : ",out1)
    
    net2 = net_calculation(weight_vector2,input_vector2,bias,weight_of_bias)
    out2 = binary_step_fxn(net2)
    
    print("\nOutput of 2nd neuron of 1st layer is : ",out2)
    
    input_vector3 = [out1,out2]
    weight_vector3 = [1,1]
    
    net3 = net_calculation(weight_vector3,input_vector3,bias,weight_of_bias)
    out3 = binary_step_fxn(net3)

    print("\nOutput of the neuron of 2nd layer i.e the output of XOR neural network is : ",out3)
    
    
    
    print("\n")
    
if __name__ == "__main__":
    main()