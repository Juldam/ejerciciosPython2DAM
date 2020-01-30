import os

'''
Implementar una aplicación que simule una agenda que permita almacenar el
nombre, apellido y teléfono de una persona. La agenda se almacenará en un
fichero de texto agenda.txt donde cada persona ocupará tres líneas, una por
cada dato(nombre, apellido, teléfono).
La aplicación permitirá mediante un menú las siguientes opciones:
a) Buscar el teléfono de una persona dado su nombre y apellido
b) Añadir una nueva persona a la agenda
c) Borrar una entrada de la agenda dado su nombre y apellido
d) Listado completo de la agenda por pantalla. Cada entrada debe ocupar una
sola línea en pantalla
e) Listado de teléfonos de todas las personas cuyo apellido empieza por una letra
determinada introducida por el usuario.
f) Salir
'''

listaBuscador=[]

def buscarNombre():
    n=str(input("Introduzca el nombre de la persona a buscar: "))
    try:
        f=open("agenda.txt", "r")
        cont=0
        '''for linea in f:
            listaBuscador.append(linea+", ")
            if cont%3==0:
                array=listaBuscador.split(",", 2)
                if array[0] == n:
                    for i in listaBuscador:
                        print(i)
                    break
                else:
                    cont=cont+1'''
        for linea in f:
            if linea == n+"\n":
                print(linea)
                print(next(f))#PARA IMPRIMIR LA SIGUIENTE LINEA EN EL BUCLE!!!
                print(next(f))
        f.close()
    except IOError:
        print("No se encuentra la agenda.txt. Asegurese de haber introducido al menos un contacto")
    except:
        print("Ha habido un error al leer el archivo agenda.txt")


def addPersona():
    n=str(input("Introduzca el nombre de la persona: "))
    a=str(input("Introduzca el apellido: "))
    t=str(input("Intrdduzca el teléfono: "))

    f=open("agenda.txt", "a")
    #f.write(n+"\n"+a+"\n"+t+"\n")
    f.write(n)
    f.write("\n")
    f.write(a)
    f.write("\n")
    f.write(t)
    f.write("\n")
    f.close()


def borrarContacto():
    n=str(input("Introduzca el nombre del contacto: "))
    f=open("agenda.txt", "r+")#Abre el archivo para leer y escribir, el puntero está al principio del archivo
    nuevoF=open("temp.txt", "w")
    cont=1
    for i in f:
        cont=cont+1
        if i != n+"\n" and cont>=2:
            nuevoF.write(i)
        else:
            cont=0
    f.close()
    nuevoF.close()
    if os.path.exists("agenda.txt"):
        os.remove("agenda.txt")
    else:
        print("El archivo no existe")
    os.rename("temp.txt", "agenda.txt")

def visualizarAgenda():
    try:
        f=open("agenda.txt", "r")
        cont=0
        for linea in f:
            if cont==0:
                array=linea.split("\n") #AUNQUE NO SE VEA EL \N SIGUE AHÍ, POR LO QUE HAY QUE QUITARLO
                print(array[0], end=" ")
                cont=1
            elif cont==1:
                array=linea.split("\n")
                print(array[0], end=", ")
                cont=2
            elif cont==2:
                print(linea)
                cont=0
        f.close()
    except:
        print("No se encuentra el archivo agenda.txt o todavía no se ha creado. Añada una entrada para crearlo.")


def buscarLetraApellido(letra):
    f=open("agenda.txt", "r")
    cont=0
    enc=False

    for i in f:
        if cont==1:
            array=list(i)#Con esto dividimos una cadena en caracteres
            if array[0].lower()==letra.lower():
                enc=True
        if(cont==2):
            if enc==True:
                print(i)
                enc=False
            cont=0
        else:
            cont=cont+1
    f.close()

while(True):
    print("Escoja una opción:")
    print("a) Buscar teléfono")
    print("b) Añadir una nueva persona a la agenda")
    print("c) Borrar entrada")
    print("d) Listado completo de la agenda")
    print("e) Listado telefonos de personas por apellido")
    print("f) Salir")
    resp=str(input("\n"))
    if resp=="f":
        print("Hasta otra!")
        break
    elif resp=="a":
        buscarNombre()
    elif resp=="b":
        addPersona()
    elif resp=="c":
        borrarContacto()
    elif resp=="d":
        visualizarAgenda()
    elif resp=="e":
        letra=str(input("Introduzca la primera letra del apellido: "))
        buscarLetraApellido(letra)
    else:
        print("Debe seleccinar una opción válida. Vuelva a intentarlo.")