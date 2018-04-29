import sqlite3


db = "dogs_extended.db"

conn = sqlite3.connect(db)

c = conn.cursor()

# IF THE TABLE EXISTS AND YOU WANT TO GET RID OF IT

# c.execute('''   DROP TABLE favorite_dogs     ''')


c.execute('''

	CREATE TABLE favorite_dogs(
		id INTEGER Primary Key Autoincrement,
		name TEXT,
		age INTEGER
	)

	''')




conn.commit()
