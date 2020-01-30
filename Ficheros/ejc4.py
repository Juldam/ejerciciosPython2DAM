'''Haz una función a la que dadas la ruta de un fichero de texto y una palabra, devuelva
una lista con las líneas que contienen esa palabra.
A continuación, diseña un programa que lea el nombre de un fichero y tantas
palabras como el usuario desee (utiliza un bucle que pregunte al usuario si desea
seguir introduciendo palabras). Para cada palabra el programa mostrará las líneas
que contienen dicha palabra en el fichero.'''

palabras=[]
diccionarioPalabras={}
contLinea=0

def lineasPalabra(rutaArchivo, palabras):
    while(True):
        try:
            f=open(rutaArchivo, "r")
            break
        except IOError:
            rutaArchivo=str(input("Ha habido un error al abrir el archivo. Introduzca de nuevo la ruta del archivo: "))
    contLinea=0
    for linea in f:
        contLinea=contLinea+1
        for p in palabras:
            if p in linea:
                #ESTO ES MUY IMPORTANTE, LA UNICA MANERA QUE HE ENCONTRADO DE SABER SI UNA KEY EXISTE EN UN DICCIONARIO ES MEDIANTE UN TRY EXCEPT
                try:
                    diccionarioPalabras[p]=diccionarioPalabras[p]+(str(contLinea)+", ")
                except KeyError:
                    diccionarioPalabras[p]=""+str(contLinea)+", "

    for i in diccionarioPalabras:
        print("La palabra '"+i+"' se encuentra en las líneas: "+diccionarioPalabras[i])
    f.close()

rutafichero=str(input("Introduzca la ruta completa del fichero de texto: "))
while(True):
    palabra=str(input("Introduzca una palabra para saber en qué lineas está: "))
    palabras.append(palabra)
    resp=str(input("¿Desea introducir otra palabra?(S/N)"))
    if resp.lower() != "s":
        break


lineasPalabra(rutafichero, palabras)