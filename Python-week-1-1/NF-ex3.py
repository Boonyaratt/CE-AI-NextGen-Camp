try:
    hour, min, sec = input("Enter hour, min, sec : ").split(',')

    hour = int(hour)
    min = int(min)
    sec = int(sec)

    if not (0 <= hour < 24):
        raise ValueError("error")
    if not (0 <= min < 60):
        raise ValueError("error")
    if not (0 <= sec < 60):
        raise ValueError("error")

    print(f"current time is {hour:02}:{min:02}:{sec:02}")

except ValueError:
    print("error")
