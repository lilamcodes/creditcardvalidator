
class Validator:
	def __init__(self, card_number,):
		self.card_number=card_number
		self.type=self.card_type()
		self.valid = self.validate()



	def card_type(self):

		if self.card_number.isdigit():
			if self.card_number[0]==4 and len(self.card_number)==16:
				print ("Visa")
				return "visa" 
			elif self.card_number[0:2] in ["51","52","53","54","55"] and len(self.card_number)==16:
				print ("Mastercard")
				print(self.card_number)
				return "mastercard"
			elif self.card_number[0,1]==(3,4) or(3,7) and len(self.card_number)==16:
				print ("Amex")
				return "amex"
			elif self.card_number[0]==(3) and len(self.card_number)==15:
				print ("Discover")
				return "discover"
			else:
				print ("invalid")
				return False

	def validate(self):
	
		card_number_list=list(map(int,self.card_number))# to create a list of integers
		card_number_list.reverse()
		print(self.card_number)
		print(card_number_list)
		for i in range(1,len(card_number_list),2):
			card_number_list[i]=int(card_number_list[i])*2
		print(card_number_list)
		new_list=list(card_number_list) # create a new list
		tupples=[]
		for i in range(1,len(card_number_list),2):
			if(card_number_list[i]>=10):

				val=list(str(card_number_list[i]))
				int_val = [int(x) for x in val] # for convert each str parameters in the list in INT
				tup_val=tuple(int_val)
				print(int_val) 
				tupples.append(tup_val)
				new_list[i]=0 #add the list to the new list

		result1=sum(new_list)
		tupple_result=list(map(sum, zip(*tupples)))
		result2=sum(tupple_result)
		total_result=result1+result2    
		print(new_list)
		print(tupples)
		print(result1)
		print(result2)
		print(total_result)
		if(total_result%10==0):
			print("Its valid")
			return True
		else:
			print("Its not valid")
			return False
		
	
	
card_number=(input("Please Enter the 15 or 16 digits of card number: "))

v=Validator(card_number)

