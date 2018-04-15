def room():

	length = float(input("what is the length of your room?"))
	

	width= float(input("what is the width of your room?"))



	area = length * width


	

	SUP = str.maketrans("2", "²")

	final  = "your room is " + str(area)+ "ft"+ "2"

	print (final.translate(SUP))

room()