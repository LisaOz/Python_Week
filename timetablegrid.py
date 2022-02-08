n = int(input("Enter integer between 1 and 10: "))
for row in range (1, n+1):
    for column in range (1, n+1):
        print(row*column)
        print()