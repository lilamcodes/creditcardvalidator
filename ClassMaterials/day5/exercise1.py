'''
EXERCISE 1 - CREATING A DATABASE

- Create a database called "Students"

- Create one table called "student_info":
	- Table 1:
		- Columns:
			- id PRIMARY KEY
			- First Name STRING
			- Last Name STRING
			- Age INTEGER
			- Homeroom STRING


'''

'''
EXERCISE 2 - SEEDING A DATABASE

- Create a database called "Students"

- INSERT into the database the following values:
	- Bob, Bobby, 19, Beetle
	- John, Johnson, 16, Grasshopper
	- Sally, Turner, 17, Beetle
	- Eric, Cartman, 16, Grasshopper
	- Kyle, Broflowsi, 16, Mantis
	- Stan, Marsh, 19, Grasshopper
	- Chris, Griffin, 18, Mantis 

'''

'''
EXERCISE 3 - WRITE THE QUERY TO ACCESS THIS INFORMATION

1. Give me all students in the table.

2. Give me all students in the Homeroom "Grasshopper"

3. Give me all students that are Age 16.

4. Give me all students that are older than 16.

5. Give me the ages of all students in Homeroom "Mantis"

6. Give me all the UNIQUE Homerooms for students of age 16

'''

x = 27


for name in names:
	insert1 = '''

		INSERT INTO student_info(name,lname,age, class)
		VALUES({},{},{})

	'''.format(name, lname, age)

x = '''
	UPDATE student_info SET age = 28 WHERE name = "Stan" 



'''



print(insert1)


# curs.execute(insert1)








