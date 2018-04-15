def prime_check(number):
	quickCheck =  [0,1,2,3,5,7]
	if type(number) != int:
		print("This ({}) is not a number!".format(number))
		return
	elif number in quickCheck:
		print("{} is a prime number")
	elif number % 2 == 0:
		print("The number {} is not a prime number!".format(number))
	elif number % 3 == 0:
		print("The number {} is not a prime number!".format(number))
	elif number % 5 == 0:
		print("The number {} is not a prime number!".format(number))
	elif number % 7 == 0:
		print("The number {} is not a prime number!".format(number))
	else:
		print("{} is a prime number".format(number))

# prime_check(12)
# prime_check(111)
# prime_check(13)
# prime_check("Tom")

def palindrome_check(string):
	compareString = ""
	string = string.lower()
	if type(string) == str:
		for index in range(len(string)-1, -1 ,-1):
			compareString += string[index]
		if compareString == string:
			print("{} is a palindrome. Flipped version is {}.".format(string, compareString))
		else:
			print("{} is NOT  a palindrome. Flipped version is {}.".format(string, compareString))
	else:
		print("{} is not a string".format(string))


# palindrome_check("anna")
# palindrome_check("blahblahBlah")
# palindrome_check("Hannah")


def anagram_check(string1, string2):
	if type(string1) != str or type(string2) != str:
		print("Please provide correct inputs")
		return
	elif len(string1) != len(string2):
		print("{} is not an anagram of {}.".format(string1, string2))
	else:
		stringOne = string1.lower()
		stringTwo = string2.lower()
		listOfCharacters = list(stringOne)
		for character in stringTwo:
			if character in listOfCharacters:
				pass
			else:
				print("{} is not an anagram of {}.".format(string1, string2))
				return
		print("{} is an anagram of {}.".format(string1, string2))

# anagram_check("laksjda", "alskdjas")
# anagram_check("live", "Evil")


def caesarcypher():
	string = input("Please provide your message:\n")
	if type(string) != str:
		print("{} is not a string.".format(string))
	else:
		cypheredString = ""
		for character in string:
			if ord(character) in range(97, 97+26):
				characterNumber = ord(character)
				if (characterNumber + 3) > 122:
					difference = characterNumber + 3 - 122
					newCharacter = chr(97 + difference - 1)
					cypheredString += newCharacter
				else:	
					newCharacter = chr(characterNumber + 3)
					cypheredString += newCharacter
			elif ord(character) in range(65, 65+26):
				characterNumber = ord(character)
				newCharacter = chr(characterNumber + 3)
				cypheredString += newCharacter
			else:
				cypheredString += character
		print("\n")
		print("{} when ceasarfied is equal to {}.".format(string, cypheredString))
		print("\n")

# caesarcypher()



def roman_numerals():
	rawInput = input("Please give me a number! ")

	while rawInput.isdigit() != True:
		rawInput = input("No, I said a number! ")

	number_choice = int(rawInput)

	final_output_string = ""

	if number_choice // 1000 >= 1:
		final_output_string += number_choice//1000 * "M"
		number_choice -= 1000*(number_choice//1000)
	if number_choice // 500 >= 1:
		final_output_string += (number_choice//500) * "D"
		number_choice -= 500*(number_choice//500)
	if number_choice // 100 >= 1:
		final_output_string += (number_choice//100) * "C"
		number_choice -= 100*(number_choice//100)
	if number_choice // 50 >= 1:
		final_output_string += (number_choice//50) * "L"
		number_choice -= 50*(number_choice//50)
	if number_choice // 10 >= 1:
		final_output_string += (number_choice//10) * "X"
		number_choice -= 10*(number_choice//10)
	if number_choice // 5 >= 1:
		final_output_string += (number_choice//5) * "V"
		number_choice -= 5*(number_choice//5)
	if number_choice // 1 >= 1:
		final_output_string += (number_choice//1) * "I"
		number_choice -= 1*(number_choice//1)
	print("The number {} in Roman Notataion is {}.".format(rawInput, final_output_string))

roman_numerals()












