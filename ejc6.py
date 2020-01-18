'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo
la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"'''



def inversa(cadena):
    listaInversa=[]
    palabraInversa=""
    for i in cadena:
        listaInversa.insert(0, i)

    for i in listaInversa:
        palabraInversa+=i

    print(palabraInversa)

cadena=str(input("Introduzca una cadena para hacerla inversa: "))
inversa(cadena)