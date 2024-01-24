#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
#For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

def reverse_digits(number):
    # Convert the number to a string and reverse it
    reversed_str = str(number)[::-1]

    # Print each digit with a space separating them
    for digit in reversed_str:
        print(digit, end=" ")

num = 7536

# Extract and print each digit in reverse order
print("Digits in reverse order:")
reverse_digits(num)