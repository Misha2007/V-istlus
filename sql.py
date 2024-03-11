import sqlite3


# filename to form database
# file = "auto_database.db"


# try:
#     conn = sqlite3.connect(file)
#     print("Database Sqlite3.db formed.")
# except:
#     print("Database Sqlite3.db not formed.")

connection = sqlite3.connect("auto_database.db")

cursor = connection.cursor()

# cursor.execute("CREATE TABLE auto_table(model str, price float, year int);").fetchall()

rows = cursor.execute("""SELECT * FROM auto_table""").fetchall()

# connection.commit()

print(rows)