'''
16- Escribir un pequeño programa donde:
    - Se ingresa el año en curso.
    - Se ingresa el nombre y el año de nacimiento de tres personas.
    - Se calcula cuántos años cumplirán durante el año en curso.
    - Se imprime en pantalla.
'''

from datetime import datetime

n=0
anio=0
diccionarioAlumnos={}


def pedirFechaNac(i, year):
    while True:
        nombre=str(input("¿Cómo se llama el alumno?"))
        now = datetime.now()
        try:
            n = int(input("¿En qué año ha nacido "+nombre+"?"))
            if n > now.year or n > year:
                print("No puede ser ese año")
            else:
                diccionarioAlumnos[nombre]=year-n
                break
        except ValueError:
            print("Introduzca un numero válido")

anio=int(input("¿Qué año es el actual?"))

for i in range(3):
    pedirFechaNac(i, anio)

for i in diccionarioAlumnos:
    print("El alumno "+str(i)+" va a cumplir "+str(diccionarioAlumnos[i])+" años")



