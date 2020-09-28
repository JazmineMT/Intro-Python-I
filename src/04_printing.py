"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print(f" x is {x}  y is {y} z is {z}")

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))
txt = " x is {num} y is {num} z is {sentence}"
print(txt.format(num = x, num2 = y, sentence = z))