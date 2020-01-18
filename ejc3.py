'''3- Definir una función que calcule la longitud de una lista o una cadena dada. (Es
cierto que python tiene la función len() incorporada, pero escribirla por nosotros
mismos resulta un muy buen ejercicio). (Borra esto)'''

def calcularLongitud(cadena):
    cont=0
    for i in cadena:
        cont=cont+1
    return cont



cad=str(input("Introduzca una cadena para saber cuántos carácteres tiene: "))

print("La cadena tiene una longitud de "+str(calcularLongitud(cad))+" carácteres")

print(len(cad))