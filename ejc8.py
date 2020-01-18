'''Definir una función superposicion() que tome dos listas y devuelva True si
tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir
la función usando el bucle for anidado.'''

listauno=["adios", 3, [3, 4, "si"], 2, 'i']
listados=[4, 1, "no", 'o', "hola", (3, 4, "si")]

def superposicion():
    enc=False
    for i in listauno:
        for j in listados:
            if i==j:
                enc=True
                break

    if enc == True:
        print("Las listas tienen al menos un elemnto en común")
    else:
        print("Las listas NO tienen ningún elemento en común")

superposicion()