try:
    print(" *** Transform second ***")
    raw_input = input("Enter seconds : ").replace('_', '')  # Remove underscores

    # Check if input contains a decimal point
    if '.' in raw_input:
        print(f'! ! ! please enter a whole number ==> {raw_input}')
        print(" --- program end --- ")
        exit()  # Exit the program after invalid input
    
    # Check if input is not a valid number
    if not raw_input.isdigit() and not (raw_input.startswith('-') and raw_input[1:].isdigit()):
        print(f'! ! ! please enter a whole number ==> {raw_input}')
        print(" --- program end --- ")
        exit()  # Exit the program after invalid input
    
    # Convert to integer after validation
    sec = int(raw_input)

    # Check if the number is negative
    if sec < 0:
        print(f'This number ({sec}) is not VALID !!!')
        exit()  # Exit the program after invalid input
    
    original_sec = sec

    # Calculate time units
    week = sec // (60 * 60 * 24 * 7)
    sec %= (60 * 60 * 24 * 7)

    day = sec // (60 * 60 * 24)
    sec %= (60 * 60 * 24)

    hour = sec // (60 * 60)
    sec %= (60 * 60)

    minute = sec // 60
    sec %= 60

    # Prepare output
    output = f"{original_sec:,} seconds ==>"

    if week:   output += f" {week} weeks"
    if day:    output += f" {day} days"
    if hour:   output += f" {hour} hours"
    if minute: output += f" {minute} minutes"
    if sec:    output += f" {sec} seconds"

    print(output)
    print(" --- program end --- ")

except ValueError as e:
    print(e)
