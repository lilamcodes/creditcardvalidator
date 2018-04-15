# x=10

# while x > 5:
	# print x

	# print("yip!!")
	# x = x - 1


# print("while done")

# A prime number is an integer greater than 1 that is only divisible by one and itself. 
# Write a function that determines whether or not its parameter is prime, returning True if it is, and False otherwise. 
# Write a main program that reads an integer from the user and displays a message indicating whether or not it is prime. 
# Ensure that the main program will not run if the file containing your solution is imported into another program.

# ex 1

def prime():

	number=int(input("enter a number"))


	for i in range(2,number):
		if number>1 and  number % i !=0:
				print(number + "is a prime number")

		else:
			print(number + "is not a prime number")


prime()