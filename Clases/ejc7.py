'''
Desarrollar un programa que conste de una clase padre Cuenta y dos subclases
PlazoFijo y CajaAhorro. Definir los atributos titular y cantidad y un método para
imprimir los datos en la clase Cuenta. La clase CajaAhorro tendrá un método para
heredar los datos y uno para mostrar la información.
La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método
para obtener el importe del interés (cantidad*interés/100) y otro método para
mostrar la información, datos del titular plazo, interés y total interés.
Crear al menos un objeto de cada subclase.
'''

class Cuenta(object):

    def __init__(self):
        self.titular=str(input("Introduzca el nombre del titular: "))
        self.cantidad=float(input("Introduzca la cantidad en euros: "))

    def imprimirDatos(self):
        print("Titular: "+str(self.titular)+", cantidad en la cuenta: "+str(self.cantidad)+" euros.")



class CajaAhorro(Cuenta):
    def __init__(self):
        super().__init__()

    def imprimirDatos(self):
        super().imprimirDatos()



class PlazoFijo(Cuenta):
    def __init__(self):
        super().__init__()
        self.plazo=int(input("Introduzca el número de meses del plazo: "))
        self.interes=int(input("Introduzca el interés (%): "))


    def importeInteres(self):
        return (self.cantidad*(self.interes/100))

    def imprimirDatos(self):
        super().imprimirDatos()
        print("El importe recibido por este cliente en "+str(self.plazo)+" meses al "+str(self.interes)+"% es de: "+str(self.importeInteres())+" euros")


print("Vamos a introducir un cliente en Plazo fijo: ")
c1=PlazoFijo()
print("Vamos a introducir un cliente en Caja de Ahorro: ")
c2=CajaAhorro()


c1.imprimirDatos()
c2.imprimirDatos()
