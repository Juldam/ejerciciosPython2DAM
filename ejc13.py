'''13- Escribir una función filtrar_palabras() que tome una lista de palabras y un
entero n, y devuelva las palabras que tengan más de n caracteres.'''

listaPalabras=["coche", "camión", "motocicleta", "tractor", "submarino", "tren"]

def filtrar_palabras(n):
    cont=0
    print("Las palabras con o más de "+str(n)+" son:")
    for i in listaPalabras:
        for j in i:
            cont=cont+1
        if cont >= int(n):
            print(i+", ", end="")
        cont=0

n=input("¿De cuántos carácteres quiere obtener las palabras de la lista?")

filtrar_palabras(n)