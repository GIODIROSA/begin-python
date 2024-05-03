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
            print("+"*50)
            print(f"+++++YA EXISTE UN ESTUDIANTE CON ESTE RUT+++++ {rut}")
            print("+"*50)
            return
        
    nuevo_estudiante= {
        "nombre": nombre.capitalize(),
        "apellido": apellido.capitalize(),
        "rut": rut
    }
    
    estudiantes.append(nuevo_estudiante)
    print("¡GRACIAS! por agregar un nuevo estudiante")
               

def eliminar_registro_estudiante(rut):
    rut_a_eliminar = rut
    for estudiante in estudiantes:
        if estudiante["rut"] == rut_a_eliminar:
            estudiantes.remove(estudiante)
            print("+"*100)
            print("EL ESTUDIANTE HA SIDO ELIMINADO DEL SISTEMA")
            print("+"*100)
            
            mostrar_estudiante(estudiantes)



def mostrar_estudiante(estudiantes):
     for indice, estudiante in enumerate(estudiantes, start = 1):
                    print("+"*100)
                    print(f"{indice}.) {estudiante}")
            

def gestor_registro_estudiante():
     while True:
        try:
            opcion = menu_principal()
            if opcion == 1:
                nombre = input("Por favor, ingrese el nombre del estudiante: ")
                apellido = input("Por favor, ingrese el apellido: ")
                rut = int(input("Por favor, ingrese el rut con digito verificador pero sin guión. ej: 39227266: "))
                if rut < 0:
                    print("Por favor, ingrese un rut correcto")
                else:
                    agregar_estudiante(nombre, apellido, rut)
                    
                mostrar_estudiante(estudiantes)
            elif opcion == 2:
                print("Para eliminar un registro debe ingresar el rut")
                rut= int(input("Por favor, ingrese el rut con digito verificador pero sin guión. ej: 111111: "))
                if rut < 0:
                    print("Rut incorrecto")
                else:
                    eliminar_registro_estudiante(rut)
               
            elif opcion == 3:
                mostrar_estudiante(estudiantes)
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