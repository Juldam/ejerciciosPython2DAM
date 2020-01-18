'''20- Escriba una función es_bisiesto() que determine si un año determinado es un
año bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es
divisible por 400'''


def es_bisiesto(anio):
    if int(anio) % 4 ==0 and int(anio) % 100 != 0 or int(anio) % 400 ==0:
        print("El "+str(anio)+" es bisiesto")
    else:
        print("El "+str(anio)+" no es bisiesto")

anio=input("Introduzca el año para saber si es bisiesto o no: ")

es_bisiesto(anio)