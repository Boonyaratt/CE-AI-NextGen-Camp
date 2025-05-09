import math

def line_equation_verbose(x1, y1, x2, y2):
    print(" *** Linear Formula ***")
    print(f"Enter x1 y1 x2 y2: {x1} {y1} {x2} {y2}")
    print(f"({x1},{y1}) ==> ({x2},{y2})")

    # คำนวณค่าดิบ A, B, C
    A = y2 - y1
    B = x1 - x2
    C = (x2 * y1) - (x1 * y2)

    # f1: แสดงแบบตรง ๆ
    print(f"f1 ==> {A:+d}x + {B:+d}y + {C:+d} = 0")

    # f2: ลดรูปด้วย gcd
    gcd = math.gcd(math.gcd(abs(A), abs(B)), abs(C))
    A2, B2, C2 = A, B, C
    if gcd != 0:
        A2 //= gcd
        B2 //= gcd
        C2 //= gcd
    print(f"f2 ==> {A2:+d}x + {B2:+d}y + {C2:+d} = 0")

    # f3: ไม่แสดงเลข 1
    def term(value, var):
        if value == 0:
            return ""
        sign = "+" if value > 0 else "-"
        abs_val = abs(value)
        if abs_val == 1:
            return f" {sign} {var}"
        else:
            return f" {sign} {abs_val}{var}"

    result = ""
    result += term(A2, "x")
    result += term(B2, "y")
    if C2 != 0:
        sign = "+" if C2 > 0 else "-"
        result += f" {sign} {abs(C2)}"

    result = result.strip()

    # ลบเครื่องหมาย "+" ที่ไม่จำเป็น
    if result.startswith("+"):
        result = result[2:]

    # แสดงผล f3 ในรูปแบบที่ต้องการ
    print(f"f3 ==> {result} = 0")
    print("===== End of program =====")

# ===== เรียกใช้ =====
x1, y1, x2, y2 = [int(i) for i in input("Enter x1 y1 x2 y2: ").split()]
line_equation_verbose(x1, y1, x2, y2)
