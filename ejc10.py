'''
Definir un histograma procedimiento() que tome una lista de números
enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9,
7]) debería imprimir lo siguiente:
****
*********
*******
'''

listaNum=[]

def procedimiento(listaNum):
    for i in listaNum:
        for j in range(i):
            print("*", end="")
        print("")


def pedirNumero():
    enc=False
    n=0
    while(not enc):
        try:
            n=int(input("Introduce un número entero: "))
            enc=True
        except ValueError:
            print("Eso no es un número entero, inténtalo de nuevo")
        return n

while True:
    num=pedirNumero()
    listaNum.append(num)
    r=str(input("¿Desea introducir otro número?S/N"))
    if r.lower()=="n":
        break

procedimiento(listaNum)
