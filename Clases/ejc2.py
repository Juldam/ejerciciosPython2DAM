'''Realizar un programa que tenga una clase Persona con las siguientes características:
La clase tendrá como atributos el nombre y la edad de una persona. Implementar los
métodos necesarios para iniciar los atributos, mostrar los datos e indicar si la
persona es mayor de edad o no'''

class Persona(object):
    nombre=""
    edad=0

    def mayorEdad(self, persona):
        if int(persona.edad) >18:
            print("La persona es mayor de edad")
        else:
            print("La persona no es mayor de edad")

    def iniciarAtributos(self):
        self.nom=str(input("Introduzca el nombre de la persona: "))
        self.edad=input("Introduzca la edad: ")


p=Persona()

p.iniciarAtributos()

p.mayorEdad(p)