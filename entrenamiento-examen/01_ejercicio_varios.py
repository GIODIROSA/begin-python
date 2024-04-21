"""
Descripción: Escriba un programa que calcule la potencia de un número ingresado por el usuario elevado a una potencia también ingresada por el
usuario.
• Entrada: El programa solicitará al usuario que ingrese la base y el exponente.
• Salida: El programa mostrará el resultado de elevar la base al exponente.
Pasos:
1. Solicitar al usuario que ingrese la base y el exponente.
2. Calcular la potencia utilizando la función de potenciación en Python (**).
3. Mostrar el resultado de la potencia calculada.
Restricciones:
1. El programa debe manejar correctamente números enteros o decimales positivos para la base y el exponente.
"""

def solicitar_valores(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError as ve:
            print(f"El número debe ser entero y positivo, Error: {ve}")

def calcular_potencia(base, exponente):
    calculo = base ** exponente
    return calculo    

def main():
    base = solicitar_valores("Ingresar el valor de la base: ")
    exponente = solicitar_valores("Ingresar el valor del exponente: ")
    mostrar_calculo = round(calcular_potencia(base, exponente))
    print(f"El calculo de la potencía es: {mostrar_calculo}")


main()