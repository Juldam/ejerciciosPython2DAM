'''Definir una función es_palindromo() que reconoce palíndromos (es decir,
palabras que tienen el mismo aspecto escritas invertidas), ejemplo:
es_palindromo ("radar") tendría que devolver True.'''


def es_palindromo(cadena):
    palabraInvertida = []
    palabraAlreves=""
    for i in cadena:
        palabraInvertida.insert(0, i)

    for i in palabraInvertida:
        palabraAlreves+=i

    if palabraAlreves == cadena:
        print("¡Esa cadena es un palíndromo!")
    else:
        print("Esa palabra NO es un palíndromo")

while True:
    palabra=str(input("Introduzca una palabra para saber si es un palíndromo: "))
    es_palindromo(palabra)
    respuesta=str(input("¿Desea introducir otra palabra(S/N)?"))
    if respuesta.lower() == "n":
        break



