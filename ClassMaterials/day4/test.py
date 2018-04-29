# Exercise 1: Please write a program which count and print the numbers of each character, from file letters.txt, in a string input by console.

# Example: If the following string is given as input from file letters.txt to the program:

# abcdefgabc

# Then, the output of the program should be:

# a,2 c,2 b,2 e,1 d,1 g,1 f,1

# Hints: Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.


read=open('letters.txt', 'r')

file_contents = read.read()

contentList= {}

	for letter in file_contents:
		if letter not in contentList:
		contentList[letter] = 1


	elif letter in file_contents:
		contentList[letter] += 1

	for letter in contentList

print(contentList)


