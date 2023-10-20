def find_unique_number(num_list):
    if len(num_list) == 0:
        return None
    
    if len(num_list) == 1:
        return num_list[0]
    
    freq = {}
    for item in num_list:
        if item in freq:
            freq.update({item:freq[item]+1})
        else:
            freq.update({item:1})
    
    for key in freq:
        if freq[key] == 1:
            return key
    # write your code here

# take integer input and convert it to list
numbers = list(map(int, input().split()))

# call the function
print(find_unique_number(numbers))