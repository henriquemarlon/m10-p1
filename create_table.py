import sqlite3
con = sqlite3.connect("sqlite.db")
cur = con.cursor()

cur.execute("CREATE TABLE tasks (title TEXT, content TEXT)")

con.commit()
con.close()