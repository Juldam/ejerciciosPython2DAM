import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="pruebas"
)

cursor=mydb.cursor()

sql="INSERT INTO usuarios (name, surname) VALUES (%s, %s)"
val=("Rocio", "Alonso")

cursor.execute(sql, val)

mydb.commit()

print(cursor.rowcount, " filas insertadas.", cursor.lastrowid)