# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard


# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even(number):
    if number % 2 == 0:
        even = True
    else:
        even = False
    return even


if __name__ == "__main__":
    num = input("Enter a number: ")
    num = int(num)
    print(is_even(num))
