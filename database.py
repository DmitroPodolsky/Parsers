import sqlite3
conn = sqlite3.connect("ban.db")
sql = "CREATE TABLE hello_hotels (name TEXT, adress TEXT, description TEXT, photo TEXT)"
#sql="SELECT * FROM books"
cursor = conn.cursor()
cursor.execute(sql)
#res = cursor.fetchall()
#for r in res:
    #print(r)
conn.close()