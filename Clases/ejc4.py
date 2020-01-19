'''Definir la Clase País con los siguientes atributos: nombre, población y área.
Dos métodos: más grande que y densidad de población.
- más grande que: Devuelve True si este país es mas grande que otro (que pasamos
como parámetro).
- densidad de población: Devuelve la densidad de población (población dividida por
superficie).
Realizar un programa en Python que compare las superficies de España y Francia y
calcule e imprima las densidades de población de ambos.

Datos: España: 46.770.000 habitantes y 504.645 km2
Francia: 66.030.000 habitantes y 640.679 km2
Si lo deseas, inventa y añade datos adicionales de otros países...'''

class Pais(object):
    def __init__(self, nombre, poblacion, area):
        self.nombre=nombre
        self.poblacion=poblacion
        self.area=area

    def masGrandeQue(self, p):
        if self.area > p.area:
            print(self.nombre+" es el más grande")
        else:
            print(p.nombre+" es el más grande")

    def densidadPoblacion(self, p):
        densidadThis=self.poblacion//self.area
        densidad=p.poblacion//p.area
        if densidadThis > densidad:
            print(self.nombre+" es el que más densidad tiene ("+str(densidadThis)+" habts por km2).")
        else:
            print(p.nombre+" es el que más densidad tiene ("+str(densidad)+" habts por km2).")


espania=Pais("España", 46770000, 504645)
francia=Pais("Francia", 66030000, 640679)

espania.masGrandeQue(francia)
espania.densidadPoblacion(francia)