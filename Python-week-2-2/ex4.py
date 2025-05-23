def print_butterfly(n):
    print(" "*2*n)
    # Upper part 
    for i in range(1, n + 1):
        print('*' * i + ' ' * (2 * (n - i)) + '*' * i)

    # Lower part 
    for i in range(n-1, 0, -1):
        print('*' * i + ' ' * (2 * (n - i)) + '*' * i)
    
    print(" "*2*n)

n = int(input("Input : "))


if n <= 0:
    print("!!!Please enter positive number!!!")
else:
    print_butterfly(n)