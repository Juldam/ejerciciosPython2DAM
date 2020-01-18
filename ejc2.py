'''Definir una función max_de_tres(), que tome tres números como argumentos y
devuelva el mayor de ellos.'''

def max_de_tres(n1, n2, n3):
    if n1>n2:
        if n1>n3:
            print (n1+" es el mayor de los tres")
        else:
            print (n3+" es el mayor de los tres")
    else:
        if n2>n3:
            print (n2+" es el mayor de los tres")
        else:
            print (n3+" es el mayor de los tres")

num1=input("Introduzca el primer número: ")
num2=input("Introduzca el segundo número: ")
num3=input("Introduzca el tercer número: ")

max_de_tres(num1, num2, num3)
