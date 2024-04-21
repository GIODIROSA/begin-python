
from libros import libros

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




def mostrar_libros(libros):
    for libro in libros:
        id= libro["id"]
        titulo = libro["nombre"]
        autor = libro["autor"]
        disponible = "Disponible" if libro["disponible"] else "Libro No disponible, se encuentra en prestamo" 
        # print(f"{id}) Título: {titulo}, Autor: {autor}, Disponible: {disponible}")

    

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
    print(titulo, autor)
      


mostrar_libros(libros)
prestar_libro("loquesea", "Franz loquesea")    