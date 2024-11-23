# Q.1) Write a python program using mean end analysis algorithmproblem of
# transforming a string of lowercase letters into another string.
# Ans:-

def mean_end_analysis(initial, target):
    if len(initial) != len(target):
        print("Strings must have the same length.")
        return
        operations = []
        for i in range(len(initial)):
            if initial[i] != target[i]:
                operations.append(f"Change '{initial[i]}' to '{target[i]}' at position {i + 1}")
            if not operations:
                print("Strings are already the same.")
            else:
                print("Transformation Steps:")
            for operation in operations:
                print(operation)

if __name__ == "__main__":
    initial_string = input("Enter the initial string: ").lower()
    target_string = input("Enter the target string: ").lower()
    mean_end_analysis(initial_string, target_string)