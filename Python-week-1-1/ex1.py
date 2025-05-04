try:
    b, h = [int(i) for i in input('Enter number : ').split(',')]
    if b < 0 or h < 0:
        raise ValueError("error")  # บังคับให้เข้า except
    print(int(b * h / 2))
except:
    print("error")