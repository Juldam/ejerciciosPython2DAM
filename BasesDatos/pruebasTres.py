import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="pruebas"
)

mycursor=mydb.cursor()

sql="SELECT * FROM usuarios WHERE name = %s"
val=('Julian',) #LA COMA ES SUPER IMPORTANTE, SI NO, NO VA!!!

mycursor.execute(sql, val)

myresult=mycursor.fetchall()

for i in myresult:
    print(i)

mycursor.close()