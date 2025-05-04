try:
    r, h = [int(i) for i in input('Enter number : ').split(',')]
    if r < 0 or h < 0:
        raise ValueError("error")  # บังคับให้เข้า except
    print(int(3.14*r*r*h))
except:
    print("error")