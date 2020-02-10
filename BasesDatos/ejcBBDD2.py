import datetime
import mysql.connector

class Llanta():
    def __init__(self, id, nombremarca, nombrelabrado, precio):
        self.id=id
        self.nombremarca=nombremarca
        self.nombrelabrado=nombrelabrado
        self.precio=precio

    def mostrar(self):
        print(self.id, self.nombremarca, self.nombrelabrado, self.precio)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="shopllantas"
)

def conectar():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345",
        database="shopllantas"
    )
    return mydb


def comprobarProveedor(proveedor):
    db=conectar()
    mycursorproveedor=db.cursor()
    sql="SELECT IdProveedor FROM proveedor WHERE IdProveedor ="+proveedor
    mycursorproveedor.execute(sql)
    myresultproveedor=mycursorproveedor.fetchone()
    if myresultproveedor==None:
        print("El proveedor con id " + proveedor + " no se encuentra en la bbdd. Hay que meterlo")
        nombre=str(input("Empresa del proveedor con id "+str(proveedor)+": "))
        contacto=str(input("Nombre del contacto : "))
        email = str(input("Email del contacto: "))
        sql="INSERT INTO proveedor VALUES (%s, %s, %s, %s)"
        val=(proveedor, nombre, contacto, email)
        bd=conectar()
        cursor=bd.cursor()
        cursor.execute(sql, val)
        bd.commit()
        bd.close()
    db.close()


def comprobarLlanta(llanta):
    db=conectar()
    mycursorllanta=db.cursor()
    sql="SELECT IdLlanta FROM llanta WHERE IdLlanta ="+llanta
    mycursorllanta.execute(sql)
    myresultllanta=mycursorllanta.fetchone()
    if myresultllanta==None:
        print("La llanta con id "+llanta+" no se encuentra en la bbdd. Hay que meterla")
        marca=input("Marca de la llanta con id "+llanta+": ")
        idlabrado=input("IdLabrado : ")
        diametro = input("Diametro: ")
        stock = input("Stock: ")
        precio=input("Precio: ")
        sql="INSERT INTO llanta VALUES (%s, %s, %s, %s, %s, %s)"
        val=(llanta, marca, idlabrado, diametro, stock, precio)
        bd=conectar()
        cursor=bd.cursor()
        cursor.execute(sql, val)
        bd.commit()
        bd.close()
    db.close()

def importar():
    archivo="Compras.txt"
    f=open(archivo, "r")
    for linea in f:
        arraylinea=linea.split("-")
        mycursor=mydb.cursor()
        sql="SELECT IdCompra FROM secompra WHERE IdCompra = %s"
        val=(str(arraylinea[0]),)
        mycursor.execute(sql, val)
        myresult=mycursor.fetchone()#Aquí no funciona con fetchall, mirar a ver por qué
        if myresult==None:
            print("Introducciendo la compra con id "+str(arraylinea[0])+" en la bbdd")
            comprobarProveedor(arraylinea[1])
            comprobarLlanta(arraylinea[2])
            sql="INSERT INTO secompra VALUES (%s, %s, %s, %s, %s, %s)"
            val=(arraylinea[0], arraylinea[1], arraylinea[2], arraylinea[3], arraylinea[4], arraylinea[5])
            mycursorDos=mydb.cursor()
            mycursorDos.execute(sql, val)
            mydb.commit()
        else:
            print("La compra con id "+str(arraylinea[0])+" ya se encuentra en la bbdd")

    f.close()



def generarBinario():
    nombrefichero="MarcasLabrados.dat"
    f=open(nombrefichero, "wb")
    cursor=mydb.cursor()
    sql="SELECT marca.Nombre, COUNT(marca.IdMarca) FROM marca, llanta WHERE marca.IdMarca=llanta.IdMarca GROUP BY marca.IdMarca"
    cursor2=mydb.cursor()
    sql2="SELECT labrado.Nombre, COUNT(labrado.IdLabrado) FROM labrado, llanta WHERE labrado.IdLabrado=llanta.IdLabrado GROUP BY labrado.IdLabrado"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    cursor2.execute(sql2)
    resultado2=cursor2.fetchall()
    for i in resultado:
        f.write(("Marca "+i[0]+", uds: "+str(i[1])).encode('utf-8'))

    for j in resultado2:
        f.write(("Labrado "+j[0]+", uds: "+str(j[1])).encode('utf-8'))
    f.close()

    leerBinario(nombrefichero)

def leerBinario(nombre):
    with open(nombre, "rb") as fichero:
        for linea in fichero:
            print(linea)



def generarFicheroTexto(nombrefichero):
    cursor=mydb.cursor()
    sql="SELECT cliente.IdCliente, cliente.Nombre, sevende.IdVenta, sevende.IdLlanta, marca.Nombre, labrado.Nombre, llanta.Precio*sevende.Cantidad, sevende.Cobrado FROM cliente, sevende, marca, labrado, llanta WHERE cliente.IdCliente=sevende.IdCliente AND sevende.IdLlanta=llanta.IdLlanta AND labrado.IdLabrado=llanta.IdLabrado AND marca.IdMarca=llanta.IdMarca ORDER BY sevende.IdVenta"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    f=open(nombrefichero, "w")
    for i in resultado:
        pagado=""
        idcliente=""
        if i[6]=="1":
            pagado="Pagado(SI)"
        else:
            pagado="Pagado(NO)"
        if i[0]!=idcliente:
            f.write("CLIENTE: "+str(i[0])+" - "+str(i[1])+"\n")
            f.write("VENTAS: \n")
        f.write("- "+str(i[2])+"m/"+str(i[3])+"/"+str(i[4])+"/"+str(i[5])+"/"+pagado)
        idcliente = i[0]
    f.close()


def ventasPendientes():
    print("Se pedira un rango de fechas para ver las ventas pendientes de cobro")
    d=int(input("Introduzca dia desde: "))
    m=int(input("Introduzca mes desde: "))
    a=int(input("Introduzca año desde: "))
    d1 = int(input("Introduzca dia hasta: "))
    m1 = int(input("Introduzca mes hasta: "))
    a1 = int(input("Introduzca año hasta: "))
    fechadesde=datetime.datetime(a,m,d)
    fechahasta=datetime.datetime(a1,m1,d1)
    cursor=mydb.cursor()
    sql="SELECT sevende.IdVenta, cliente.Nombre, sevende.FechaVenta, sevende.Cantidad*llanta.Precio FROM sevende, cliente, llanta WHERE sevende.IdCliente=cliente.IdCliente AND sevende.IdLlanta=llanta.IdLlanta AND sevende.Cobrado=0"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    print("Rango de fechas: "+fechadesde.strftime("%x")+" al "+fechahasta.strftime("%x"))
    print("Ventas:")
    for i in resultado:
        arrayfecha=i[2].split("/")
        fecha=datetime.datetime(int(arrayfecha[2]), int(arrayfecha[1]), int(arrayfecha[0]))
        if fecha>fechadesde and fecha<fechahasta:
            print(i)



def listaObjetos(diametro):
    listallantas=[]
    cursor=mydb.cursor()
    sql="SELECT llanta.IdLlanta, marca.Nombre, labrado.Nombre, llanta.Precio FROM llanta, marca, labrado WHERE llanta.IdMarca=marca.IdMarca AND llanta.IdLabrado=labrado.IdLabrado AND Diametro >= "+str(diametro)
    cursor.execute(sql)
    resultado=cursor.fetchall()
    for i in resultado:
        l=Llanta(i[0], i[1], i[2], i[3])
        listallantas.append(l)

    visualizarListaObjetos(listallantas)

def visualizarListaObjetos(lista):
    for i in lista:
        i.mostrar()

while(True):
    print("Escoja una opción: ")
    print("1) Importar información desde fichero txt a la base de datos")
    print("2) Generar un fichero binario .dat que contenga el número de llantas por Marca y Labrado")
    print("3) Generar fichero VentasClientes.txt")
    print("4) Generar listado en pantalla de ventas pendientes de cobro")
    print("5) Generar lista de objetos con info de llantas disponibles")
    print("6) Salir")
    resp=input()

    if resp=="1":
        importar()
    elif resp=="2":
        generarBinario()
    elif resp=="3":
        generarFicheroTexto("VentasClientes.txt")
    elif resp=="4":
        ventasPendientes()
    elif resp=="5":
        diametro=input("Introduzca el diametro para el cual quiere obtener el listado de llantas: ")
        listaObjetos(diametro)
    elif resp=="6":
        print("Hasta otra!")
        break
    else:
        print("Debe seleccionar una opción del 1 al 6. Inténtelo de nuevo")