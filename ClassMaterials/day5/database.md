# Database and SQLite3 Lecture

## SQL COMMANDS

### Create Table
```
CREATE TABLE employees (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		firstName TEXT,
		lastName TEXT,
		salary REAL,

)
```




- The structure of the command for creating a TABLE is shown above. After "CREATE TABLE", the name of the table is written and then within the parentheses are what each column is called, followed by the data type expected.

### SELECT STATEMENT
```
SELECT * FROM employees
```
- This statement allows you to read/grab information from the database.
- It always starts with SELECT and then what is after FROM is the table you would like.
- Translation: SELECT **something** FROM **table_name**

# WHERE STATEMENT
```
SELECT * FROM employees WHERE firstName = 'John';
```
- WHERE is used to provide a condition for what you are looking for.
- For example, the above SQL command asks for all the employees that have their firstName attribute as 'John'.

### SQLITE3 - Setting up Python Script
```
db = "students.db"

conn = sqlite3.connect(db)

c = conn.cursor()

c.execute("Whatever command you would like"

)

conn.commit()
```
- Above, "conn" is equal to the sqlite3 object invoking a connect() funciton with a database name as a string.
- Then, we create a cursor object which is an object that can run SQL commands on the database. Think of Cursor as the navigator who you can provide directions for where to go.
- .execute() takes a SQL command as a string and executes on the table/database.
- Finally, .commit() allows to commit your changes to the database. That means that the changes made should be saved. For more info, look up "SQL rollback transaction".

### Resources 
- SQLite3 Documentation
	- https://www.sqlite.org/docs.html
