"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
"""

a= 10
b = a
b = 20

print(f"El valor de a: {a}")
print(f"El valor de b: {b}")

x = 10
def calcular(x: int):
    x = 20

print(f"Se imprime el valor de x = {x}")


## Referencia

def modifica_lista(my_list: list):
    my_list.append(4)

lst = [1,2,3]
modifica_lista(lst)
print(lst)


print("*"*50)

valor1= 5
valor2= 20

def value(valor_a: int, valor_b: int)-> tuple:
    temp = valor_a
    valor_a = valor_b
    valor_b = temp
    return valor_a, valor_b


valor_nuevo_a, valor_nuevo_b = value(valor1, valor2)

print("Valor_original de a", valor1)
print("valor_orginal de b", valor2)
print("valor_nuevo_a", valor_nuevo_a)
print("valor_nuevo_b", valor_nuevo_b)

list1= [10, 20]
list2 = [30, 40]

def ref(value_a : list , value_b: list):
    temp = value_a
    temp.append(50)
    value_a = value_b
    value_b = temp
    return value_a, value_b

value_list_a, value_list_b = ref(list1, list2)
print("Valor original lista 1", list1)
print("Valor origina lista 2", list2)
print("valor nuevo list 1", value_list_a)
print("valor nuevo list 2", value_list_b)