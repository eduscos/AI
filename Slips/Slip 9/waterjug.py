# Q.2) Write a Python program to solve water jug problem. 2 jugs with capacity 5
# gallon and 7 gallon are given with unlimited water supply respectively. The target
# to achieve is 4 gallon of water in second jug.
# Ans:-

def water_jug_problem(capacity_x, capacity_y, target):
    jug_x = 0
    jug_y = 0
    while jug_x != target and jug_y != target:

        print(f"Jug X: {jug_x}L, Jug Y: {jug_y}L")

        # Fill jug X if it is empty
        if jug_x == 0:
            jug_x = capacity_x
            print("Fill Jug X")
        # Transfer water from jug X to jug Y if jug X is not empty
        elif jug_x > 0 and jug_y < capacity_y:
            transfer = min(jug_x, capacity_y - jug_y)
            jug_x -= transfer
            jug_y += transfer
            print("Transfer from Jug X to Jug Y")
        # Empty jug Y if it is full
        elif jug_y == capacity_y:
            jug_y = 0
            print("Empty Jug Y")
            print(f"Jug X: {jug_x}L, Jug Y: {jug_y}L")
            print("Solution Found!")

# Main function to initiate the problem
def main():
    capacity_x = 5 # Capacity of jug X
    capacity_y = 7 # Capacity of jug Y
    target = 4 # Amount of water to measure
    print("Solving Water Jug Problem:")
    water_jug_problem(capacity_x, capacity_y, target)

if __name__ == '__main__':
main()