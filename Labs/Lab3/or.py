def net_calculation(weight_vector,input_vector,weight_bias):
    # net = yin
    
    yin = 0
    
    for i in range (len(input_vector)):
        yin = yin + input_vector[i] * weight_vector[i]
        
    yin = yin + weight_bias
    
    return yin

    

def threshold_activation_function(yin):
    if yin >= 1:
        return 1
    
    elif yin > -1 and yin < 1 :
        return 0
    
    elif yin <= -1:
        return -1
        

def update_weights(learning_rate,error,input_vector,weight_vector,weight_bias):
    
    for i in range(len(weight_vector)):
        change_in_weight = learning_rate * error * input_vector[i]
        weight_vector[i] = weight_vector[i] + change_in_weight
    
    weight_bias = weight_bias + learning_rate * error
    
    return weight_vector,weight_bias

def error_vector_all_zeros_check(error_vector):
    for error in error_vector:
        if error == 0:
            continue
        else:
            return 0
    
    return 1
    

def main():
    input_vector1 = [1,1]
    input_vector2 = [1,-1]
    input_vector3 = [-1,1]
    input_vector4 = [-1,-1]
    
    target_output_vector = [1,1,1,-1]
    
    weight_vector = [0,0]
    learning_rate = 1
    weight_bias = 0
    
    input_vectors = [input_vector1,input_vector2,input_vector3,input_vector4]
    
   
    epoch_iterator = 0
    
    print("\n\n")
    
    
    
    
    while(True):
        
        error_vector = []
        input_vector_iterator = 0
        
        print("\n\n************** Starting epoch ", epoch_iterator+1," **************\n\n")
        
        for input_vector in input_vectors:
            print("For input vector ",input_vector_iterator+1," of epoch ",epoch_iterator+1 ," : ")
            yin = net_calculation(weight_vector,input_vector,weight_bias)
            y_calculated_output = threshold_activation_function(yin)
            error = target_output_vector[input_vector_iterator] - y_calculated_output
            weight_vector, weight_bias = update_weights(learning_rate,error,input_vector,weight_vector,weight_bias)
            print("The yin = ",yin)
            print("The y_calculated_output = ",y_calculated_output)
            print("The error = ",error)
            print("The new weight vector is : ", weight_vector)
            print("The new weight of the bias is : ",weight_bias)
            print("\n==================================================\n")
            error_vector.append(error)
            input_vector_iterator += 1
        
        should_we_break = error_vector_all_zeros_check(error_vector)
        
        if should_we_break == 0:
            epoch_iterator += 1
            continue
        
        else:
            break

    print("\n\nThus the final Weight Vector for which we get zero error for all input vectors is : ",weight_vector)
    print("\nThe Final Weight of Bias is : ",weight_bias,"\n\n")
    
if __name__ == "__main__":
    main()