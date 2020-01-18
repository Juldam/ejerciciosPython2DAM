'''4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
contrario devuelve False.'''

vocales=['a', 'e', 'i', 'o', 'u']

def vocal(letra):
    enc=False
    for i in vocales:
        if letra==i:
           enc = True

    if enc==True:
        print("La letra es una vocal")
    else:
        print("La letra no es una vocal")

letra=input("Introduzca una letra: ")

vocal(letra)

