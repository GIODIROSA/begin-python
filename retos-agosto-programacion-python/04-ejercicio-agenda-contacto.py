
"""
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
"""

AGENDA= []

def ingresar_contacto(nombre, numero):
    contacto = {
        'nombre': nombre,
        'numero': numero
    }
    if nombre not in AGENDA:
       AGENDA.append(contacto)
    else:
        print(f"El contacto con nombre '{nombre}' ya existe en la agenda.")

    print("\n**AGENDA**\n")
    for index, item in enumerate(AGENDA):
        print(f"{index+1}).-", item)



def actualizar_contacto(nombre_ingresado):
    print("\n**Actualizar contacto de la agenda**\n")
    for contacto in AGENDA:
        if contacto['nombre'] == nombre_ingresado:
            nuevo_nombre= input("Ingrese el nuevo nombre: ")
            contacto['nombre'] = nuevo_nombre
            print(f"Nombre actualizado: {contacto}")
        return



def mostrar_contacto():
    print("\n**AGENDA**\n")
    for index, item in enumerate(AGENDA):
        print(f"{index + 1}).-", item)



def buscar_contacto(nombre):
    print("\n**Buscar contacto en la agenda**\n")
    buscando_nombre= nombre;
    for contacto in AGENDA:
        if contacto['nombre'] == buscando_nombre:
            print(f"Nombre: {contacto['nombre']} / Numero: {contacto['numero']}")
        return

def eliminar_contacto(nombre):
    print("\n**Eliminar el contacto en la agenda**\n")
    nueva_agenda = [contacto for contacto in AGENDA if contacto['nombre'] != nombre]
    print(f"Contacto eliminado: {nombre}")
    print("\n")
    print("\n**Agenda actualizada**\n")
    return print(nueva_agenda)



def menu_principal(texto_agenda_contacto):
    print("*"*50)
    print(f'{texto_agenda_contacto["texto_bienvenida"]}')
    print("-"*50)
    print(f'1. {texto_agenda_contacto["texto_ingresar_contacto"]}')
    print(f'2. {texto_agenda_contacto["texto_mostrar_contacto"]}')
    print(f'3. {texto_agenda_contacto["texto_actualizar_contacto"]}')
    print(f'4. {texto_agenda_contacto["texto_buscar_contacto"]}')
    print(f'5. {texto_agenda_contacto["texto_eliminar_contacto"]}')
    print(f'6. {texto_agenda_contacto["texto_finalizar_agenda"]}')
    print("*"*50)
    opciones = int(input("Seleccione una de las anteriores opciones: "))
    return opciones



def agenda_contacto(texto_agenda_contacto):
    isOn= True;
    while isOn:
      try:
          opcion= menu_principal(texto_agenda_contacto)
          if opcion == 1:
              numero= 0
              nombre= input('Ingresa el nombre del contacto: ').strip()
              telef_input= (input('Ingresa el teléfono del contacto: '))
              if telef_input.isdigit() and len(telef_input) == 9:
                  numero= int(telef_input)
              else:
                  print('Debe ser un numero valido')
                  raise ValueError

              if nombre:
                  ingresar_contacto(nombre, numero)
              else:
                  print("No ingresaste un nombre válido, por favor intenta de nuevo.")

          elif opcion == 2:
              mostrar_contacto();


          elif opcion == 3:
              nombre = input('Ingresa el nombre del contacto que desea actualizar: ').strip()
              actualizar_contacto(nombre)

          elif opcion == 4:
              nombre = input('Ingresa el nombre del contacto que desea buscar: ').strip()
              if nombre:
                buscar_contacto(nombre)

          elif opcion == 5:
              nombre = input('Ingresa el nombre del contacto que desea eliminar: ').strip()
              eliminar_contacto(nombre);

          elif opcion == 6:
              print('Gracias por finalizar el sistema de agenda. ¡Vuelve pronto!')
              isOn = False;

          else:
            print("ERROR")

      except ValueError:
          print('*'*50)
          print(f'Error debe introducir una opción correcta')
          print('*'*50)



def main():
    print("CARGA AGENDA")
    texto_agenda_contacto={
        'texto_bienvenida': 'Bienvenidos a la agenda de contacto',
        'texto_ingresar_contacto': 'Ingresar contacto',
        'texto_mostrar_contacto': 'Mostrar los contactos',
        'texto_actualizar_contacto': 'Actualizar contacto',
        'texto_buscar_contacto': 'Buscar contacto',
        'texto_eliminar_contacto': 'ELiminar contacto',
        'texto_finalizar_agenda': "Finalizar Agenda de contacto"
    }

    agenda_contacto(texto_agenda_contacto)


main();