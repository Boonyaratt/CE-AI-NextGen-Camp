user_input = input("Select 1. (Rectangle) or 2. (Triangle), width, length : ")

try:
    x_str, width_str, length_str = user_input.split(',')
    x = int(x_str.strip())
    width = float(width_str.strip())
    length = float(length_str.strip())

    if x == 1:
        area = width * length
        print("Rectangle Area =", int(area))
    elif x == 2:
        area = 0.5 * width * length
        print("Triangle area =", int(area))
    else:
        print("Invalid selection")
except:
    print("Invalid input format")
