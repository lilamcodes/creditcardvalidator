def roman():


	rawInput = input("Please provide me a number: (Positive please!) ")


	while rawInput.isdigit() == False:
		rawInput = input("Please provide me a number: (Positive please!) ")

	number = int(rawInput)

	final_string = ""

	if number//1000 >= 1:
		final_string += "M" * (number//1000)
		number -= (number//1000) * 1000
	
	if number//500 >= 1:
		final_string += "D" * (number//500)
		number -= (number//500) * 500
	if number//100 >= 1:
		final_string += "C" * (number//100)
		number -= (number//100) * 100
	if number//50 >= 1:
		final_string += "L" * (number//50)
		number -= (number//50) * 50
	if number //40 == 1:
		final_string += "XL"
		number -= 40
	if number//10 >= 1:
		final_string += "X" * (number//10)
		number -= (number//10) * 10
	if number //9 == 1:
		final_string += "IX"
		number -= 9
	if number//5 >= 1:
		final_string += "V" * (number//5)
		number -= (number//5) * 5
	if number//1 >= 1:
		final_string += "I" * (number//1)
		number -= (number//1) * 1



	print("Here is our roman output:", final_string)

roman()