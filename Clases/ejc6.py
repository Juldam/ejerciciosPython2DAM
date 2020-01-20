'''
En un banco tiene clientes que pueden hacer depósitos y extracciones de dinero. El
banco requiere también al final del día calcular la cantidad de dinero que se ha
depositado.
Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá
los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos
__init__, operar y depósito total.
'''

listaClientes=[]

class cliente(object):
    def __init__(self, nombre, cantidad):
        self.nombre=nombre
        self.cantidad=cantidad

    def depositar(self, cantidad):
        self.cantidad+=int(cantidad)
        print("Operación realizada")

    def extraer(self, cantidad):
        self.cantidad-=int(cantidad)
        print("Operación realizada")

    def mostrarTotal(self):
        return print("El cliente "+self.nombre+" tiene un total de "+self.cantidad+" euros en su cuenta.")

class banco(object):
    def __init__(self, c1, c2, c3):
        self.c1=c1
        self.c2=c2
        self.c3=c3

    def operar(self):
        print("Nada por aquí")

    def depositoTotal(self):
        return float(c1.cantidad+c2.cantidad+c3.cantidad)


c1=cliente("juan", 324234)
c2=cliente("elisa", 345243)
c3=cliente("raul", 34499)
listaClientes.append(c1)
listaClientes.append(c2)
listaClientes.append(c3)

while(True):
    print("Elija un opción: ")
    print("a) Nuevo cliente")
    print("b) Buscar cliente")
    print("c) Listar clientes")
    print("d) Calcular dinero total del banco")
    print("e) Salir")
    resp=str(input("\n"))
    if resp=="a":
        nom=str(input("Escriba el nombre del nuevo cliente: "))
        cant=input("Escriba la cantidad del nuevo cliente: ")
        listaClientes.append(cliente(nom, cant))
        print("Cliente introducido en la base de datos.\n")
    elif resp=="b":
        nom=str(input("Introduzca el nombre del cliente: "))
        enc=False
        for i in listaClientes:
            if i.nombre==nom:
                enc=True
                print(i.nombre+" cantidad en el banco: "+str(i.cantidad))
                while(True):
                    print("Elija opción: ")
                    print("1 - Ingresar dinero en cuenta")
                    print("2 - Retirar dinero en cuenta")
                    print("3 - Cancelar")
                    r=input()
                    if r == "1":
                        cant=input("¿Cuánta cantidad desea ingresar?")
                        i.depositar(cant)
                        break
                    elif r=="2":
                        cant=input("¿Cuánta cantidad desea retirar?")
                        i.extraer(cant)
                        break
                    elif r=="3":
                        print("Voviendo al menú principal")
                        break
                    else:
                        print("Escoja una opción válida...")

        if enc==False:
            print("No se encuentra ese cliente en el banco")

    elif resp=="c":
        for i in listaClientes:
            print(i.nombre)
    elif resp=="d":

        b=banco(c1, c2, c3)
        print("La cantidad total en el banco es: "+str("{0:.2f}".format(b.depositoTotal()))+" euros.") #CON ESTO REDONDEAMOS A DOS DECIMALES

    elif resp=="e":
        print("Hasta otra!")
        break
    else:
        print("Opción no válida, inténtelo de nuevo.")


