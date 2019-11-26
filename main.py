"""Python For Everybody week 3 code"""

# variables and data types
print("Hello World!")

x = 5 + 9
print(x)

y = ("5 + 9")
print(y)

"""Python For Everybody week 4 code"""

# Booleans
x = int(input("please enter a number for x: "))
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

print(10 > 9)
print(10 == 9)
print(10 < 9)

"""Python For Everybody week 5 code"""

x = 1  # int
y = 3.7  # float
z = 1j  # complex

# For Loops
# Print all numbers from 0 to 7, and print a message when the loop has ended
for x in range(8):
    print(x)
else:
    print("All Done!")

"""Python For Everybody week 6 code"""


# Function Call
def my_function():
    print("Hello User!")


my_function()


# Parameters
def hurley_fam(fname):
    print(fname + " Hurley")


hurley_fam("Rylie")
hurley_fam("Paul")
hurley_fam("Jennifer")


# Arguements
def middle_child(child3, child2, child1):
    print("The middle child is " + child3)


middle_child(child1="Sean", child2="Flynn", child3="Jacob")

"""Python For Everybody week 7 code"""

"""
code pulled from W3schools
__author__ = w3Schools
"""

# Print a message once the condition is false
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# Exit the loop when i is 3
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
