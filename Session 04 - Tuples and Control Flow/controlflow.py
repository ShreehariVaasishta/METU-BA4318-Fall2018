# program flow is basically branching and looping in any language
# we first cover the while looping (to be in line with our textbook)
reserve = 0
while reserve < 100:
    print("Current reserve is, ", reserve)
    incoming = int( input("Please make a deposit on the reserve:") )
    reserve = reserve + incoming
else:
    print("Exiting loop with reserve:", reserve)
    
# then we consider the if statement
if reserve > 500:
    print("We deposited really fast")
elif reserve > 200:
    print("We deposited OK")
else:
    print("We barely passed 100")
# note that there is no switch-case in Python

wallet = [1,1, 5, 5, 5, 10, 10, 10, 100, 100]
sum = 0
for note in wallet:
    sum = sum + note
print("Sum is:", sum)

# when there is a list of lists or tuples things get interesting
coordinates = [ (0,0), (1,2), (4,5)]
area = 0
for x,y in coordinates:
        area = area + x*y
print("Area under curve is approximately: ", area)
# when you have a number of tuples with same size
xs = (0,1,4)
ys = (0, 2, 5)
# then we you can use the zip function
zipped = zip(xs,ys)
zippedlist = list(zipped)
print (zippedlist)

# how about a dictionary?
emails = {}
emails["METU"] = "gbora@metu.edu.tr"
emails["Bilkent"] = "bora.gungoren@bilkent.edu.tr"
emails["Gmail"] = "bora.gungoren@gmail.com"

for k in emails:
    print("Key: ", k)

for k,v in emails.items():
    print("Key: ", k, " value:", v)
    

