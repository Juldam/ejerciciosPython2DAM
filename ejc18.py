'''18- Definir una lista con un conjunto de nombres, imprimir la cantidad que
comienzan con la letra a. También se puede hacer elegir al usuario la letra a
buscar. (Un poco más emocionante)'''

listanombres=["pedro", "maria", "susana", "raul", "luis", "juan", "pepe", "lucas", "ricardo", "roberto"]


def nombres(l):
    cont=0
    for i in listanombres:
        if i[0] == l:
            cont=cont+1
    print("Hay "+str(cont)+" nombres que empiezan por ese carácter")



letra=str(input("Introduzca la letra para saber cuantos nombres empiezan por esa letra: "))

nombres(letra)




