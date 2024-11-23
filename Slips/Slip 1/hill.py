## Q1. Python program that demonstrates the hill climbing algorithm to find the
##  maximum of a mathematical function. (For example f(x)=-x^2+4x)

import random

def hill_climbing(function, initial_value, step_size, iterations):
    
    current_value = initial_value
    
    for _ in range(iterations):
        neighbors = [current_value - step_size, current_value, current_value + step_size]
        neighbors = [val for val in neighbors if val >= 0] # Ensure x is non-negative
        current_value = max(neighbors, key=function, default=current_value)
    
    return current_value, function(current_value)

# Define the function
my_function = lambda x: -x**2 + 4*x

# Set initial parameters
initial_x = random.uniform(0, 10)
step_size = 0.1
iterations = 100

# Run hill climbing algorithm
result_x, result_value = hill_climbing(my_function, initial_x, step_size, iterations)

# Print results
print("Maximum found at x =", result_x)
print("Maximum value =", result_value)