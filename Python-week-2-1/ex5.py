def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def line_equation_verbose(x1, y1, x2, y2):
    print(f"({x1},{y1}) ==> ({x2},{y2})")

    # คำนวณค่าดิบ A, B, C
    A = y2 - y1
    B = x1 - x2
    C = (x2 * y1) - (x1 * y2)

    # f1: แสดงแบบตรง ๆ
    print(f"f1 ==> {A}x + {B}y + {C} = 0")


    # f2: ลดรูปด้วย gcd
    gcd_all = gcd(gcd(abs(A), abs(B)), abs(C))
    A2, B2, C2 = A, B, C
    if gcd_all != 0:
        A2 //= gcd_all
        B2 //= gcd_all
        C2 //= gcd_all
    print(f"f2 ==> {A2}x + {B2}y + {C2} = 0")

    # ปรับให้ A2 เป็นบวก (เพื่อไม่ให้เริ่มต้นสมการด้วยลบ)
    if A2 < 0:
        A2 *= -1
        B2 *= -1
        C2 *= -1

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

    if result.startswith("+"):
        result = result[2:]

    print(f"f3 ==> {result} = 0")
    print("===== End of program =====")
    
print(" *** Linear Formula ***")
x1, y1, x2, y2 = [int(i) for i in input("Enter x1 y1 x2 y2: ").split()]
line_equation_verbose(x1, y1, x2, y2)
