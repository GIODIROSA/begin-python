# Dummies

libros = [
    {"id": 1, "nombre": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True},
    {"id": 2, "nombre": "1984", "autor": "George Orwell", "disponible": True},
    {"id": 3, "nombre": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "disponible": True},
    {"id": 4, "nombre": "El principito", "autor": "Antoine de Saint-Exupéry", "disponible": True},
    {"id": 5, "nombre": "Orgullo y prejuicio", "autor": "Jane Austen", "disponible": True},
    {"id": 6, "nombre": "Matar a un ruiseñor", "autor": "Harper Lee", "disponible": True},
    {"id": 7, "nombre": "El gran Gatsby", "autor": "F. Scott Fitzgerald", "disponible": True},
    {"id": 8, "nombre": "La odisea", "autor": "Homero", "disponible": True},
    {"id": 9, "nombre": "Harry Potter y la piedra filosofal", "autor": "J.K. Rowling", "disponible": True},
    {"id": 10, "nombre": "El señor de los anillos", "autor": "J.R.R. Tolkien", "disponible": True},
    {"id": 11, "nombre": "El Hobbit", "autor": "J.R.R. Tolkien", "disponible": True},
    {"id": 12, "nombre": "Las aventuras de Sherlock Holmes", "autor": "Arthur Conan Doyle", "disponible": True},
    {"id": 13, "nombre": "Fahrenheit 451", "autor": "Ray Bradbury", "disponible": True},
    {"id": 14, "nombre": "El alquimista", "autor": "Paulo Coelho", "disponible": True},
    {"id": 15, "nombre": "La Divina Comedia", "autor": "Dante Alighieri", "disponible": True},
    {"id": 16, "nombre": "El nombre del viento", "autor": "Patrick Rothfuss", "disponible": False},
    {"id": 17, "nombre": "El juego de Ender", "autor": "Orson Scott Card", "disponible": True},
    {"id": 18, "nombre": "Anna Karenina", "autor": "León Tolstoi", "disponible": True},
    {"id": 19, "nombre": "Los Miserables", "autor": "Victor Hugo", "disponible": True},
    {"id": 20, "nombre": "Guerra y paz", "autor": "León Tolstoi", "disponible": True},
    {"id": 21, "nombre": "Lolita", "autor": "Vladimir Nabokov", "disponible": False},
    {"id": 22, "nombre": "Ulises", "autor": "James Joyce", "disponible": True},
    {"id": 23, "nombre": "Crimen y castigo", "autor": "Fyodor Dostoyevsky", "disponible": True},
    {"id": 24, "nombre": "Jane Eyre", "autor": "Charlotte Brontë", "disponible": True},
    {"id": 25, "nombre": "El retrato de Dorian Gray", "autor": "Oscar Wilde", "disponible": False},
    {"id": 26, "nombre": "La Metamorfosis", "autor": "Franz Kafka", "disponible": True},
    {"id": 27, "nombre": "En busca del tiempo perdido", "autor": "Marcel Proust", "disponible": True},
    {"id": 28, "nombre": "El corazón de las tinieblas", "autor": "Joseph Conrad", "disponible": True},
    {"id": 29, "nombre": "Siddhartha", "autor": "Hermann Hesse", "disponible": True},
    {"id": 30, "nombre": "To Kill a Mockingbird", "autor": "Harper Lee", "disponible": False}
]



"""
Ejercicio 3: Sistema de Biblioteca Simple
Objetivo: Implementar un sistema básico para gestionar préstamos de libros en una biblioteca.

Instrucciones:

Iniciar el programa con una lista de libros disponibles (título y autor).

Permitir al usuario buscar un libro por título o autor para ver si está disponible.
Si el libro está disponible, ofrecer la opción de prestar el libro. Esto lo marcará como no disponible hasta que sea devuelto.
Permitir al usuario devolver libros, marcándolos nuevamente como disponibles.
Dar la opción al usuario de listar todos los libros y ver cuáles están disponibles y cuáles están prestados.
Repetir el proceso hasta que el usuario decida salir del programa.
Conceptos a Practicar: Listas, diccionarios, bucles, condicionales, funciones, entrada/salida estándar.

"""


"""
1) mostrar_libros 
2) prestar_libro
3) devolver_libro 
4) agregar_libro
"""




def mostrar_libros(libros):
    for libro in libros:
        id= libro["id"]
        titulo = libro["nombre"]
        autor = libro["autor"]
        disponible = "Disponible" if libro["disponible"] else "Libro No disponible, se encuentra en prestamo" 
        print(f"{id}) Título: {titulo}, Autor: {autor}, Disponible: {disponible}")

    

def prestar_libro(titulo, autor):
        for libro in libros:
            if titulo == libro["nombre"] or autor == libro["autor"]:
                if libro["disponible"]:
                    libro["disponible"]= False
                    print(f"Gracias, Disfrute del libro: {titulo} de autor: {autor} en calidad de prestamo")
                else:
                    print("El libro no esta disponible")
                return 
        print("No se encontro el libro")            
          


def devolver_libro(titulo, autor):
    for libro in libros:
      if titulo == libro["nombre"]:
          libro["disponible"] = True
          print(f"Gracias, por devolver el título: {titulo} Autor: {autor} ")
          return

    print("Opción no valida")
      

def agregar_libro(libro):
    libros.append(libro)
    print("Se agrego libro con exito")
    

# mostrar_libros(libros)
# prestar_libro("loquesea", "Franz loquesea")  
# devolver_libro("Siddhartha", "Hermann Hesse")
nuevo_libro={
    "nombre": "Nuevo Libro",
    "autor": "Giovanni Di Rosa",
    "Disponible": True 
}

agregar_libro(nuevo_libro)

