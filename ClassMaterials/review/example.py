a = 1
b = 2
c = 3

x = "Word"

list1 = [a,b,c]

list1.append(4)

# For loop

for item in list1:
	print(item)

print(list1[0])

counter = 1
print(counter)
print(list1)
counter += 1


while counter < 100:
	print(counter)
	print(list1)
	counter += 1

if counter == 100:
	print("While loop has ended")




dict1 = {"key":"value", "Apple": 10}

print(dict1)

print(dict1["Apple"])
