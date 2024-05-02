import pandas as pd #type: ignore
import csv
import random

def cargarArchivo():
    palabras_df = pd.read_csv("palabras.csv")
    palabras = palabras_df['Palabras'].to_list()
    return palabras

def seleccionAleatoria():
    palabra_secreta = random.choice(cargarArchivo())
    return palabra_secreta

def JuegoAhorcado():
    palabra_secreta = seleccionAleatoria()
    palabra_oculta = ["_"] *  len(palabra_secreta)
    intentos = 6
    while("_" in palabra_oculta and intentos > 0):
        print("Palabra a adivinar:"," ".join(palabra_oculta))
        
        letra = input("Ingresar letra a evaluar: ")
        if letra in palabra_secreta:
            print("Bien! adivinaste una letra")
            
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_oculta[i] = letra
        else: 
            print("Le siente :'< no existe la letra en la palabra secreta")
            intentos -= 1
            print("Te quemaste ... te quedán ", intentos, " intentos ")
            
    if "_" not in palabra_oculta:
        print("Bien Ganaste... adivinaste toda la palabra!")
        
        
JuegoAhorcado()