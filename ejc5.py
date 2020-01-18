''' 5 - Escribir una funcion sum() y una función multip() que sumen y multipliquen
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4])
debería devolver 10 y multip([1,2,3,4]) debería devolver 24 '''

#milista=[4,2,8,5]
milista=[]

def sum(lista):
    resultado=0
    for i in lista:
        resultado+=i
    print("El resultado de la suma es: "+str(resultado))

def multip(lista):
    resultado=1
    for i in lista:
        resultado*=i
    print("El resultado de la multiplicación es: "+str(resultado))

while(True):
    n=input("Introduzca un número: ")
    milista.append(int(n))
    r=str(input("¿Desea introducir otro número? S/N"))
    if r.lower() == "n":
        break

sum(milista)
multip(milista)