print(" *** Power of n ***")
n, num = [int(i) for i in input("Enter n num : ").split(' ')]

original_num = num  
power = 0
factors = []

if n <= 1 or num < 1:
    print(f"{original_num} is NOT a power of {n}")
else:
    while num % n == 0:
        num = num // n
        power += 1
        factors.append(str(n))

    if num == 1:
        print(f"{original_num} is a power of {n}.")
        print(f"{original_num} = {'*'.join(factors)}")
    else:
        print(f"{original_num} is NOT a power of {n}")

print("===== End of program =====")
