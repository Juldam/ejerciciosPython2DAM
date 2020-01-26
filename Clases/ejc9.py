'''Dada la Clase Vehículo, extiende dicha Clase y realiza la siguiente implementación:
- Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehículos.
- Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra
mostrando el nombre de su clase y sus atributos.
- Modifica la función catalogar() para que reciba un argumento optativo ruedas,
haciendo que muesetre únicamente los que su número de ruedas concuerde con el valor del
argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:"
únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2, y 4 ruedas como valor.'''

listaVehiculos=[]

class Vehiculo(object):
    def __init__(self, color, ruedas):
        self.color=color
        self.ruedas=ruedas
        listaVehiculos.append(self)#Esto va metiendo todas las instancias de objetos en la lista, ya que todas pasan por aquí (clase padre de todas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga=carga

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo=tipo

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

def catalogar(listaVehic, ruedas=-1):
    if ruedas==-1:
        #for i in listaVehic
        for i in quitarDuplicados(listaVehic):
            #print("Clase: "+i.__class__.__name__)#PARA MOSTRAR EL NOMBRE DE LA CLASE
            print("Clase: "+i)
    else:
        print("Con ese número de ruedas tenemos las siguientes clases:")
        #for i in listaVehic:
        for i in quitarDuplicadosRuedas(listaVehic, ruedas):
                #print("Clase: "+i.__class__.__name__)
                print("Clase: "+i)


def quitarDuplicados(lista):
    listaSinRepetidos=[]
    for i in lista:
        if i.__class__.__name__ not in listaSinRepetidos:
            listaSinRepetidos.append(i.__class__.__name__)
    return listaSinRepetidos

def quitarDuplicadosRuedas(lista, numruedas):
    listaSinRepetidos = []
    cont=0
    for i in lista:
        if i.ruedas == numruedas:
            cont=cont+1
            if i.__class__.__name__ not in listaSinRepetidos:
                listaSinRepetidos.append(i.__class__.__name__)
    print("Se han encontrado "+str(cont)+" vehículos con "+str(numruedas)+" ruedas.")
    return listaSinRepetidos

cocheUno=Coche("rojo", 4, 120, 100)
camionetaUno=Camioneta("azul", 4, 100, 80, 900)
bicicletaUno=Bicicleta("verde", 2, "urbana")
motoUno=Motocicleta("amarillo", 2, "deportiva", 200, 150)
motoDos=Motocicleta("amarillo", 2, "deportiva", 200, 150)

catalogar(listaVehiculos)
catalogar(listaVehiculos, 0)
catalogar(listaVehiculos, 2)
catalogar(listaVehiculos, 4)