# Q.1) Write a Python program to accept a string. Find and print the number of
# upper case alphabets and lower case alphabets.
# Ans:-

def count_upper_lower(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count

# Example usage
user_input = input("Enter a string: ")
upper, lower = count_upper_lower(user_input)

print(f"Number of uppercase alphabets: {upper}")
print(f"Number of lowercase alphabets: {lower}")