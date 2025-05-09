a,b,c = [int(i) for i in input('Enter input : ').split(',')]
if (a>b and a < c) or (a<c and a>b):
    print(f'Middle is {a}')
elif (b>a and b < c) or (b<c and b>a):
    print(f'Middle is {b}')
elif (c>a and c < b) or (c<b and c>a):
    print(f'Middle is {c}')
elif a == b and a == c:
    print(f'Middle is {c}')
    