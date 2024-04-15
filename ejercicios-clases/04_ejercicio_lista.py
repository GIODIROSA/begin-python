"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

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
   for asignatura in asignaturas:
       print(f"Yo estudio: {asignatura}")

def main():
    mensaje_inicial= "Ingresar asignaturas: "
    mensaje_secundario= "Ingrese la última asignaturas: "
    mensaje_despedida= "Gracias por ingresar las asignaturas correspondientes"
    mensaje= ingresar_asignatura(mensaje_inicial, mensaje_secundario, mensaje_despedida) 
    return mensaje

main()