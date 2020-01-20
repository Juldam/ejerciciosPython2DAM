'''Realizar una clas que administre una agenda. Se debe almacenar para cada
contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las
siguientes opciones:
a) Añadir contacto
b) Lista de contactos
c) Buscar contacto
d) Editar contacto
e) Cerrar agenda
'''

misContactos=[]

class Contacto(object):

    def __init__(self, nombre, telefono, email):
        self.nombre=nombre
        self.telefono=telefono
        self.email=email


def comprobarNombre(nom):
    enc=False
    for i in misContactos:
        if i.nombre==str(nom):
            enc=True
    return enc



while(True):
    print("Escoja una opción: ")
    print("a) Añadir contacto")
    print("b) Listar contactos")
    print("c) Buscar contacto")
    print("d) Editar contacto")
    print("e) Cerrar agenda")
    r=str(input("Introduzca letra: "))

    if r=="a":
        while(True):
            nom=str(input("Introduzca el nombre del contacto: "))
            if comprobarNombre(nom) == True:
                print("Ese nombre ya está en la lista, introduzca uno diferente")
            else:
                break
        tel=input("Introduzca el teléfono del contacto: ")
        email=str(input("Introduzca el email del contacto: "))
        p=Contacto(nom, tel, email)
        misContactos.append(p)
        print("Contacto añadido a la agenda")
    elif r=="b":
        for element in misContactos:
            print(element.nombre)
    elif r == "c":
        enc=False
        contacto=str(input("Introduzca el contacto que quiere buscar: "))
        for i in misContactos:
            if contacto == str(i.nombre):
                print(i.nombre+": "+"Telefono->"+i.telefono+", e-mail->"+i.email)
                enc=True
        if enc==False:
            print("No se ha encontrado ese contacto en la agenda")
    elif r == "d":
        enc = False
        contacto = str(input("Introduzca el contacto que quiere editar: "))
        for i in misContactos:
            if contacto == str(i.nombre):
                print("El contacto "+i.nombre + " que quiere editar tiene los siguientes datos: " + "Telefono->" + i.telefono + ", e-mail->" + i.email+"\n")
                n=str(input("Introduzca nuevo nombre para el contacto: "))
                i.nombre=n
                tel=input("Introduzca nuevo telefono para el contacto: ")
                i.telefono=tel
                e=str(input("Introduzca nuevo e-mail para el contacto: "))
                i.email=e
                print("Contacto editado")
                enc = True
        if enc == False:
            print("No se ha encontrado ese contacto en la agenda")
    elif r == "e":
        print("Hasta otra!")
        break
    else:
        print("Debe introducir una letra entre la a y la e")





