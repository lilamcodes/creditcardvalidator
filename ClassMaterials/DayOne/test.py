def vowel(word):

#create list of vowels as reference
	vowels=["a","e","i","o","u"]
	if word in vowels:  
		return True
	else:
		return False

# vowel("a")

def piglatin():
	word=input("enter word")
	# wordlower=word.lower()


	if len(word)>0 and word.isalpha():
		first=word[0] #why do we have to label it first?
	# if vowel(word[0]):
	# 	print (word + "ay")

		if vowel(first):
			new_word1 = word[0:len(word)] + "yay"
			print(new_word1)

		else:  # I need help understanding this part
			for ch in word:
				if vowel(ch):
					loc = word.index(ch)
					print(loc)
					new_word2= word[loc:len(word)] + word[0:loc] + "ay"

					print (new_word2)

	else:
		print("empty")

		# for ch in word:
		# 	if vowel(ch):
		# 		print("hello")
		# 	else:
		# 		print(ch)






	# 	i=1
	# 	while (vowel(word[i])==false) and (i<len(word)):
	# 		i+1

	# print(word[i:]+word[:i+'ay'])


piglatin()


# def one(a,b):
# 	total = a + b

# one(4)