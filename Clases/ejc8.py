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
'''

listaAsignaturas=[]
listaEstudiantes=[]
listaProfesores=[]

class Miembro(object):
    def __init__(self, nombre, edad, dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

class Profesor(miembro):
    def __init__(self, numregistro):
        super().__init()
        self.numregistro=numregistro
        self.asignaturas=[]

    def addDocencia(self, nomAsignatura):
        self.asignaturas.append(nomAsignatura)

    def imprimeDocencia(self):
        for i in self.asignaturas:
            print("Asignatura "+str(i)+":")
            i=Asignatura()
            for j in

class Estudiante(miembro):
    def __init__(self, numestudiante):
        super().__init__()
        self.numestudiante=numestudiante


class Asignatura(object):
    def __init__(self, nomAsig, codAsig):
        self.nomAsig=nomAsig
        self.codAsig=codAsig
        self.estudiantesAsig=[]

    def addEstudiante(self, nombreEstudiante):
        self.estudiantesAsig.append(nombreEstudiante)

    def imprimirListado(self):
        print("Los estudiantes de la asignatura "+str(self.nomAsig)+" son:\n")
        for i in self.estudiantesAsig:
            print(str(i))


luis=Profesor("Luis", 50, "34567", 5001)
pepe=Profesor("Pepe", 37, "65432", 5010)

jorgito=Estudiante("Jorgito", 20, "56678", 1001)
juanito=Estudiante("Juanito", 19, "44444", 1002)
jaimito=Estudiante("Jaimito", 19, "22334", 1005)

