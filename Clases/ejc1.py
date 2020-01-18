'''Realizar un programa que conste de una clase llamada Alumno que tenga como
atributos el nombre y al nota del alumno. Definir los métodos para inicilaizar sus
atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha
aprobado o no.'''

class Alumno ():
    nombre=""
    nota=0
    def __init__(self):
        self.nombre
        self.nota

    def iniciarAtributos(self):
        self.nombre=str(input("Introduzca un nombre de usuario: "))
        while (True):
            self.nota=input("Introduzca la nota: ")
            if (int(self.nota) >= 0 and int(self.nota) <= 10):
                break
            else:
                print("Las notas deben estar entre 0 y 10")


    def imprimirAtributos(self):
        print("La nota de "+str(self.nombre)+" es de "+self.nota)
        if(int(self.nota)>5):
            print("El alumno ha aprobado")
        else:
            print("El alumno ha suspendido")

a=Alumno()
a.iniciarAtributos()
a.imprimirAtributos()