"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla
"""


def ingresar_asignatura(mensaje_inicial, mensaje_secundario, mensaje_despedida):
    contador= 0
    asignaturas= []
    for i in range(1, 6):
        contador = i
        print(contador)
        if contador == 5:
            materia = input(mensaje_secundario)
            asignaturas.append(materia.capitalize())
            lista_asignaturas(asignaturas)
            print(mensaje_despedida)
        else:
            materia = input(mensaje_inicial)
            asignaturas.append(materia.capitalize())
            

def lista_asignaturas(asignaturas):
   return print(f"Las asignaturas ingresas son: {asignaturas}")

def main():
    mensaje_inicial= "Ingresar asignaturas: "
    mensaje_secundario= "Ingrese la última asignaturas: "
    mensaje_despedida= "Gracias por ingresar las asignaturas correspondientes"
    mensaje= ingresar_asignatura(mensaje_inicial, mensaje_secundario, mensaje_despedida) 
    return mensaje

main()


