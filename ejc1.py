'''
Definir una función max() que tome como argumento dos números y devuelva el
mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero
hacerla nosotros mismos es un muy buen ejercicio).
'''

def max(num1, num2):
    if num1>num2:
        print ("El"+str(num1)+" es el mayor")
    elif num2>num1:
        print ("El "+str(num2)+" es el mayor")


n1=input("Introduzca el primer número: ")
n2=input("Introduzca el segundo número: ")

max(n1, n2)