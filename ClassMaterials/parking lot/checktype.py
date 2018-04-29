
control = False

while control == False:
	number = input("Please give me number: ")
	if number.isdigit() == True:
		number = int(number)
		control = True

award_player()

# print(number)
# print(type(number))
# print(dir(number))

answer = number * 20

print("Your answer is {}".format(answer))