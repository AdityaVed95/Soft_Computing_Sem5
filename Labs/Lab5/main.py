def activation_fxn(net):
    if net>= 0:
        return 1
    else:
        return -1

def new_weight(old_weight,input_element,actual_output):
    return old_weight + (input_element*actual_output)


input_vector1 = [1,1]
input_vector2 = [1,-1]
input_vector3 = [-1,1]
input_vector4 = [-1,-1]

target_output_vector = [1,-1,-1,-1]

weight_vector = [2,1]
learning_rate = 1
weight_bias = -3

input_vectors = [input_vector1,input_vector2,input_vector3,input_vector4]

print("\nInitialisations at start is :")
print("Weight Vector : ",weight_vector)
print("Weight of Bias : ",weight_bias)


# for 4 input vectors : 
for j in range(4):
    input_to_neuron = 0
    
    input_to_neuron = input_vectors[j][0]*weight_vector[0] + input_vectors[j][1]*weight_vector[1] + weight_bias
    
    actual_output = activation_fxn(input_to_neuron)
    
    weight_vector = [new_weight(weight_vector[0],input_vectors[j][0],actual_output),new_weight(weight_vector[1],input_vectors[j][1],actual_output)]
    
    weight_bias = new_weight(weight_bias,1,actual_output)

print("\nThe results after unsupervised training for 1 epoch is : \n")
print("weight of bias : ",weight_bias)
print("weight vector : ",weight_vector)

print("\nNow lets try to test it on our dataset : ")

for j in range(len(input_vectors)):
    print("For ",j+1,"th input vector : ",input_vectors[j])
    input_to_neuron = input_vectors[j][0]*weight_vector[0] + input_vectors[j][1]*weight_vector[1] + weight_bias
    
    actual_output = activation_fxn(input_to_neuron)
    print("Output generated is : ",actual_output,end="\n\n")
    
    















