'''
En este ejercicio realizará un programa en Python que asigne e imprima en pantalla
las asignaturas, profesores y estudiantes de una pequeña "universidad".
Defina:
- Clase superior Miembro.
    +Con atributos nombre, edad y dni.
- Dos clases que heredan de ella: Profesor y Estudiante.
    +Profesor tiene, adicionalmente:
        *Atributo número de registro
        *Atributo asignaturas imparte: Lista, inicialmente vacía, con la
        relación de asignaturas que imparte el profesor.
        *Método añade dociencia. Añade un elemento a la lista de
        asignaturas que imparte el profesor.
        *Método imprime docencia. Imprime la lista de asignaturas que
        imparte un profesor, junto con la relación de estudiantes
        matriculados que hay en cada una de ellas.
    +Estudiante tiene, adicionalmente:
        *Atributo número de estudiante
- Clase Asignatura:
    +Atributos nombre y código
    +Atributo estudiantes: Lista, inicialmente vacía, con la relación de
    estudiantes matriculados en ella.
    +Método añade estudiante: Añade un estudiante matrículado a la lista
    de la asignatura.
    +Método imprime listado: Imprime la lista de estudiantes matriculados
    en una asignatura.
Realizar un programa que:
- Cree todos los objetos necesarios
- Asigne los valores adecuados a sus atributos
- Imprima en pantalla las asignaturas que imparte cada profesor junto con la relación
de estudiantes matriculados en ellas.
- Opcional: Realice una función adicional (ojo, no le pedimos un método) que reciba como
parámetro el nombre de un estudiante (por ejemplo "Jaimito", pero no el objeto jaimito)
e imprima las asignaturas en que éste está matriculado. Haga llamadas a esta función
para comprobar su funcionamiento. Ayuda: Para simplificar el código puede serle de
utilidad crear una lista con todas las asignaturas (lista objetos).
'''

listaAsignaturas=[]
listaEstudiantes=[]
listaProfesores=[]

class Miembro(object):
    def __init__(self, nombre, edad, dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

class Profesor(Miembro):
    def __init__(self, nombre, edad, dni, numregistro):
        super().__init__(nombre, edad, dni)
        self.numregistro=numregistro
        self.asignaturas=[]
        listaProfesores.append(self)

    def addDocencia(self, nomAsignatura):
        self.asignaturas.append(nomAsignatura)

    def imprimeDocencia(self):
        for i in self.asignaturas:
            print("\nAsignatura "+str(i.nomAsig)+":")
            i.imprimirListado()

class Estudiante(Miembro):
    def __init__(self, nombre, edad, dni, numestudiante):
        super().__init__(nombre, edad, dni)
        self.numestudiante=numestudiante


class Asignatura(object):
    def __init__(self, nomAsig, codAsig):
        self.nomAsig=nomAsig
        self.codAsig=codAsig
        self.estudiantesAsig=[]
        listaAsignaturas.append(self)

    def addEstudiante(self, nombreEstudiante):
        self.estudiantesAsig.append(nombreEstudiante)#Aquí le estoy pasando al array un objeto estudiante

    def imprimirListado(self):
        print("Los estudiantes de la asignatura "+str(self.nomAsig)+" son:")
        for i in self.estudiantesAsig:
            print(str(i.nombre))

def asignaturasEstudiante(nom):
    print("Las asignaturas en las que está matriculado "+str(nom)+" son: ")
    for i in listaAsignaturas:
        for j in i.estudiantesAsig:
            if j.nombre.lower()==nom.lower():
                print("- "+i.nomAsig)

luis=Profesor("Luis", 50, "34567", 5001)
pepe=Profesor("Pepe", 37, "65432", 5010)

jorgito=Estudiante("Jorgito", 20, "56678", 1001)
juanito=Estudiante("Juanito", 19, "44444", 1002)
jaimito=Estudiante("Jaimito", 19, "22334", 1005)

matematicas=Asignatura("Matemáticas", 5)
fisica=Asignatura("Física", 7)
latin=Asignatura("Latín", 13)
historia=Asignatura("Historia", 19)
filosofia=Asignatura("Filosofía", 36)

luis.addDocencia(matematicas)
luis.addDocencia(fisica)
pepe.addDocencia(latin)
pepe.addDocencia(historia)
pepe.addDocencia(filosofia)

matematicas.addEstudiante(jorgito)
fisica.addEstudiante(juanito)
fisica.addEstudiante(jaimito)
latin.addEstudiante(jorgito)
latin.addEstudiante(jaimito)
historia.addEstudiante(juanito)
historia.addEstudiante(jaimito)
filosofia.addEstudiante(jaimito)

print("Bienvenido a la Universidad diminuta.")
while(True):
    print("Escoja una opción:")
    print("a) Ver asignaturas que imparte cada profesor")
    print("b) Ver asignaturas por estudiante")
    print("c) Salir")
    resp=str(input(""))
    if resp=="a":
        for i in listaProfesores:
            print(i.imprimeDocencia())
    elif resp=="b":
        nom=str(input("Introduzca el nombre del estudiante: "))
        asignaturasEstudiante(nom)
    elif resp=="c":
        break
    else:
        print("Debe escoger una respuesta válida. Inténtelo de nuevo.")
