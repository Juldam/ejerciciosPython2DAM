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


while(True):
    print("Escoja una opción: ")
    print("a) Añadir contacto")
    print("b) Listar contactos")
    print("c) Buscar contacto")
    print("d) Editar contacto")
    print("e) Cerrar agenda")
    r=str(input("Introduzca letra: "))

    if r=="a":
        print("opc a")
    elif r=="b":
        print("opc b")
    elif r == "c":
        print("opc c")
    elif r == "d":
        print("opc d")
    elif r == "e":
        print("Hasta otra!")
        break
    else:
        print("Debe introducir una letra entre la a y la e")



