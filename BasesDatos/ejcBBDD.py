'''
Se desea implementar una aplicación en PYTHON que  permita gestionar la base de datos Extraescolares(Esta  base
de  datosalmacena  todas  las  actividades  extraescolares  que oferta un Centro de Estudios a sus alumnos.
Cada alumno sólo podrá matricularse en una actividad extraescolar). Para ello dispone de dos tablas:
ALUMNO(CodAlumno, NomAlumno, Edad, Población, Email, CodActividad)ACTIVIDAD(CodActividad, NomActividad,
Categoría, Precio, NumDiasSemana)La  aplicación  realizará  la  conexión  con  la  base  dedatos  con  la
que  va  a  trabajar.Y  a continuación, mediante un menú permitirá las siguientes opciones:
    1.Insertar un nuevo elemento a la base de datos. El usuario seleccionara si lo que quiere añadir  es  un  alumno
    o  una  actividad. Debes  tener  en  cuenta  que  las claves  primarias serán incrementales (debes calcularlas),
    es decir, cada nuevo elemento incrementara el código del anterior en una unidad. Además, al insertar un alumno,
    debes comprobar que el  código  de  la  actividad  en  la  que  se  matricula  el  alumno  debe  existir  en  la
    tabla actividad. Dado  que  es  necesario  calcular  un  código  de  manera  incremental  en  las  dos  inserciones, será
    OBLIGATORIO realizarun ÚNICOmétodo  para  dicho  fin,  el  cual  se  invoque  en  ambos casos.

    2.Dado  que estamos  en  tiempo  de  crisis,  el  Centro  ha  decidido  bajar  el  precio  de  todas aquellas actividades
    cuya categoría sea idiomasun 15% ó deporteun 10%.

    3.Generar un fichero de textoa partir de la base de datos, conla información de todas las actividades.  La
    información  que  debe  aparecer  en  dicho  fichero  es  larelativa  a  la actividad junto con el nombre,
    edad y población, de todos los alumnos matriculados en dicha actividad.
    El formato del fichero será como el que se muestra a continuación:CODIGO ACTIVIDAD: 1NOMBRE ACTIVIDAD:
    NataciónCATEGORIA: DeportePRECIO: 50NUMERO DIAS: 2ALUMNOS:Pedro Sánchez –4 –SalamancaMaría Fernández
    –5 –Carbajosa de la SagradaRoberto García –5 -CabrerizosSonia Troconiz –4 -SalamancaCODIGO ACTIVIDAD: 2....

    4.Generar  un listado  en  pantalla,  con  la  información  de  todas  las  actividades  cuya categoría sea una
    introducida por el usuario en el programa principal. La información a mostrar será el nombre de la actividad y
    para cada una de ellas, el nombre detodos los alumnos y el número total de alumnos matriculados en la misma.
    Por ejemplo: NOMBRE ACTIVIDAD: TenisALUMNOS:Paula JiménezCarla GómezDavid DomínguezTOTAL DE ALUMNOS: 3....

    5.Generar una lista de objetos de datos que almacene las distintas categorías y el número total de actividades
    existentes de cada categoría. Mostrar dicha estructura mostrando algo similar a lo siguiente: CATEGORIA: Deporte,
    TOTAL DE ACTIVIDADES: 3.

    6.Salir
'''

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="extraescolares"
)


class ActividadesCat(object):
    def __init__(self, nomcateg, numact):
        self.nomcateg=nomcateg
        self.numact=numact

    def mostrar(self):
        print("CATEGORIA: "+self.nomcateg+", TOTAL ACTIVIDADES: "+str(self.numact)) #FIJARSE EN LA COMA (EN VEZ DE UN +)

def comprobarTablaVacia(tabla):
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM "+tabla)
    mycursor.fetchall() #ESTO ES NECESARIO PORQUE SI NO NO AVANZA EL CURSOR A TRAVÉS DE TODAS LAS TUPLAS QUE NOS SALEN
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return True
    else:
        return False

def introducirAlumno():
    arrayOpciones=[]
    if comprobarTablaVacia("actividad"):
        print("No se puede introducir alumnos antes de insertar al menos una actividad")
    else:
        id=ultimoRegistro("codalumno", "alumno")
        nomalumno=str(input("Introduzca el nombre del alumno: "))
        while(True):
            try:
                edad=int(input("Introduzca la edad del alumno"))
                if(edad<=0 or edad>100):
                    print("Introduzca una edad válida. Inténtelo de nuevo")
                else:
                    break
            except ValueError:
                print("Debe introducir un número entero. Inténtelo de nuevo")
        poblacion=str(input("Introduzca la población del alumno: "))
        email=str(input("Introduzca el e-mail del alumno: "))
        print("Seleccione una actividad: ")
        mycursor=mydb.cursor()
        mycursor.execute("SELECT codactividad, nomactividad FROM actividad")
        myresult=mycursor.fetchall()
        for i in myresult:
            arrayOpciones.append(i[0])
            print(i)
        while(True):
            try:
                resp=int(input())
                if resp in arrayOpciones:
                    sql="INSERT INTO alumno VALUES (%s, %s, %s, %s, %s, %s)"
                    val=(id, nomalumno, edad, poblacion, email, resp)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    break
                else:
                    print("Debe seleccionar un valor de la lista para continuar. Inténtelo de nuevo")
            except ValueError:
                print("Debe introducir un número entero que corresponda con el código de la actividad. Inténtelo de nuevo.")

def introducirActividad():
    id=ultimoRegistro("codactividad", "actividad")
    nomactividad=str(input("Introduzca el nombre de la actividad: "))
    categoria=str(input("Introduzca el nombre de la categoria: "))
    while(True):
        try:
            precio=float(input("Introduzca el precio: "))
            break
        except ValueError:
            print("Eso no es un número")
    while(True):
        try:
            numdiassemana=int(input("Introduzca el número de días de la semana: "))
            break
        except ValueError:
            print("Eso no es un número")
    mycursor=mydb.cursor()
    sql="INSERT INTO actividad VALUES (%s, %s, %s, %s, %s)"
    val=(id, nomactividad, categoria, precio, numdiassemana)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, " fila insertada")


def ultimoRegistro(idCol, tabla):
    resultado=0
    mycursor=mydb.cursor()
    mycursor.execute("SELECT "+idCol+" FROM "+tabla+" ORDER BY "+idCol+" DESC LIMIT 1")
    result=mycursor.fetchone()
    if result==None:
        resultado=1
    else:
        for i in result:
            resultado=i+1
    return resultado

def bajarPrecios():
    mycursor=mydb.cursor()
    mycursor.execute("UPDATE actividad SET precio=(precio*0.9) WHERE categoria LIKE 'Deporte'")
    mycursor.execute("UPDATE actividad SET precio=(precio*0.85) WHERE categoria LIKE 'Idiomas'")
    print("Los precios han sido actualizados")

def generarFichero():
    nomfichero=str(input("Introduzca el nombre del fichero donde desea guardar el listado de actividades (con .txt): "))
    f=open(nomfichero, "w")

    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM actividad")
    myresult=mycursor.fetchall()
    for i in myresult:
        f.write("CODIGO ACTIVIDAD: "+str(i[0])+"\n")
        f.write("NOMBRE ACTIVIDAD: "+str(i[1])+"\n")
        f.write("CATEGORIA: "+str(i[2])+"\n")
        f.write("PRECIO: "+str(i[3])+"\n")
        f.write("NUMERO DIAS: "+str(i[4])+"\n")
        f.write("ALUMNOS: "+"\n")
        mycursordos=mydb.cursor()
        mycursordos.execute("SELECT * FROM alumno WHERE codactividad ="+str(i[0]))
        myresultdos=mycursordos.fetchall()
        for j in myresultdos:
            f.write("\t"+str(j)+"\n")


def listarActividades(categ):
    mycursor=mydb.cursor()
    sql="SELECT * FROM actividad WHERE actividad.categoria LIKE '"+categ+"'"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()

    if myresult==None:
        print("No hay actividades para esa categoria")
    else:
        for i in myresult:
                print("Nombre actividad: "+str(i[1]))
                mycursor.execute("SELECT alumno.nomalumno FROM alumno, actividad WHERE alumno.codactividad=actividad.codactividad AND actividad.nomactividad = '"+str(i[1])+"'")
                myresultDos=mycursor.fetchall()
                print("Alumnos: ")
                cont=0
                for f in myresultDos:
                    print(f)
                    cont+=1
                print("Total alumnos: "+str(cont))

    mycursor.close()

def generarListaObjetos():
    listaobjetos=[]
    mycursor=mydb.cursor()
    mycursor.execute("SELECT categoria FROM actividad GROUP BY categoria")
    myresult=mycursor.fetchall()
    for row in myresult:
        cat=row[0]
        mycursor.execute("SELECT COUNT(nomactividad) FROM actividad WHERE categoria LIKE '"+cat+"'")
        myresultDos=mycursor.fetchall()
        num=myresultDos[0]
        listaobjetos.append(ActividadesCat(cat, num))
    mycursor.close()
    for i in listaobjetos:
        print(i.mostrar())



while(True):
    print("Escoja una opción: ")
    print("1 - Insertar alumno o actividad")
    print("2 - Bajar precios")
    print("3 - Generar fichero de texto de las actividades")
    print("4 - Listar actividades de una categoria")
    print("5 - Generar lista de objetos")
    print("6 - Salir")
    resp=str(input())
    if resp=="1":
        while(True):
            r=str(input("¿Desea introducir un alumno (a) o una actividad (b)?"))
            if r=="a":
                introducirAlumno()
                break
            elif r=="b":
                introducirActividad()
                break
            else:
                print("Debe introducir una opción válida. Inténtelo de nuevo")
    elif resp=="2":
        bajarPrecios()
    elif resp=="3":
        generarFichero()
    elif resp=="4":
        while(True):
            categ=str(input("¿De qué categoría desea visualizar las actividades por pantalla? "))
            if categ != "":
                listarActividades(categ)
                break
            else:
                print("Introduzca una actividad...")
    elif resp=="5":
        generarListaObjetos()
    elif resp=="6":
        print("Hasta otra")
        break
    else:
        print("Debe introducir una respuesta válida. Inténelo de nuevo.")