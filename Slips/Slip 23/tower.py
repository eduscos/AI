# Q.1) Write a Program to Implement Tower of Hanoi using Python
# Ans:-

def tower_of_hanoi(n, source_peg, target_peg, auxiliary_peg):
    if n == 1:
        print(f"Move disk 1 from {source_peg} to {target_peg}")
    return
    tower_of_hanoi(n - 1, source_peg, auxiliary_peg, target_peg)
    print(f"Move disk {n} from {source_peg} to {target_peg}")
    tower_of_hanoi(n - 1, auxiliary_peg, target_peg, source_peg)
    if __name__ == "__main__":
        number_of_disks = int(input("Enter the number of disks: "))
        tower_of_hanoi(number_of_disks, 'A', 'C', 'B')