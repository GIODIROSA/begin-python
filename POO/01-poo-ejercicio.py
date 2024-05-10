"""
Ejercicio 1: Crear una clase Libro
Objetivo: Practicar la definición de clases y la creación de objetos.

Descripción:

Define una clase Libro que tenga los siguientes atributos: título, autor y año de publicación.
Crea un método que imprima toda la información del libro en un formato amigable.
Crea algunos objetos de esta clase y utiliza el método para imprimir su información.
"""

class Libros:
    def __init__(self, titulo, autor, agnio):
        self.titulo = titulo
        self.autor = autor
        self.agnio = agnio
    
    def mostrar_informacion_libro(self):
        print(f"Se presenta el libro: {self.titulo} de autor: {self.autor} y el año de publicación es: {self.agnio}")

    
mi_libro = Libros("Cien año de soledad", "Gabriel Garcia Marquez", 1970)
mi_libro.mostrar_informacion_libro()