'''19- Crear una función contar_vocales(), que reciba una palabra y cuente cuantas
letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.'''

diccionarioVocales={"a":0, "e":0, "i":0, "o":0, "u":0}

def mostrar_vocales():
    for i in diccionarioVocales:
        print(str(diccionarioVocales[i])+" -> "+str(i))

def contar_vocales(palabra):
    for i in palabra:
        if i in diccionarioVocales:
            diccionarioVocales[i]=int(diccionarioVocales.get(i))+1
            #print(diccionarioVocales[i])
    mostrar_vocales()


palabra=str(input("Introduzca una palabra: "))

contar_vocales(palabra)
