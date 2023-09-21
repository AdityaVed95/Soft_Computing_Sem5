import numpy as np

def net_calculation(weight_vector,input_vector,bias,weight_of_bias):
    net = 0 
    for i in range (len(input_vector)):
        net = net + input_vector[i]*weight_vector[i]
    
    net = net + bias * weight_of_bias
    return net

def binary_step_fxn(net):
    
    if net >= 2:
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
    
    input_vector = [x1,x2]
    weight_vector = [1,1]
    bias  = 1
    weight_of_bias = 1
    net = net_calculation(weight_vector,input_vector,bias,weight_of_bias)
    out = binary_step_fxn(net)
    print("The Output of the OR Gate Neuron is : ",out)
    
    print("\n")
    
if __name__ == "__main__":
    main()