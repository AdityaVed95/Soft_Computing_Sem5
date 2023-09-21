import math 

def unipolar_sigmoidal_activation_fxn(net):
    return 1/(1+(math.e**(-net)))

def net_calculation(weight_vector,input_vector):
    input_vector[0]
    
    

def main():
    # error back propagation training algorithm for xor gate : 
    input_vector = [[0,1]]
    weight_from_input_to_hidden_layer = [[0.6,-0.3],[-0.1,0.4]]
    weight_from_hidden_to_output_layer = [0.4,0.1]
    weight_of_bias_to_hidden_neuron_1 = 0.3
    weight_of_bias_to_hidden_neuron_2 = 0.5
    weight_of_bias_to_output_neuron = -0.2
    target_output_vector = [1]
    learning_rate = 0.25
    
    
    # for 1st training pair
    
    for i in range (1):
    
        input_to_hidden_neuron_1 = input_vector[i][0]*weight_from_input_to_hidden_layer[0][0] + input_vector[i][1]*weight_from_input_to_hidden_layer[1][0] + weight_of_bias_to_hidden_neuron_1
        
        input_to_hidden_neuron_2 = input_vector[i][0]*weight_from_input_to_hidden_layer[0][1] + input_vector[i][1]*weight_from_input_to_hidden_layer[1][1] + weight_of_bias_to_hidden_neuron_2
        
        output_of_hidden_neuron_1 = unipolar_sigmoidal_activation_fxn(input_to_hidden_neuron_1)
        
        output_of_hidden_neuron_2 = unipolar_sigmoidal_activation_fxn(input_to_hidden_neuron_2)
        
        input_to_output_neuron = output_of_hidden_neuron_1*weight_from_hidden_to_output_layer[0] + output_of_hidden_neuron_2*weight_from_hidden_to_output_layer[1] + weight_of_bias_to_output_neuron
        
        output_of_output_neuron = unipolar_sigmoidal_activation_fxn(input_to_output_neuron)
        
        change_in_weight_from_hidden_to_output_layer = [ learning_rate*(target_output_vector[0]-output_of_output_neuron)*output_of_output_neuron*(1-output_of_output_neuron)*output_of_hidden_neuron_1 , learning_rate*(target_output_vector[0]-output_of_output_neuron)*output_of_output_neuron*(1-output_of_output_neuron)*output_of_hidden_neuron_2 ]
                                                    
        
        change_in_bias_weight_to_output_neuron = learning_rate*(target_output_vector[0]-output_of_output_neuron)*output_of_output_neuron*(1-output_of_output_neuron)
        
            
        x = learning_rate*output_of_hidden_neuron_1*(1-output_of_hidden_neuron_1)*(target_output_vector[0]-output_of_output_neuron)*output_of_output_neuron*(1-output_of_output_neuron)*weight_from_hidden_to_output_layer[0]
        
        y = learning_rate*output_of_hidden_neuron_2*(1-output_of_hidden_neuron_2)*(target_output_vector[0]-output_of_output_neuron)*output_of_output_neuron*(1-output_of_output_neuron)*weight_from_hidden_to_output_layer[1]
        
        change_in_weight_from_input_to_hidden_layer = [[input_vector[i][0]* x, input_vector[i][1]* x],[input_vector[i][0]* y, input_vector[i][1]* y]]
        
        change_in_bias_to_hidden_neuron1 = learning_rate*output_of_hidden_neuron_1*(1-output_of_hidden_neuron_1)*(target_output_vector[0]-output_of_output_neuron)*output_of_output_neuron*(1-output_of_output_neuron)*weight_from_hidden_to_output_layer[0]
        
        change_in_bias_to_hidden_neuron2 = learning_rate*output_of_hidden_neuron_2*(1-output_of_hidden_neuron_2)*(target_output_vector[0]-output_of_output_neuron)*output_of_output_neuron*(1-output_of_output_neuron)*weight_from_hidden_to_output_layer[0]
        
        weight_from_hidden_to_output_layer = [weight_from_hidden_to_output_layer[0]+change_in_weight_from_hidden_to_output_layer[0],weight_from_hidden_to_output_layer[1]+change_in_weight_from_hidden_to_output_layer[1]]
        
        weight_of_bias_to_output_neuron = weight_of_bias_to_output_neuron + change_in_bias_weight_to_output_neuron
        
        weight_from_input_to_hidden_layer = [[weight_from_input_to_hidden_layer[0][0]+change_in_weight_from_input_to_hidden_layer[0][0],weight_from_input_to_hidden_layer[0][1]+change_in_weight_from_input_to_hidden_layer[0][1]],[weight_from_input_to_hidden_layer[1][0]+change_in_weight_from_input_to_hidden_layer[1][0],weight_from_input_to_hidden_layer[1][1]+change_in_weight_from_input_to_hidden_layer[1][1]]]
        
        weight_of_bias_to_hidden_neuron_1 = change_in_bias_to_hidden_neuron1 + change_in_bias_to_hidden_neuron1
        
        weight_of_bias_to_hidden_neuron_2 = change_in_bias_to_hidden_neuron2 + change_in_bias_to_hidden_neuron2

    
    print(weight_from_input_to_hidden_layer)
    print(weight_from_hidden_to_output_layer)
    print(weight_of_bias_to_output_neuron)


main()
    
    
    
    
    
    