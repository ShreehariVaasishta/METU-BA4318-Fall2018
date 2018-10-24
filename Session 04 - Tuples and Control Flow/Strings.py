# Let's play with strings and dictionaries
hello = "Hello"
world = "World"
h = hello[0]
print("h: ", h)
size = len(hello) # should be 5
print(size)
helloworld = hello + " " + world + "!"
print(helloworld)
mask = "01234556789ABCDEF"
masks = 2 * mask
print(masks)
escapes = "\' \" \\ \t after tab \n"
print(escapes)
first = "first"
second = "second"
nochar = ""
space = " "
tab = "\t"
# join joins lists of strings into a string
print(nochar.join([first, second]) )
print(space.join([first, second]) )
print(tab.join([first, second]) )
# split splits strings
sentence = "This is a sentence with   \t \n lots of whitespace"
wordlist = sentence.split()
print("The word list: ", wordlist)
codeword = "This##is a coded##word"
uncoded = codeword.split("##")
print("Uncoded: ", uncoded)
# conversion of numbers in string format
numstring1 = "123.456"
number = float(numstring1)
numstring2 = "123,456"
# number2 = float(numstring2) # This does not run

# a dictionary, empty at first
dict = {}
dict[0] = "Added with key 0"
dict[1] = "Added with key 1"
dict[25] = "Added with key 25"
dict["Bora"] = "Added with key \"Bora\" as String"
# Anything that is immutable can be used as a key. Numbers and strings are usual and safe choices. Tuples are immutable lists are not
dict[(0,1,2,3)] = "Added with a tuple as a key"