Midterm, Final, Homework = [int(i) for i in input('Enter inputs : ').split(',')]

if 0<= Midterm <= 40 and 0 <= Final <= 50 and Homework <= 10:
    print(f'Total score : {Midterm + Final + Homework}')
else:
    print('Invalid input')