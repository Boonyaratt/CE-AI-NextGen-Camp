x = int(input("Enter your score : "))

if 90 <= x <= 100:
    print("A")
elif 85 <= x < 90:
    print("B+")
elif 80 <= x < 85:
    print("B")
elif 70 <= x < 80:
    print("C+")
elif 60 <= x < 70:
    print("C")
elif 55 <= x < 60:
    print("D+")
elif 50 <= x < 55:
    print("D")
elif 0 <= x < 50:
    print("F")
else:
    print("Invalid score")
