
n = 5

for i in range(1, n + 1):
    # Print spaces
    for k in range(n, i, -1):
        print(" ", end="")

    # Print numbers (here just '1')
    for j in range(i, 0, -1):
        print("*", end="")

    print()  # Move to next line
