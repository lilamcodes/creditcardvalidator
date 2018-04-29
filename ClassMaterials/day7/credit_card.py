class Validator:

	def __init__(self, card_number):
		self.card_number = str(card_number)
		self.card_type = self.establish_type()
		self.valid = self.validate()


	def establish_type(self):
		number = self.card_number

		if len(number) in (15,16):
			if len(number) == 15 and number[0:2] in ("34","37"):
				return "AMEX"
			elif len(number) == 16 and number[0:2] in ("51", "52", "53", "54", "55"):
				return "Mastercard"
			elif len(number) == 16 and number[0] == "4":
				return "Visa"
			elif len(number) == 16 and number[0]=="3" or len(number) == 16 and number[0:5] == "6011":
				return "Discover"
			else:
				return "Unknown Type"
		else:
			print("Not one of the types.")
			return "Unknown Type"

	def validate(self):
		cc_number = self.card_number[::-1]
		list_of_values = []
		for index in range(0,len(cc_number)):
			value = int(cc_number[index])
			if index % 2 ==1:
				if value * 2 >=10:
					list_of_values.append(1)
					list_of_values.append(value*2-10)
				else:
					list_of_values.append(value*2)
			else:
				list_of_values.append(value)

		total = sum(list_of_values)
		print("Total", total)
		if total%10 == 0:
			print("Valid Card:",self.card_number)
			return True
		else:
			print("Invalid Card:",self.card_number)
			return False


rawInput = input("Please input card number")

print("Raw", rawInput)
while rawInput.isdigit() == False and len(rawInput)<14 and len(rawInput)>17:
	rawInput = input("Please input card number")

cc1 = Validator(rawInput)

print(Validator().validate(cc1))
print(cc1.card_type)
print(cc1.card_number)





