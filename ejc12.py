'''12- Escribir una función mas_larga() que tome una lista de palabras y devuelva
la más larga.'''

listaPalabras=["perro", "gato", "rinoceronte", "orungatan", "pez"]

def mas_larga(lista):
    numletras = 0
    palabralarga = ""
    cont = 0
    for i in lista:
        for j in i:
            cont = cont+1
        print(i+" tiene "+str(cont)+" letras")
        if cont > numletras:
            palabralarga = i
            numletras = cont
        cont=0
    return palabralarga

print("La palabra más larga es "+mas_larga(listaPalabras))
