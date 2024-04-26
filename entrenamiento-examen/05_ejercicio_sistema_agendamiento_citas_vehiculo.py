from datetime import datetime, timedelta


"""
Ejercicio 4  Sistema de Gestión de Citas para Pruebas de Manejo
• Descripción: Desarrolle un programa para gestionar las citas de pruebas de manejo en un concesionario de vehículos. El programa debe permitir a los clientes
programar citas para realizar pruebas de manejo y recibir confirmaciones de reserva.
• Entrada: Fecha y hora de la cita. Tipo de vehículo para la prueba de manejo. Información de contacto del cliente.
• Salida: Confirmación de reserva de la cita.
Pasos:
1. Seleccionar Fecha y Hora: Permita al cliente seleccionar una fecha y hora para la cita de la prueba de manejo, según la disponibilidad del concesionario.
2. Elegir Tipo de Vehículo: Permita al cliente elegir el tipo de vehículo que desea probar durante la cita.
3. Ingresar Información de Contacto: Solicite al cliente que ingrese su información de contacto para recibir la confirmación de la reserva.
4. Confirmar Reserva: Muestre un mensaje de confirmación de reserva al cliente, indicando la fecha, hora y detalles de la cita de la prueba de manejo..
Restricciones:
1. Debe tener en cuenta la disponibilidad de vehículos y de personal para realizar las pruebas de manejo.
2. Debe proporcionar opciones de fecha y hora que se ajusten a la agenda del concesionario
"""


vehiculos_disponibles= ["Sedan", "Suv", "Camioneta", "Deportivo"]

hora_inicio = 9
hora_cierre = 17
fecha_hora_disponible = [datetime.now().replace(hour=i, minute=0) for i in range(hora_inicio, hora_cierre)]

def agendar_cita(fecha_hora_disponible, vehiculos_disponibles):
    while True:
        print("Agendar la cita en el concesionario")
        print("1. Agendar Fecha y hora")
        print("2. Seleccionar tipo de vehiculo")
        print("3. Ver la reserva")
        print("3. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:

            for i, fecha_hora in enumerate(fecha_hora_disponible):
                print(f"{i+1}. {fecha_hora.strftime('%d-%m-%Y %H:%M')}")
            seleccion = int(input("Elige una fecha y hora: ")) - 1
            fecha_hora_seleccionada = fecha_hora_disponible[seleccion]
            print(f"Has seleccionado la fecha y hora {fecha_hora_seleccionada.strftime('%d-%m-%Y %H:%M')}")
        elif opcion == 2:
             
            for i, vehiculo in enumerate(vehiculos_disponibles):
                print(f"{i+1}. {vehiculo}")
            seleccion_vehiculo= int(input("Elige un vehiculo: ")) - 1
            vehiculo_seleccionado = vehiculos_disponibles[seleccion_vehiculo]
            print(f"Haz elegido el tipo de vehiculo: {vehiculo_seleccionado}")

        elif opcion == 3:
            break
        else:
            print("Lo siento, opción invalida")


agendar_cita(fecha_hora_disponible, vehiculos_disponibles)



