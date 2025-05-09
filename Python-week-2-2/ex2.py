a,b,c,d = [int(i) for i in input('Enter numbers : ').split(' ')]

def find_max(a,b,c,d):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    if d > max_num:
        max_num = d
    return max_num

def find_min(a,b,c,d):
    min_num = a
    if b < min_num:
        min_num = b
    if c < min_num:
        min_num = c
    if d < min_num:
        min_num = d
    return min_num

max = find_max(a,b,c,d)
min = find_min(a,b,c,d)
sum = (a+b+c+d)-(max+min)

print(f'Total : {sum}')