

#1.
def greetings():
	name_input = input("Please tell me your name: ")
	print("Hello {}! Nice to meet you!".format(name_input))

#2.
def area():
	length = float(input("Please provide the length: "))
	width = float(input("Please provide the width: "))

	print("The area of your space is {}ft".format(length*width))

#3.
def bottles():
	smalldep = 0.1
	largedep = 0.25

	numOfSmall = float(input("Large Bottles: "))
	numOfLarge = float(input("Small Bottles: "))

	print("Your total refund is  ${}".format(numOfSmall*smalldep + numOfLarge * largedep))

#4.
def vowels():
	character = input("Please provide a character: ")

	if character in "aeiou":
		print("This is a vowel")
	elif character == "y":
		print("{} is a special case. It can be both.")
	elif character.isalpha() == True:
		print("The character {} is not a vowel".format(character))
	else:
		print("The character {} is not in the english alphabet".format(character))

#5.
def equilateral():
	side1 = input("Side 1: ")
	side2 = input("Side 2: ")
	side3 = input("Side 3: ")

	if side1 == side2 and side2 == side3:
		print("Equilateral")
	elif side1 == side2 or side2 == side3 or side1 == side3:
		print("Isosceles")
	elif side1 != side2 and side1 != side3 and side2 != side3:
		print("Scalene")


#6.
def triangles(number):

	for i in range(1,number+1):
		# print("first i", i)
		print("*"*i)
	for i in range(number-1,0,-1):
		# print("second i", i)
		print("*"*i)

#7. 
def odd_or_even():
	int_input = int(input("Number: "))

	if int_input % 2 == 0:
		print("Even")
	elif int_input % 2 == 1:
		print("Odd")
	else:
		print("Not a number!")

#8.
def fizzbuzz():

	for i in range(1,101):
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)

#9.
def multiplication_table(min_num, max_num):
    
    # just space before the top row
    print("    ", end = " ")
    '''
    Display the top row of tables
    '''
    for i in range(min_num, max_num + 1):
        print("{:4}".format(i), end=" ")
    print()
    '''
    Display the table
    '''
    for i in range(min_num, max_num + 1):
        print("{:4}".format(i), end=" ")
        for j in range(min_num, max_num + 1):
            print("{:4}".format(i*j), end=" ")
        print()



# multiplication_table(1, 20) 
















