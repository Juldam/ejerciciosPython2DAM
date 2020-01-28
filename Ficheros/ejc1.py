'''
Realizar un programa que genere un fichero de texto y a continuación muestre cada
una de sus líneas precedidas por el número de línea.
'''




def crearFichero(texto, rutafichero):
    f=open(rutafichero, "w")
    f.writelines(texto)
    f.close()

def mostrarFichero(rutafichero):
    with open(rutafichero, "r") as fichero:
        for linea in fichero:
            print("'"+linea+"'")


rutafichero="textoejerc1.txt"
texto=str(input("Introduzca el texto que desea guardar en el fichero de texto: "))
crearFichero(texto, rutafichero)
print("El fichero que ha creado contiene: ")
mostrarFichero(rutafichero)