import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="pruebas"
)

cursor=mydb.cursor()

sql="INSERT INTO usuarios (name, surname) VALUES (%s, %s)"
val=[
    ("Pedro", "Sanchez"),
    ("Raul", "Pérez"),
    ("Elisa", "García")
]
cursor.executemany(sql, val) #El executemany parece que itera en la tupla de valores que hemos creado anteriormente. Aí no tenemos que hacer un insert o un cursor.execute por cada fila que queremos insertar

mydb.commit()

print(cursor.rowcount, " filas insertadas.")