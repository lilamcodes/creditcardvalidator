import random

def reverse():
	
	possibles = []
	while len(possibles) <= 200:
		x = [random.choice(range(10)) for i in range(16)]
		while sum(x) % 10 != 0:
			x = [random.choice(range(10)) for i in range(16)]
		possibles.append(x)
	for possible in possibles:
		print(possible)

reverse()