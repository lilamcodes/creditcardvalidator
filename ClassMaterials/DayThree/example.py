import csv


from datetime import datetime

start = datetime.now()

print(start)

for i in range(1000000):
	x = i

end = datetime.now()

print(end)

print("Total Time", end-start)

# with open("words.txt","r+") as wordsFile:
# 	string_rep = wordsFile.read()
# 	# string_list = string_rep.split()
# 	wordsFile.write("\n Tommy has written to this file.")

# with open("Book.csv") as bc:
# 	csvlines = csv.reader(bc)
# 	for item in csvlines:
# 		print(item)
# # 	csvlines = csv.DictReader(bc)
# # 	for row in csvlines:
# # 		print(row["Name"], row["Zip"])
# # 		if row["Name"] == "John":
# # 			change_name()
# # 		row["Name"] = "New Name for that person"
# # 		row["Account Balance"] = 0
# # 	# csvlines.write("new.csv")


