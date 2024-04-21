"""
Ejercicio 1 / Calculadora de potencia
• Descripción: Escriba un programa que calcule la potencia de un número ingresado por el usuario elevado a una potencia también ingresada por el usuario.
• Entrada: El programa solicitará al usuario que ingrese la base y el exponente.
• Salida: El programa mostrará el resultado de elevar la base al exponente.
Pasos:
1. Solicitar al usuario que ingrese la base y el exponente.
2. Calcular la potencia utilizando la función de potenciación en Python (**).
3. Mostrar el resultado de la potencia calculada.
Restricciones:
1. El programa debe manejar correctamente números enteros o decimales positivos para la base y el exponente.
"""


def solicitar_potencia(mensaje):
    while True:
        try:
            valor= int(input(mensaje))
            if valor < 0:
                raise ValueError
            return valor
        except ValueError:
            print("El valor debe ser un numero positivo y no decimal")

def calcular_potencia(base, potencia):
    resultado= base ** potencia
    return resultado


def main():
    base= solicitar_potencia("Por favor, ingrese la base: ")
    potencia= solicitar_potencia("Por favor, ingrese la potencia: ")
    print("El calculo de la potencia es: ", calcular_potencia(base, potencia))

main()
