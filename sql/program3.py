import sqlite3
cars = [
    (1, 'Audi', 4324),
    (2,'Merceedes', 78732),
    (3, 'Skoda', 78432),
    (4, 'Volvo', 78483),
    (5, 'Bently', 83634)
]

con = sqlite3.connect('lnm.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
cur.executemany("INSERT INTO Cars VALUES(?,?,?)",cars)
con.commit()
con.close()
print("Values inserted")