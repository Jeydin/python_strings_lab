def concat(x, y):
	print(x + " " + y) 

concat("hello", "world")

def first_last(x):
	firstLetter = x[0]
	lastLetter = x[-1]
	print("First letter is " + firstLetter + " and last letter is " + lastLetter)
	
first_last("World")

def substring(x, y, z):
	fish = x[y:z]
	print(fish)
substring("alligator", 3, 8)

def lastFirst(x):
	space = x.find(" ")
	chicken = space + 1
	firstName = x[0:space]
	lastName = x[chicken:]
	print(lastName + ", " + firstName)
lastFirst("James Bond")

def replaceString(x, y, z):
	chicken = x[:x.find(y)]
	egg = len(chicken) + len(y)
	fish = x[egg:]
	print(chicken + z + fish)
replaceString("Computer science is fun.", "science", "programming")