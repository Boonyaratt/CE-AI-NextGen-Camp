def is_sorted_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

# รับค่าจำนวน 5 ตัวจากคีย์บอร์ด
numbers = list(map(int, input("Enter numbers : ").split()))

# ตรวจสอบว่าเรียงจากน้อยไปมากหรือไม่
print(is_sorted_ascending(numbers))
