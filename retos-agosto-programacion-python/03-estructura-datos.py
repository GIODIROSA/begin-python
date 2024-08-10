"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
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

#LISTA
listas= ["Bonatti", "Di Rosa", "Brugnoli", "Errazurriz"]
"""
print(listas[0]);
print(listas[1]);
print(listas[2]);
print(listas[3]);
"""
#RECORRER UNA LISTA
for artista in listas:
    print("=>", artista)
    print("-" * 50)

print("último elemento de la lista: ",listas[-1])

#INSERTAR ELEMENTOS EN UNA LISTA
"""
listas.append("Barba")
for artista in listas:
    print("=>", artista)
    print("-" * 50)

print("último elemento de la lista: ",listas[-1])

"""

#ELIMINAR ELEMENTOS DE UNA LISTA
"""
del listas[3]
for artista in listas:
    print("=>", artista)
    print("-" * 50)
"""

listas.append("Barba")
for index, artista in enumerate(listas):
    print(index + 1, artista)
    print("-" * 50)

#Mezclar dos listas

artistas = ["Dino Di Rosa", "Jorge Balmes", "Gracia Barrios", "Brugnoli", "Bonatti", "Mathei"]
disciplinas = ["Pintura", "Grabado", "Instalación", "Dibujo", "Color"]
for artista, disciplina in zip(artistas, disciplinas):
    print("=>", artista, disciplina)


#Longitud
colaboradores = ["Giovanni", "Catalina", "Giselle"]
for item in range(0, len(colaboradores)):
    print(colaboradores[item])


# Utiliza operaciones de inserción, borrado, actualización y ordenación.




