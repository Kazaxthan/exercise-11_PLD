#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
#For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

def reverse_digits(number):
    # convert the number to string
    reversed_str = str(number)[::-1]

    #  digit with a space separating them
    for digit in reversed_str:
        print(digit, end=" ")

# get user input
user_input = input("Enter an integer: ")

try:
    # swith the input to integers 
    num = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Extract and print each digit in reverse order
print("Digits in reverse order:")
reverse_digits(num)