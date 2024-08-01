import sqlite3 as lite
con = lite.connect('lnm.db')
cur=con.cursor()
cur.execute("SELECT * FROM Cars")
rows = cur.fetchall()
con.close()
#print(rows)
for row in rows:
    print(row)