import pymysql
import datetime
from ListadoLlantas import Llanta

def conectar():
    mydb=pymysql.connect(
        host="localhost",
        user="root",
        passwd="12345",
        db="shopllantas"
    )
    return mydb


def buscarCompra(cod):
    mydb=conectar()
    cursor=mydb.cursor()
    sql="SELECT IdCompra FROM secompra WHERE IdCompra LIKE "+cod
    cursor.execute(sql)
    resultado=cursor.fetchone()
    cursor.close()
    if resultado==None:
        return False
    else:
        return True


def importar(archivo):
    f=open(archivo, "r")
    for linea in f:
        arrayfichero=linea.split("-")
        if buscarCompra(arrayfichero[0])==False:
            id=arrayfichero[0]
            proveedor=arrayfichero[1]
            llanta=arrayfichero[2]
            cantidad=arrayfichero[3]
            fecha=arrayfichero[4]
            importe=arrayfichero[5]
            mydb=conectar()
            cursor=mydb.cursor()
            sql="INSERT INTO secompra VALUES (%s, %s, %s, %s, %s, %s)"
            val=(id, proveedor, llanta, cantidad, fecha, importe)
            cursor.execute(sql, val)
            mydb.commit()
            cursor.close()
    f.close()


def generarFichero():
    f=open("VentasClientes.txt", "w")
    mydb=conectar()
    cursor=mydb.cursor()
    sql="SELECT * FROM cliente"

    cursor.execute(sql)
    resultado=cursor.fetchall()
    for i in resultado:
        f.write("CLIENTE: "+str(i[0])+" - "+str(i[1])+"\n")
        f.write("VENTAS: \n")
        cursordos=mydb.cursor()
        sqldos="SELECT sevende.IdVenta, sevende.IdLlanta, marca.Nombre, labrado.Nombre, (sevende.Cantidad*llanta.Precio*1.1), sevende.Cobrado FROM sevende, marca, labrado, llanta, cliente WHERE llanta.IdMarca=marca.IdMarca AND llanta.IdLabrado=labrado.IdLabrado AND sevende.IdCliente=cliente.IdCliente AND cliente.IdCliente="+str(i[0])+" GROUP BY sevende.IdVenta"
        cursordos.execute(sqldos)
        resultadodos=cursordos.fetchall()
        for j in resultadodos:
            if str(j[5])=="1":
                pagado="SI"
            else:
                pagado="NO"
            f.write(str(j[0])+"/"+str(j[1])+"/"+str(j[2])+"/"+str(j[3])+"/"+str(j[4])+"/"+pagado+"\n")
    f.close()

def generarListado():
    while True:
        try:
            y1=int(input("Introduzca año desde: "))
            m1=int(input("Introduzca mes desde: "))
            d1=int(input("Introduzca día desde: "))
            break
        except ValueError:
            print("Solo puede introducir números enteros. Inténtelo de nuevo.")

    while True:
        try:
            y2=int(input("Introduzca año hasta: "))
            m2=int(input("Introduzca mes hasta: "))
            d2=int(input("Introduzca día hasta: "))
            break
        except ValueError:
            print("Solo puede introducir números enteros. Inténtelo de nuevo.")

    fechauno=datetime.datetime(y1,m1,d1)
    fechados=datetime.datetime(y2,m2,d2)

    mydb=conectar()
    cursor=mydb.cursor()
    sql="SELECT sevende.Idventa, cliente.Nombre, sevende.FechaVenta, sevende.Cantidad*llanta.Precio FROM sevende, cliente, llanta WHERE sevende.IdLlanta=llanta.IdLlanta AND cliente.IdCliente=sevende.IdCliente"

    cursor.execute(sql)
    resultado=cursor.fetchall()
    print("RANGO DE FECHAS: " + str(d1) + "/" + str(m1) + "/" + str(y1) + " al " + str(d2) + "/" + str(m2) + "/" + str(
        y2))

    for i in resultado:
        array=str(i[2]).split("/")
        fecha=datetime.datetime(int(array[2]), int(array[1]), int(array[0]))
        if fecha>fechauno and fecha<fechados:
            print(str(i[0])+"/"+str(i[1])+"/"+str(i[2])+"/"+str(i[3]))


def listaObjetos():

    while True:
        try:
            diametro=float(input("De qué diametro desea realizar el listado de llantas?"))
            break
        except ValueError:
            print("Debe introducir un carácter numérico. Pruebe otra vez")


    listado=[]
    mydb=conectar()
    cursor=mydb.cursor()
    cursor.execute("SELECT llanta.IdLlanta, marca.Nombre, labrado.Nombre, llanta.Precio FROM llanta, marca, labrado WHERE llanta.IdMarca=marca.IdMarca AND llanta.IdLabrado=labrado.IdLabrado AND llanta.Diametro > "+str(diametro))
    resultado=cursor.fetchall()
    for i in resultado:
        llanta=Llanta(str(i[0]), str(i[1]), str(i[2]), str(i[3]))
        listado.append(llanta)

    visualizarListadoObjetos(listado)


def visualizarListadoObjetos(listado):
    for i in listado:
        print(str(i.idllanta)+"/"+str(i.nommarca)+"/"+str(i.precio))


while True:
    print("Escoja opción:")
    print("1 - Importar de compras.txt")
    print("3 - Generar fichero VentasClientes.txt")
    print("4 - Ver listado ventas por fecha")
    print("5 - Lista objetos")
    print("6 - Salir")
    try:
        r=int(input())
        if r == 1:
            importar("Compras.txt")
        elif r == 2:
            pass
        elif r == 3:
            generarFichero()
        elif r == 4:
            generarListado()
        elif r == 5:
            listaObjetos()
        elif r == 6:
            print("Hasta otra")
            break
        else:
            print("Debe elegir una opcion. Vuelva a intentarlo")
    except ValueError:
        print("Debe elegir un número entero. Vuelva a intentarlo")

