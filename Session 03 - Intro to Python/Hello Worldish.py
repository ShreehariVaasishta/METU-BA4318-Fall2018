# It is customary to first write Hello World in any programming class. 
print("Hello World. This is BA4318.")
# Python variables need not be defined first to be used. Whenever we use a variable for the first time. They get to be defined.
# Integers, Floats, Complex Numbers and Booleans are built-in types
x = 2
print(x)
# Expressions are what these variables are used in
x = (x + 2) * (x-1)
print(x)
# Variable types are also flexible. So the variable names can change type based on result on the expression. 
x = x / 3
print(x)
# Let's import a library in the middle of the file just because we decide we need it
import math
xfloor = math.floor(x)
xceil = math.ceil(x)
# print function can display multiple values. No need to combine them into one large string. 
print("x floor is: ", xfloor," x ceil is: ", xceil)
# boolean values are True and Fals
abool = True
print(abool)
# We can directly assign the results of boolean expressions to boolean variables
anotherbool = x > 1
print(anotherbool)
# We are done for this very short introduction. 
print("End of Hello World.")