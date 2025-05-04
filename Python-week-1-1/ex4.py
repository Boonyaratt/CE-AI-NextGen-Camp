print(" *** Distance *** ")
u,a,t=[float(i) for i in input("Enter Velocity Acceleration Time: ").split(',')]
# print(f"u={u}, a={a}, t={t}")

if u >= 0 and a >= 0 and t >= 0:
    s = u*t + (1/2)*a*t*t
    print(f"Your Distance = {s:.2f}")