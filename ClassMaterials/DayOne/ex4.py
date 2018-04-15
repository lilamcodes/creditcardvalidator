def vowels():

	letter=input("Enter a letter")

	if letter in ["a","e","i","o","u"]:
		print ("your letter is a vowel")
	elif letter =="y":
		print ("sometimes y is a vowel")
	else:
		print("this is not a vowel")

vowels()