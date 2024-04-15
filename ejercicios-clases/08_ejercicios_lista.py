"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""


def almacenar_asignatura():
    asignaturas = []
    notas = []

    for _ in range(5):
        asignatura = input("Ingrese la asignatura: ")
        nota = float(input(f"Ingrese la nota de {asignatura}: "))

        asignaturas.append(asignatura)
        notas.append(nota)

    filtrar_asignaturas_reprobadas(asignaturas, notas)

def filtrar_asignaturas_reprobadas(asignaturas, notas):
    repetir = []

    for i in range(len(asignaturas)):
        if notas[i] < 4:
            repetir.append(asignaturas[i])

    print("Asignaturas que tienes que repetir:")
    for asignatura in repetir:
        print(asignatura)

almacenar_asignatura()



