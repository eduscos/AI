# Q.1) Write a python program to remove punctuations from the given string?
# Ans:-

import string

def remove_punctuation(input_string):
    
    # Obtain the set of punctuation characters
    punctuation_set = set(string.punctuation)
    
    # Remove punctuation from the input string
    result_string = ''.join(char for char in input_string if char not in punctuation_set)
    
    return result_string

# Example usage
input_string = "Hello, World! This is an example string with punctuations!!!"

result = remove_punctuation(input_string)

print("Original String:", input_string)
print("String without Punctuation:", result)