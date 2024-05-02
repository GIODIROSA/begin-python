"""
Ejercicio 1 / Gestión de un registro de estudiantes
•Descripción: Realice un script que permita al usuario gestionar un registro de estudiantes, incluyendo la posibilidad de agregar nuevos estudiantes, 
eliminar estudiantes y mostrar el registro actualizado.
•Entrada: El usuario ingresará comandos para agregar nuevos estudiantes, eliminar estudiantes o mostrar el registro de estudiantes.
•Salida: Dependiendo de la opción ingresada por el usuario, debe mostrar un mensaje al agregar un estudiante, eliminar un estudiante, o mostrar el 
registro de estudiantes.
Pasos:
1. Inicializar registro de estudiantes: Inicialice una lista vacía para almacenar los estudiantes, donde cada estudiante será representado como un 
diccionario con el nombre, apellido y número de identificación. (check)
2. Agregar estudiante: El usuario ingresará el nombre, apellido y número de identificación de un nuevo estudiante para agregarlo al registro. (check)
3. Eliminar estudiante: El usuario ingresará el número de identificación de un estudiante para eliminarlo del registro. (check)
4. Mostrar registro de estudiantes: El usuario podrá visualizar el registro actualizado de estudiantes, mostrando el nombre, apellido y número de 
identificación de cada estudiante.
5. Repetir hasta terminar: El usuario podrá realizar múltiples operaciones de gestión de estudiantes antes de decidir terminar el script. (check)
Restricciones:
•Cada estudiante debe tener un número de identificación único en el registro. (check)
"""

estudiantes = []

# CRUD - NO UPDATE
# agregar
# eliminar
# mostrar

def menu_principal():
    print("\n")
    print("*"*50)
    print("1. Agregar un estudiante")
    print("2. Eliminar un estudiante")
    print("3. Mostrar estudiantes inscritos")
    print("4. Salir")
    opcion = int(input("Seleccione una opcion: "))
    print("*"*50)
    return opcion

def agregar_estudiante(nombre, apellido, rut):
    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            print("Ya existe un estudiante con este rut, ingrese otro")
            return
        
    nuevo_estudiante= {
        "nombre": nombre,
        "apellido": apellido,
        "rut": rut
    }
    
    estudiantes.append(nuevo_estudiante)
               

def eliminar_registro_estudiante(rut):
    rut_a_eliminar = rut
    for estudiante in estudiantes:
        if estudiante["rut"] == rut_a_eliminar:
            estudiantes.remove(estudiante)
            print("El estudiante se elimina el registro")


def mostrar_estudiantes_registrado():
    for estudiante in estudiantes:
        for clave, detalle in estudiante.items():
            print(f"{clave.capitalize()}: {detalle.capitalize()}\n")
            print("_"*50)
            

def gestor_registro_estudiante():
     while True:
        try:
            opcion = menu_principal()
            if opcion == 1:
                nombre = input("Por favor, ingrese el nombre del estudiante: ")
                apellido = input("Por favor, ingrese el apellido: ")
                rut = input("Por favor, ingrese el rut con digito verificador pero sin guión. ej: 39227266: ")
                agregar_estudiante(nombre, apellido, rut)
                print("Estudiantes", estudiantes)
                print("¡GRACIAS! por agregar un nuevo estudiante")
            elif opcion == 2:
                print("Para eliminar un registro debe ingresar el rut")
                rut= input("Por favor, ingrese el rut con digito verificador pero sin guión. ej: 39227266: ")
                eliminar_registro_estudiante(rut)
                print("Estudiantes:", estudiantes)
            elif opcion == 3:
                mostrar_estudiantes_registrado()
            elif opcion == 4:
                print("Gracias por ingresar al sistema de inscripción de estudiantes")
                break
            else:
                raise ValueError
        except ValueError:
            print("¡¡¡ERROR!!! al ingresar un estudiante")




def main():
    gestor_registro_estudiante()


main()