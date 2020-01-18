'''Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase
con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño
mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).'''

class Triangulo(object):

    def __init__(self, l1, l2, l3):
        lado1=l1
        lado2=l2
        lado3=l3

    def imprimirLadoMayor(self):
        if int(l1) > int(l2):
            if int(l1) > int(l3):
                print("El lado mayor es el "+str(l1))
            else:
                print("El lado mayor es el "+str(l3))
        elif int(l2) > int(l3):
            print("El lado mayor es el "+str(l2))
        else:
            print("El lado mayor es el "+str(l3))


    def tipodeTriangulo(self):
        if l1==l2 and l2==l3:
            print("El triángulo es equilátero")
        elif l1==l2 or l2==l3 or l1==l3:
            print("El triángulo es isósceles")
        elif l1!=l2 and l3!=l2 and l1!=l3:
            print("El triángulo es escaleno")



while(True):
    try:
        l1=int(input("Introduzca el primer lado del Triángulo: "))
        l2=int(input("Segundo lado: "))
        l3=int(input("Tercer lado: "))
        t=Triangulo(l1, l2, l3)
        break
    except ValueError:
        print("Esos valores no son válidos, vuelva a intentarlo de nuevo")

while(True):
    r=str(input("Escoja una opción: \na) Saber el lado mayor\nb) Saber el tipo de triangulo \nc)Salir"))
    if r =="a":
        t.imprimirLadoMayor()
    elif r=="b":
        t.tipodeTriangulo()
    elif r=="c":
        print("Hasta otra")
        break
    else:
        print("Debe escoger una opción válida. Inténtelo de nuevo.")
