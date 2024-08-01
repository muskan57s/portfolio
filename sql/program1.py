import sqlite3
con = sqlite3.connect('lnm.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTs CAR")
cur.execute('''CREATE TABLE Cars(
    Id INT,Name TEXT, Price INT)''')

print("table cars created.")
cur.execute("INSERT INTO Cars VALUES(11,'Audi',52642)")
cur.execute("INSERT INTO Cars VALUES(21,'Mercedes',57642)")
con.commit()
con.close()
print("Values in table car inserted")