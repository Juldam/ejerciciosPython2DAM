'''
Crear un fichero "Pacientes.txt", que contiene la información de unos pacientes en el
formato (nombre edad diabetico si/no). A partir de dicho fichero, generar un nuevo
fichero que contenga los pacientes que tienen más de 20 años y no son diabéticos.
'''

rutaFichero="Pacientes.txt"
rutaFicheroNoDiabeticos="PacientesNoDiabeticos.txt"
pacientes=[]

class Paciente(object):
    def __init__(self, nombre, edad, diabetico):
        self.nombre=nombre
        self.edad=edad
        self.diabetico=diabetico

p1=Paciente("Juan", 59, False)
pacientes.append(p1)
p2=Paciente("Eva", 17, False)
pacientes.append(p2)
p3=Paciente("Luis", 13, True)
pacientes.append(p3)
p4=Paciente("Rosa", 78, True)
pacientes.append(p4)
p5=Paciente("Esteban", 4, False)
pacientes.append(p5)



def crearFichero(edad, enc):
    if(edad==-1):
        f=open(rutaFichero, "a")
        f.write("Los pacientes son:")
        for i in pacientes:
            f.write("\n- " + i.nombre)
        f.close()
    else:
        f = open(rutaFicheroNoDiabeticos, "a")
        f.write("Los pacientes menores de 20 años y sin diabetes son:")
        for i in pacientes:
            if(i.edad<20 and i.diabetico==False):
                f.write("\n- " + i.nombre)
        f.close()





input("Se va a crear un fichero con los pacientes. Presione INTRO para continuar")
crearFichero(-1, False)
input("Ahora se va a crear un fichetro con los pacientes menores de 20 anos y sin diabetes")
crearFichero(20, False)



