"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""


def ingresar_asignatura(mensaje_inicial, mensaje_secundario, mensaje_despedida):
    contador= 0
    asignaturas= []
    notas= []
    for i in range(1, 6):
        contador = i
        print(contador)
        if contador == 5:
            materia = input(mensaje_secundario)
            nota= float(input("Ingrese la última nota: "))
            print(mensaje_despedida)
            asignaturas.append(materia.capitalize())
            notas.append(nota)
            lista_asignaturas_notas(asignaturas, notas)
        else:
            materia = input(mensaje_inicial)
            nota= float(input("Ingrese la nota: "))
            asignaturas.append(materia.capitalize())
            notas.append(nota)

            

def lista_asignaturas_notas(asignaturas, notas):
    for i in range(len(asignaturas)):
       print(f"En la asignatura: {asignaturas[i]} has sacado: {notas[i]}")


def main():
    mensaje_inicial= "Ingresar asignaturas: "
    mensaje_secundario= "Ingrese la última asignaturas: "
    mensaje_despedida= "Gracias por ingresar las asignaturas correspondientes"
    mensaje= ingresar_asignatura(mensaje_inicial, mensaje_secundario, mensaje_despedida) 
    return mensaje

main()

