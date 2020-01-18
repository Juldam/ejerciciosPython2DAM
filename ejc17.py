'''17- Definir una tupla con 10 edades de personas. Imprimir la cantidad de
personas con edades superiores a 20. Puedes variar el ejercicio para que sea el
usuario quien ingrese las edades.'''

import random

milista=[None]*10
mitupla=()
print("Se han generado 10 edades aleatorias y se han metido en una tupla")


for i in range(10):
    milista[i]=random.randint(0, 100)

mitupla=tuple(milista)

while True:
    try:
        n=int(input("A partir de qué edad quiere saber el número de personas que hay?"))
        break
    except ValueError:
        print("Introduzca un núemro valido")

cont=0
for i in mitupla:

    if i > int(n):
        cont=cont+1
print("Hay "+str(cont)+" personas mayores a esa edad en la tupla")

for i in mitupla:
    print(str(i)+", ", end="")
