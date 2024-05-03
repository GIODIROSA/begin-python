"""
Ejercicio 2 / Gestión de un registro de empleados
•Descripción: Realice un script que permita al usuario gestionar un registro de empleados, incluyendo la posibilidad de agregar nuevos empleados, 
actualizar el salario de los empleados y mostrar el registro actualizado.
•Entrada: El usuario ingresará comandos para agregar nuevos empleados, actualizar el salario de los empleados o mostrar el registro de 
empleados.
•Salida: Dependiendo de la opción ingresada por el usuario, debe mostrar un mensaje al agregar un empleado, actualizar el salario de un empleado, 
o mostrar el registro de empleados.
Pasos:
1. Inicializar registro de empleados: Inicialice una lista vacía para almacenar los empleados, donde cada empleado será representado como un diccionario con el nombre, apellido, cargo y salario. (check)

2. Agregar empleado: El usuario ingresará el nombre, apellido, cargo y salario de un nuevo empleado para agregarlo al registro. (check)

3. Actualizar salario de empleado: El usuario ingresará el nombre y apellido de un empleado, y el nuevo salario para actualizar en el registro. (check)

4. Mostrar registro de empleados: El usuario podrá visualizar el registro actualizado de empleados, mostrando el nombre, apellido, cargo y salario de 
cada empleado.

5. Repetir hasta terminar: El usuario podrá realizar múltiples operaciones de gestión de empleados antes de decidir terminar el script.

Restricciones:
•Cada empleado debe tener una combinación única de nombre y apellido en el registro.

"""


empleados= []

def menu_principal():
    print("1. Ingresar un empleado: ")
    print("2. Actualizar un empleado: ")
    print ("3. Eliminar un empleado: ")
    print ("4. Mostrar el registro de usuario")
    print("5. Salida")
    opcion= int(input("Seleccione una de las anteriores opciones: "))
    if opcion > 0:
        return opcion
    else: 
        print("Debe ingresar un número para escoger una opción del menú")
    


def registro_empleado(nuevo_empleado):
    empleados.append(nuevo_empleado)
    mostrar_registro_empleados()
    print("+++El empleado se ha registrado correctamente +++")
 
    
def actualizar_salario(actualizacion_empleado):

    nombre = actualizacion_empleado["nombre"]
    apellido = actualizacion_empleado["apellido"]
    salario = actualizacion_empleado["nuevo-salario"]

    for empleado in empleados:
        if empleado["nombre"] == nombre and empleado["apellido"] == apellido:
            empleado["salario"] = salario
        else: 
            print("Nombre y apellido del empleado no se encuentra en el sistema")
            
    mostrar_registro_empleados()
    print(f"+++ El salario del empleado se actualizó correctamente +++")


  
# def mostrar_registro_empleados():
#     contador = 0
#     for empleado in empleados:
#         contador += 1
#         print(f"{contador}). {empleado}")
#         print("*"*50)

def mostrar_registro_empleados():
    print("*"*50)
    print("+++a continuación se mostrará el registro de empleados")
    
    for indice, empleado in enumerate(empleados, start= 1):
        print(f"Empleado: {indice}.) {empleado}")

    print("*"*50)



def eliminar_registro_empleado(eliminar_empleado):
    
    nombre = eliminar_empleado["nombre"]
    apellido = eliminar_empleado["apellido"]

    for empleado in empleados:
        if empleado["nombre"] == nombre and empleado["apellido"] == apellido:
            empleados.remove(empleado)
    print("Empleado eliminado correctamente")
    



    
        
def registro_empleados():
    while True:
        try:
            opcion = menu_principal()
        
            if opcion == 1:
                nombre = input("Ingresar el nombre del empleado: ")
                apellido = input("Ingrese el apellido del empleado: ")
                cargo = input("Ingrese el cargo del empleado: ")
                salario = float(input("Ingrese el salario del empleado: "))

                if salario < 0:
                    print("Debe ingresar una cifra valida de salario")
                else:
                    nuevo_empleado= {
                        "nombre": nombre.lower(),
                        "apellido": apellido.lower(),
                        "cargo": cargo.lower(),
                        "salario": salario
                    }

                registro_empleado(nuevo_empleado)
                
            elif opcion == 2: 
                print("Opción para Actualizar el salario del empleado")
                nombre = input("Ingresar el nombre del empleado: ")
                apellido = input("Ingrese el apellido del empleado: ")
                nuevo_salario = float(input("Ingrese el nuevo monto de salario para actualizar: "))

                if nuevo_salario < 0:
                    print("Ingrese una cifra de salario correcta")
                else:
                    actualizacion_empleado= {
                        "nombre": nombre.lower(),
                        "apellido": apellido.lower(),
                        "nuevo-salario": nuevo_salario
                    }

                actualizar_salario(actualizacion_empleado)
                
            elif opcion == 3:

                nombre_eliminar = input("Ingresar el nombre del empleado: ")
                apellido_eliminar = input("Ingrese el apellido del empleado: ")
                
                eliminar_empleado= {
                    "nombre": nombre_eliminar.lower(),
                    "apellido": apellido_eliminar.lower(),
                }

                eliminar_registro_empleado(eliminar_empleado)
                      
            elif opcion == 4:
                mostrar_registro_empleados()
            elif opcion == 5:
                break 
        except ValueError:
            print("Debe ingresar una opción correcta")    


def main():
    registro_empleados()


main()


"""

nota: el sorted()--- devuelve una lista

list() # convertir a lista
tuple() #convertir a tupla

lista_diccionarios = [
    {'nombre': 'Carlos', 'edad': 30},
    {'nombre': 'Ana', 'edad': 25},
    {'nombre': 'Felipe', 'edad': 20}
]

# Ordenar la lista de diccionarios por la clave 'nombre'
lista_ordenada = sorted(lista_diccionarios, key=lambda x: x['nombre'])

print(lista_ordenada)

v2

# Ordenar considerando que algunos diccionarios podrían no tener la clave 'nombre'
lista_ordenada = sorted(lista_diccionarios, key=lambda x: x.get('nombre', ''))

"""