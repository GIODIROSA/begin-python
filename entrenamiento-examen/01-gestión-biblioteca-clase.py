libros = [
    {"título": "El principito", "autor": "Antoine de Saint-Exupéry", "disponible": True},
    {"título": "El túnel", "autor": "Ernesto Sabato", "disponible": True},
    {"título": "Cien años de soledad",
        "autor": "Gabriel García Márquez", "disponible": False},
    {"título": "El amor en los tiempos del cólera",
        "autor": "Gabriel García Márquez", "disponible": True},
    {"título": "Rayuela", "autor": "Julio Cortázar", "disponible": False}
]


def mostrar_libros():
    for libro in libros:
        titulo = libro["título"]
        disponible = "Disponible" if libro["disponible"] else "No disponible"
        mensaje = f"Título: {titulo}, Estado: {disponible}"
        print(mensaje)


def agregar_libro(libro):
    libros.append(libro)
    print("Libro agregado con éxito.")


def prestar_libro(titulo):
    for libro in libros:
        if libro["título"] == titulo:
            if libro["disponible"]:
                libro["disponible"] = False
                print("Libro prestado con éxito.")
            else:
                print("El libro ya está prestado.")
            return
    print("Libro no encontrado.")


def devolver_libro(titulo):
    for libro in libros:
        if libro["título"] == titulo:
            if not libro["disponible"]:
                libro["disponible"] = True
                print("Libro devuelto con éxito.")
            else:
                print("El libro ya está disponible.")
            return
    print("Libro no encontrado.")


def mostrar_menu():
    print("\n1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar estado de los libros")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion


def principal():
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            nuevo_libro = {"título": titulo,
                           "autor": autor, "disponible": True}
            agregar_libro(nuevo_libro)
        elif opcion == 2:
            titulo = input("Ingrese el título del libro a prestar: ")
            prestar_libro(titulo)
        elif opcion == 3:
            titulo = input("Ingrese el título del libro a devolver: ")
            devolver_libro(titulo)
        elif opcion == 4:
            mostrar_libros()
        elif opcion == 5:
            break
        else:
            print("Opción inválida.")


principal()
