def calculate_price(size, cheese, extras):
    if size == 'S':
        price = 99
    elif size == 'M':
        price = 199
    elif size == 'L':
        price = 299
    else:
        print("Invalid size.")
        return

    if cheese == 'Y':
        if size == 'S':
            price += 20
        elif size == 'M':
            price += 30
        elif size == 'L':
            price += 40

    if extras == 'Y':
        price += 20

    return price

size, cheese, extras = input("Enter size(S,M,L), cheese(Y/N), extras(Y/N) : ").split()

price = calculate_price(size, cheese, extras)

print(f"Price : {price}")
