def bottle():
	smallbottles=int(input("How many less than one litre bottles do you have?"))

	largebottles=int(input("how many bottles greater than one litre do you have"))

	totalsmalldeposit=int(smallbottles ) * .10

	totallargebottles=int(largebottles) * .25

	totaldeposit= int(totalsmalldeposit) + int(totallargebottles)


	final  = "Your have " + str(totalsmalldeposit)+ " small bottles and "+ str(totallargebottles) +" large bottles.  Your total refund is " + "$" + str(totaldeposit) 

	print(final)





bottle()