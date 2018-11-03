# first ever function definition
def absolute(x):
    if x > 0 :
        return x
    else:
        return -x
    
variable = -5
print("variable is:", variable)
abs = absolute(variable)
print ("absolute value is:", abs)

# call by specifying parameter name
def areatriangle(width, height):
    return width * height / 2

w = 5
h = 10
print("area is:", areatriangle(width=w, height=h) )

# default parameters
def areacircle(r, pi = 3.14159):
    return pi*r*r

radius = 10
area1 = areacircle(radius)
area2 = areacircle(radius, 3)
area3 = areacircle(radius, pi = 3.14)
print("area1: ", area1, "area2: ", area2, "area3: ", area3)

# variable number of arguments
def summation(*numbers):
    # numbers is treated as a list
    if len(numbers) == 0:
        # no parameters
        return 0
    else:
        # there are some numbers
        sum=0
        for number in numbers:
            sum = sum + number
        return sum

total1 = summation (1,2,3,4,5)
print("total1:", total1)

# mynumbers = (1,2,3,4,5)
# total2 = summation (mynumbers)
# print("total2:", total2)

# list as parameter
def sumbylist(list1):
    if len(list1) == 0:
        return 0
    else:
        sum=0
        for number in list1:
            sum = sum + number
        return sum

mynumbers = [1,2,3,4,5]
total3 = sumbylist (mynumbers)
print("total3:", total3)

def summation2(*numbers):
    # numbers is treated as a list
    if len(numbers) == 0:
        # no parameters
        return 0
    else:
        # there are some numbers
        sum=0
        mylist = list(numbers)
        for number in mylist:
            sum = sum + number
        return sum

total4 = summation (1,2,3,4,5)
print("total4:", total4)


