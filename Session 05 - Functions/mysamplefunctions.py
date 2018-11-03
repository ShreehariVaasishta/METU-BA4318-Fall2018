""" mysamplefunctions """
def absolute(x):
    if x > 0 :
        return x
    else:
        return -x
    
# call by specifying parameter name
def areatriangle(width, height):
    return width * height / 2

def areacircle(r, pi = 3.14159):
    return pi*r*r

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

def sumbylist(list1):
    if len(list1) == 0:
        return 0
    else:
        sum=0
        for number in list1:
            sum = sum + number
        return sum

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
   


