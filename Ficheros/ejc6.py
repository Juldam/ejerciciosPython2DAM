'''
Diseña un programa que cuente el número de caracteres de un fichero de texto,
incluyendo los saltos de línea. (El nombre del fichero se pide al usuario por teclado).
'''


def contarCaracteres(fichero):
    try:
        f=open(fichero, "r")
        contCaract = 0
        for linea in f:
            contCaract = contCaract + (len(linea))
        print("Ese fichero tiene " + str(contCaract) + " carácteres incluyendo los saltos de línea.")
    except IOError:
        print("Ese archivo no existe. Inténtelo de nuevo.")
    except:
        print("Ha habido un error a la hora de leer el archivo...")



while(True):
    nomFichero=str(input("Introduzca la ruta/nombre de un fichero de texto para saber los carácteres que tiene: "))
    contarCaracteres(nomFichero)
    resp=str(input("¿Desea introducir otra palabra?(S/N)"))
    if resp.upper() != "S":
        break
