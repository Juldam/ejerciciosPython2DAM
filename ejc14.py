'''14- Escribir un programa que le diga al usuario que ingrese una cadena. El
programa tiene que evaluar la cadena y decir cuántas letras mayúsculas tiene.'''

cont=0

palabra=str(input("Introduzca una cadena para saber cuántas mayúsculas tiene la palabra: "))

for i in palabra:
    if i == i.upper() and i != " " :
        cont=cont+1

print("Esa cadena tiene "+str(cont)+" letras mayúsculas")