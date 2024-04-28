import pandas as pd
import csv

def cargar_datos_csv(archivo):
    with open(archivo, newline="", encoding='utf-8') as csvarchivo:
        lector_csv = csv.DictReader(csvarchivo)
        data = list(lector_csv)
        return data

      

print("===>", cargar_datos_csv("datos-ejercicio-3.csv"))


