import pymysql

def conectar():
    mydb=pymysql.connect(
        host="localhost",
        user="root",
        passwd="12345",
        db="extraescolares"
    )
    return mydb

def introducirAlumno():
    print("Seleccione la actividad: ")
    db=conectar()
    cursor=db.cursor()
    sql="SELECT codactividad, nomactividad FROM actividad"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    while True:
        for i in resultado:
            print(str(i[0])+" - "+str(i[1]))
        print(str(len(resultado)+1)+" - Otro")
        try:
            resp=int(input())
            if resp<1 or resp>len(resultado)+1:
                print("Opción incorrecta. EScoja de nuevo")
            else:
                break
        except ValueError:
            print("Opción incorrecta. Escoja de nuevo")





def introducriActividad():
    pass

while True:
    print("Escoja opción: ")
    print("1 - Insertar nuevo alumno/actividad")
    print("2 - ")
    print("3")
    print("4")
    print("5")
    print("6 - Salir")
    resp=int(input())

    if resp==1:
        while(True):
            print("Desea introducir un alumno (1) o una actividad (2)")
            r=int(input())
            if r==1:
                introducirAlumno()
            elif r==2:
                introducirActividad()
            else:
                print("Vuelva a intentarlo")
    elif resp==2:
        pass
    elif resp==3:
        pass
    elif resp==4:
        pass
    elif resp==5:
        pass
    elif resp==6:
        print("Hasta otra!")
        break
    else:
        print("Opción no válida. Vuelva a intentarlo")
