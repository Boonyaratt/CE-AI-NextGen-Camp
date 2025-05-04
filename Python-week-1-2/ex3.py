try:
    student_ID, name = input('Enter student ID and name : ').split(',')

    student_ID = student_ID.strip()
    name = name.strip()

    if not (student_ID.isdigit() and len(student_ID) == 8):
        raise ValueError("Invalid student ID")

    for ch in name:
        if not (ch.isalpha() or ch == ' '):
            raise ValueError("Invalid name")

    print(f"Student ID : {student_ID} Name :  {name}")
    print(f"Year Entry : 25{student_ID[:2]} Last 4 Digit : {student_ID[-4:]} Department : Computer Engineering")

except:
    print("Invalid input")
