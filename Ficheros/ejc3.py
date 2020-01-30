'''
Realizar un programa al que dado un fichero de texto que puedes crear con el bloc de
notas, muestre por pantalla la línea más larga. Si hay más de una línea con la longitud
máxima, el programa mostrará únicamente la primera de ellas.
'''

lineaMasLarga=""
max=0

def lineaMasLarga(rutafichero):
    f=open(rutafichero, "r")
    for linea in f:
        if len(linea)>max:
            lineaMasLarga=linea
    f.close()
    print("La linea más larga es: "+str(lineaMasLarga))

lineaMasLarga("ficheroprueba.txt")
