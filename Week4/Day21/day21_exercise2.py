# This is a program for the validation of input

while True:  # creates a loop that continually runs until you manually stops it
    print("running")

    break  # this will stop the loop from running indefinitely and will exit the loop immediately when it is executed

# To check if input is a number (only digits)

text = "123"
print(text.isdigit())  # returns True if all characters in the string are digits, otherwise returns False

text = "abc"
print(text.isdigit())  # returns False because the string contains non-digit characters