from .train import train_xor

def main():
    input_vector = [[0,0],[0,1],[1,0],[1,1]]
    weight_from_input_to_hidden_layer = [[0.1,0.2],[0.3,0.1]]
    weight_from_hidden_to_output_layer = [0.2,0.1]
    weight_of_bias_to_hidden_neuron_1 = 0.1
    weight_of_bias_to_hidden_neuron_2 = 0.1
    weight_of_bias_to_output_neuron = 0.1
    target_output_vector = [0,1,1,0]
    learning_rate = 1
    
    (input_vector, target_output_vector, learning_rate, weight_from_input_to_hidden_layer, weight_from_hidden_to_output_layer, weight_of_bias_to_hidden_neuron_1, weight_of_bias_to_hidden_neuron_2, weight_of_bias_to_output_neuron) = train_xor(input_vector, target_output_vector, learning_rate, weight_from_input_to_hidden_layer, weight_from_hidden_to_output_layer, weight_of_bias_to_hidden_neuron_1, weight_of_bias_to_hidden_neuron_2, weight_of_bias_to_output_neuron)
    
    print("\n\n\n============ Final output : =================")
    print("weight_from_input_to_hidden_layer: ",weight_from_input_to_hidden_layer)
    print("weight_from_hidden_to_output_layer : ",weight_from_hidden_to_output_layer)
    print("weight_of_bias_to_hidden_neuron_1 :",weight_of_bias_to_hidden_neuron_1)
    print("weight_of_bias_to_hidden_neuron_2  : ",weight_of_bias_to_hidden_neuron_2)
    print("weight_of_bias_to_output_neuron : ",weight_of_bias_to_output_neuron)


if __name__ == '__main__':
    main()
