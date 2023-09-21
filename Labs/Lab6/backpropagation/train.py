from .activation import unipolar_sigmoidal_activation_fxn

def train_xor(input_vector, target_output_vector, learning_rate, weight_from_input_to_hidden_layer, weight_from_hidden_to_output_layer, weight_of_bias_to_hidden_neuron_1, weight_of_bias_to_hidden_neuron_2, weight_of_bias_to_output_neuron):
    # ... [your backpropagation logic here] ...
    
    # doing only 1 epoch consisting of 4 iterations : 
    for i in range (4):
    
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
        
        weight_of_bias_to_output_neuron += change_in_bias_weight_to_output_neuron
        
        weight_from_input_to_hidden_layer = [[weight_from_input_to_hidden_layer[0][0]+change_in_weight_from_input_to_hidden_layer[0][0],weight_from_input_to_hidden_layer[0][1]+change_in_weight_from_input_to_hidden_layer[0][1]],[weight_from_input_to_hidden_layer[1][0]+change_in_weight_from_input_to_hidden_layer[1][0],weight_from_input_to_hidden_layer[1][1]+change_in_weight_from_input_to_hidden_layer[1][1]]]
        
        weight_of_bias_to_hidden_neuron_1 += change_in_bias_to_hidden_neuron1 
        
        weight_of_bias_to_hidden_neuron_2 += change_in_bias_to_hidden_neuron2 

        print("\n\n================")
        print("for input vector ",i," : ")
        print("weight_from_input_to_hidden_layer: ",weight_from_input_to_hidden_layer)
        print("weight_of_bias_to_hidden_neuron_1 :",weight_of_bias_to_hidden_neuron_1)
        print("weight_of_bias_to_hidden_neuron_2  : ",weight_of_bias_to_hidden_neuron_2)
        print("weight_from_hidden_to_output_layer : ",weight_from_hidden_to_output_layer)
        print("weight_of_bias_to_output_neuron : ",weight_of_bias_to_output_neuron)
    
    
    return (input_vector, target_output_vector, learning_rate, weight_from_input_to_hidden_layer, weight_from_hidden_to_output_layer, weight_of_bias_to_hidden_neuron_1, weight_of_bias_to_hidden_neuron_2, weight_of_bias_to_output_neuron)