n = int(input("Enter the number of rows: "))
i = 1

while i <= n:
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
        
    print()
    i += 1