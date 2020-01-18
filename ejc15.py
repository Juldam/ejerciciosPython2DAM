'''15- Construir un pequeño programa que convierta números binarios en enteros.'''

def calculardoraDecimal(n):
    cont=1
    numDecimal=0
    for i in reversed(n):
        if(i=="1"):
            numDecimal+=cont
        cont=cont*2

    print("Ese número en decimal es: "+str(numDecimal))




while True:
    n=str(input("Introduzca un numero en binario: "))
    enc=True
    for i in n:
        if i != "1" and i != "0":
            enc=False
    if enc==True:
        break
    else:
        print("Eso no es un número binario. Vuelva a intentarlo")

calculardoraDecimal(n)