"""
Generador de reporte de gastos mensuales

Descripción: Desarrolle un programa que genere un reporte de los gastos mensuales de un usuario, clasificados por categorías. El programa debe permitir al
usuario ingresar los gastos de cada categoría y mostrar un resumen al final.
• Entrada: Los gastos de cada categoría (números reales).
• Salida: Un reporte de los gastos mensuales por categoría.
Pasos:
1. Ingresar Gastos por Categoría: Solicite al usuario que ingrese los gastos correspondientes a cada categoría.
2. Almacenar Gastos: Guarde los gastos ingresados en una estructura de datos adecuada, como un diccionario donde las claves son las categorías y los valores
son las listas de gastos.
3. Mostrar Reporte: Itere sobre las categorías y muestre los gastos correspondientes.
Restricciones:
1. Los gastos deben ser números reales positivos.
"""

gastos = {
    1: {"categoria": "alimentos", "gasto": 0},
    2: {"categoria": "servicios", "gasto": 0},
    3: {"categoria": "ropa", "gasto": 0},
    4: {"categoria": "entretenimiento", "gasto": 0},
    5: {"categoria": "comics", "gasto": 0}
}


def generar_reporte():
    reporte = "El Reporte de gastos:\n "
    for clave, detalles in gastos.items():
        categoria = detalles["categoria"]
        valor = detalles["gasto"]
        reporte += f"{categoria}=> gasto:{valor}\n "

    mensaje = "¡Atención! El valor es 0." if valor == 0 else ""
        
    print("\n" + "*" * 50 + "\n")
    print(reporte)
    print(mensaje)
    print("\n" + "*" * 50 + "\n")


def menu_principal():
    print("\n1. Categoria alimentos")
    print("2. Categoria servicios")
    print("3. Categoria ropa")
    print("4. Categoria entretenimiento")
    print("5. Categoria comics")
    print("6. Generar Reporte")
    print("7. Salir")
    opcion = int(input("Seleccione una opcion: "))
    return opcion



def main():
    while True:
        try:
            opcion = menu_principal()
            if opcion == 1:
                gasto = int(input("Ingrese el monto gastado: "))
                if gasto < 0:
                    raise ValueError
                else:
                    gastos[1]["gasto"] = gasto
            elif opcion == 2:
                gasto = int(input("Ingrese el monto gastado: "))
                if gasto < 0:
                    raise ValueError
                else:
                    gastos[2]["gasto"] = gasto
            elif opcion == 3:
                 gasto = int(input("Ingrese el monto gastado: "))
                 if gasto < 0:
                    raise ValueError
                 else:
                    gastos[3]["gasto"] = gasto
            elif opcion == 4:
                gasto = int(input("Ingrese el monto gastado: "))
                if gasto < 0:
                    raise ValueError
                else:
                    gastos[4]["gasto"] = gasto
            elif opcion == 5:
                 gasto = int(input("Ingrese el monto gastado: "))
                 gastos[5]["gasto"] = gasto
            elif opcion == 6:
               generar_reporte()
            elif opcion == 7:
                print("Gracias por ingresar al sistema de reporte de gastos")
                break
            else:
                raise ValueError
        except ValueError:
            print("Los valores deben ser positivos y enteros")

main()
   
    

