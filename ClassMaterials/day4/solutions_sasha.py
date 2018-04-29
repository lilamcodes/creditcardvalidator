def count_letters():
	# Grab File Name
	file_name = input("Please provide a file name: ")

	while "." not in file_name:
		print("Check if the following is correct: {}".format(file_name))
		file_name = input("Please Try Again: ")


	with open(file_name) as file:
		file_string = file.read()
		
		count_dict = {}

		# Populate the dictionary with counts of each letter
		for character in file_string:
			if character in count_dict:
				count_dict[character] += 1
			elif character not in count_dict:
				count_dict[character] = 1

		# Print the final output
		for info in count_dict.items():
			print("{},{}".format(info[0],info[1]))

# count_letters()

def count_words(fileName, n):

	# n = input("How many records do you want to see? ")
	# while n.isdigit()== False:
	#   n = input("How many records do you want to see? ")
	# n = int(n)

	with open(fileName) as art:
		articleString = art.read()
		punctuation = ("!",",","?",".",":",'"',"%","\n","(",")","$")


		withOutPunc =  "".join(c.lower() for c in articleString if c not in punctuation)

		list_of_words = withOutPunc.split(" ")

		word_dict = {}

		for word in list_of_words:

			if word not in word_dict:
				word_dict[word] = 1
			elif word in word_dict:
				word_dict[word] += 1

		sorted_keys = sorted(word_dict, key=word_dict.get, reverse=True)[:n]
		for index, key in enumerate(sorted_keys):
			print('{}. "{}" appears {} times.'.format(index+1, key, word_dict[key]))



count_words("article.txt", 5)











