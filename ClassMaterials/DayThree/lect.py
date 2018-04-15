import csv

with open('toolhire.csv') as file:
    my_reader = csv.reader(file)
    # The reader object is not limited to i les. It can also take a list of strings
    # as its input instead.
    rowOne = list(my_reader)
    print(type(rowOne)) 
    print((rowOne)) 
print("Row One",rowOne) 

row_list = []
with open('toolhire.csv') as file:
    my_reader = csv.reader(file)
    for row in my_reader:
        row_list.append(row)
    
print("Row list",row_list)

with open("myfile.csv", 'w', newline='') as data:
    data_writer = csv.writer(data)
    for row in row_list:
        data_writer.writerow(row)