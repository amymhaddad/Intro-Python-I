# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
    return bool(num % 2 == 0)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

user_number = is_even(num)
print(user_number)

# Print out "Even!" if the number is even. Otherwise print "Odd"
if user_number == True:
    print("Even!")
else:
    print("Odd")
