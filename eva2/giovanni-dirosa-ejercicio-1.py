"""
Ejercicio 1: Gestión de lista de invitados para un evento. 
Descripción: Realice un script que permita al usuario gestionar una lista de invitados para un evento, donde cada invitado es representado por su nombre como una cadena de texto. El usuario podrá agregar nuevos invitados, eliminar invitados, buscar invitados por nombre y mostrar la lista de invitados actualizada.
Entrada: El usuario ingresará comandos para agregar nuevos invitados, eliminar invitados o mostrar la lista de invitados.
Salida: Dependiendo de la opción ingresada por el usuario, debe mostrar un mensaje al agregar un invitado, eliminar un invitado, buscar un invitado por nombre, o mostrar la lista de invitados.
Pasos:
•	Inicializar lista de invitados: Inicialice una lista vacía para almacenar los nombres de los invitados. (check)
•	Agregar invitado: El usuario ingresará el nombre de un nuevo invitado para agregarlo a la lista de invitados. (check)
•	Eliminar invitado: El usuario ingresará el nombre de un invitado para eliminarlo de la lista de invitados. (check)
•	Mostrar lista de invitados: El usuario podrá visualizar la lista actualizada de invitados. (check)
•	Repetir hasta terminar: El usuario podrá realizar múltiples operaciones de gestión de invitados antes de decidir terminar el script. (check)
•	Mensajes de estado: Después de cada operación realizada por el usuario, el sistema mostrará el estado de la operación.
Restricciones:
•	Cada nombre de invitado debe ser una cadena de texto no vacía. 
•	No se permiten nombres de invitados duplicados en la lista. (check)
•	Las operaciones de agregar invitado, eliminar invitado y mostrar la lista de invitados las debe realizar con una función personalizada. (check)
Entregable:
Archivo con la siguiente estructura: nombre-apellido-ejercicio-01.py

"""

invitados = []

# menú de invitados

def menu_principal():
    print("1. Agregar un invitado: ")
    print("2. Eliminar un invitado: ")
    print("3. Mostrar un invitado: ")
    print("4. Salida")
    opcion= int(input("Seleccione una de las anteriores opciones: "))
    return opcion


# function gestion de registro de invitados 

# CREATED

def agregar_invitados(nuevo_invitado):
    invitado_validar = nuevo_invitado["nombre"]
    for invitado in invitados:
        if invitado["nombre"] == invitado_validar:
            print("+"*100)
            print(f"+++++ EL INVITADO YA EXISTE +++++ {invitado}")
            print("+"*100)
            return
            
    invitados.append(nuevo_invitado)
    
    print("+"*100)
    print(invitados)
    print("Se ha registrado el invitado correctamente")
    print("+"*100)
    

    
# READ

def mostrar_registro_invitados():
    print("+"*100)
    print("+++ A continuación se mostrará el registro de invitados +++")
    
    for indice, invitado in enumerate(invitados, start= 1):
        print(f"Invitado: {indice}.) {invitado}")

    print("+"*100)
    

# DELETE

def eliminar_registro_invitado(nombre):
    print("=>", nombre)
    for invitado in invitados:
        if invitado["nombre"] == nombre:
            invitados.remove(invitado)
            print("+"*100)
            print("El invitado ha sido eliminado del registro correctamente")
            print("+"*100)
            
            mostrar_registro_invitados()


    
def registro_invitados():
    isOn= True
    while isOn:
        try:
            opcion = menu_principal()
        
            if opcion == 1:
              nombre= input("Ingresar el nombre del invitado: ") 
              
              print("nombre", nombre)
                   
              if nombre == "":
                  
                  print("+"*100)
                  print("¡¡¡DEBE!!! ++++ ingresar un nombre ++++")
                  print("+"*100)
                  
                  raise ValueError
              else:
                  nuevo_invitado = {
                  "nombre": nombre.capitalize()
              }
                  
              agregar_invitados(nuevo_invitado)
                
            elif opcion == 2: 
                nombre= input("Ingresar el nombre del invitado que desea eliminar del registro: ") 
                
                eliminar_registro_invitado(nombre)
                
            elif opcion == 3:
                
                mostrar_registro_invitados()
                      
            elif opcion == 4:
                print("¡¡¡Gracias!!! por usar el sistema de gestión de invitados. Nos vemos pronto")
                break 
            else:
                raise ValueError
        except ValueError:
            print("+"*100)
            print("¡¡¡***ERROR***!!! intente de nuevo")
            print("+"*100)    
            
            

def main():
    registro_invitados()
    


main()