'''Definir una función generar_n_caracteres() que tome un entero n y devuelva el
caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería
devolver "xxxxx".'''

n=0

def generar_n_caracteres(entero, caracter):
    for i in range (entero):
        print(caracter, end="")

def pedirNumero():
    n = input("Introduzca un número entero: ")
    return n

while True:
    try:
        n=int(pedirNumero())
        break
    except ValueError:
        print("Eso no es un número entero, vuelve a intentarlo")

c=str(input("Introudzca un carácter: "))

generar_n_caracteres(n, c)

'''
#También se podría hacer así: 

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
'''