def print_pyramid_v2(height):
    # Loop for each level of the pyramid
    for i in range(1, height):
        # Print leading spaces
        print(' ' * (height - i), end='')

        # Print the left side, inside dots, and right side
        print('/' + '.' * (2 * i - 2) + '\\')

    # Print the base of the pyramid
    print('/' + '_' * (2*height-2) + '\\')

    print("===== End of program =====")

print(" *** Pyramid-V ***")
# Get input from the user
height = int(input("Enter height : "))

# Check if the number is positive
if height <= 0:
    print("!!!Please enter positive number!!!")
else:
    # Call the function to print the pyramid
    print_pyramid_v2(height)