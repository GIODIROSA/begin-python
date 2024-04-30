
"""
Ejercicio 5 / Juego de Adivinanza de Palabras
•Descripción: Desarrolle un juego en el que el jugador debe adivinar una palabra secreta, letra por letra. El jugador tiene un número limitado de intentos para 
adivinar la palabra completa.
•Entrada: Letra propuesta por el jugador como adivinanza.
•Salida: Estado actual de la palabra enmascarada, mostrando las letras adivinadas y las letras aún no adivinadas. Indicación de si la letra propuesta por el 
jugador está en la palabra secreta.
Pasos:
1. Generar Palabra Secreta: El sistema elige aleatoriamente una palabra secreta de una lista predefinida. check
2. Mostrar Palabra Enmascarada: El sistema muestra al jugador la palabra enmascarada, con todas las letras ocultas excepto la primera. check
3. Pedir Adivinanza al Jugador: El sistema solicita al jugador que adivine la siguiente letra de la palabra, mostrando cuántos intentos le quedan (5 intentos máximo). check
4. Verificar Adivinanza: El sistema compara la letra propuesta por el jugador con la palabra secreta. check
4.1 Si la letra está en la palabra secreta, el sistema actualiza la 
palabra enmascarada para mostrar la letra adivinada en su posición correcta. 
4.2 Si la letra no está en la palabra secreta, el sistema informa al jugador y reduce el 
número de intentos restantes. check
5. Repetir hasta adivinar o agotar Intentos: El proceso de adivinanza se repite hasta que el jugador adivine la palabra secreta o agote todos sus intentos.
Restricciones:
1. El juego debe ser capaz de manejar solo una palabra, check
1.1 si el texto ingresado es mayor a una palabra devolver error. check
"""

import pandas as pd


def generador_palabra():
    palabras = ["perro", "brazo", "cable", "dulce", "fresa", "globo"]
    serie = pd.Series(palabras)
    palabra_random = serie.sample().iloc[0]
    return palabra_random


def enmascarar_palabra(palabra, letras_adivinadas):
    letras_adivinadas.add(palabra[0])
      
    mascara = [letra if letra in letras_adivinadas else '_' for letra in palabra]
    
    mascara_str = ' '.join(mascara)
    
    return print(f"Adivina la palabra: {mascara_str}")



def adivinar_palabra(palabra_random):
    intento = 5
    letras_adivinadas = set()
    while intento > 0:
        try:
            print("Palabra que debe adivinar: ")
            enmascarar_palabra(palabra_random, letras_adivinadas)
            letra = input("Por favor, ingrese una letra: ")
            if len(letra) > 1:
                print("*"*50)
                print("¡¡¡¡¡ERROR!!!!! Debe ingresar solo una letra")
                print("*"*50)
                continue
            else: 
                letra_ingresada_usuario = letra

            if letra_ingresada_usuario in palabra_random:
                letras_adivinadas.add(letra_ingresada_usuario)
                print(f"La letra ingresada: {letra_ingresada_usuario} si está en la palabra por adivinar continua intentando")
                if all(letra in letras_adivinadas for letra in palabra_random):
                   print("¡Felicidades! Has adivinado la palabra completa.")
                   break

            else:
                print("Incorrecto, la letra no esta en la palabra")
                intento -= 1
                print(f"Numero de intento restante: {intento}")

            if intento == 0:
                raise ValueError
        except ValueError:
            print("Se acabo el numero de intentos")
            break

   

def main():
    palabra_random = generador_palabra()
    adivinar_palabra(palabra_random)


main()



"""
if 'mera' in 'esmeralda':  # esto nos devolverá True
    print('mera existe en esmeralda.')
else:
    print('mera no existe en esmeralda.')


Agua - Líquido esencial para la vida.
Brazo - Parte del cuerpo humano.
Cable - Utilizado para transmitir electricidad o datos.
Dulce - Alimento con sabor azucarado.
Fresa - Fruta roja y pequeña.
Globo - Objeto inflable que flota en el aire.

"""

