'''Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase
con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño
mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).'''

class Triangulo(object):

    def __init__(self, l1, l2, l3):
        lado1=l1
        lado2=l2
        lado3=l3

    def imprimirLadoMayor(self):
        print("hola")
    def tipodeTriangulo(self):
        print("hola")



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
    r=str(input("Escoja una opción: \na) Saber el lado mayor\nb) Saber el tipo de triangulo c)Salir"))
    if r =="a":
        t.imprimirLadoMayor()
    elif r=="b":
        t.tipodeTriangulo()
