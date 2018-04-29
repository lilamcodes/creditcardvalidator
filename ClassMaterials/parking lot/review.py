# 1. Dictionary has copy(). What is it?


# DEEP
dict1 = {"apple": 4}

dict2 = dict1.copy()

dict1["apple"] = 3

# print("dict1", dict1)
# print("dict2", dict2)


# SHALLOW

dict1 = {"apple": [1,2,3]}
dict2 = dict1.copy()
copy = dict1 

dict1["apple"].append(5)

# print("dict1", dict1)
# print("dict2", dict2)
# print("copy with equal sign", copy)

# 2. How to open a csv? How to open a text file?

# NOTE the string in the open() function is a path!!!! not just the name.
# If no path (such as .., or /) is in the string, it assumes the file is right next to it.

with open("example.txt") as examp:
	# read() makes a string copy of the file.
	exampString = examp.read()
	# print(exampString)
	# print(type(exampString))


import csv

with open("example.csv") as examp:
	# WITH reader()
	# exampCSV = csv.reader(examp)
	# for row in exampCSV:
	# 	print(row)

	# WITH DictReader()
	exampCSV = csv.DictReader(examp)
	# for row in exampCSV:
	# 	print("State",row["State"])
	

# 3. sorted()? What is it?

def add(number1, number2):

	return number1 + number2

def func(number):
	return number * -1

x = [3,2,4]
# y = sorted(x, key=func)
y = sorted(x)

# print("x",x)
# print("y",y)


# 4. append() vs insert()

exampleList = [1,2,3,4]

# Example with append()
# Adds the value to the end automatically! No choice!!

exampleList.append(5)

# print(exampleList)

# Example with insert
# Adds the value to the index position you say! Also, does not get rid of
# the value that is already at that index position.

exampleList.insert(0, 5)

print(exampleList)











