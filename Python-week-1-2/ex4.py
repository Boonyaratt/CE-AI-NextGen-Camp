try:
    a, b, c = [float(i) for i in input('Enter inputs : ').split(',')]

    if a == 0:
        raise ValueError("0.00, 0.00")  

    d = b**2 - 4*a*c  

    if d < 0:
        raise ValueError("0.00, 0.00")  

    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)

    x1 = 0.00 if x1 == 0 else x1
    x2 = 0.00 if x2 == 0 else x2

    print(f"{min(x1, x2):.2f}, {max(x1, x2):.2f}")

except ValueError:
    print("0.00, 0.00")
