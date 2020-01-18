'''11- La función max() del ejercicio 1 (primera parte) y la función max_de_tres()
del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números.
Supongamos que tenemos más de 3 números o no sabemos cuántos números
son. Escribir una función max_in_list() que tome una lista de números y devuelva
el más grande.'''

listaNum=[]
n=0

def max_in_list(lista):
    max=0;
    for i in lista:
        if lista.index(i)==0:#me devuelve la posición en la lista
            max=i
        else:
            if i>max:
                max=i

    print("El mayor de todos los números de la lista es: "+str(max))

def pedirNumero():
    enc=True
    n=0
    while(enc):
        try:
            n=int(input("Introduzca un número: "))
            enc=False
        except ValueError:
            print("Eso no es un número entero. Inténtelo otra vez")

    return n

while True:
    n=pedirNumero()
    listaNum.append(n)
    r=str(input("¿Desea introducir otro número?(s/n)"))
    if r.lower() == "n":
        break

max_in_list(listaNum)