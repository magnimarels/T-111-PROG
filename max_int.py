# Write a code that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.
# The max_int will be determined by an if statement to see if the input is higher than the previous input
# When there is a negative number input the code will go and print the max_int
num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
while num_int >= 0:
    if max_int <= num_int:
        max_int = num_int
        num_int = int(input("Input a number: ")) 
    elif num_int >= 0:
        num_int = int(input("Input a number: "))    # Do not change this line
    else:
        print("The maximum is", max_int)    # Do not change this line

# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line
