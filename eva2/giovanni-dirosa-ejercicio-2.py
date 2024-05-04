"""

Ejercicio 2: Análisis de datos de sistemas operativos.
Utilizar archivo adjunto datos-ejercicio-02.csv. (check)
Descripción: Realice un script que permita realizar un análisis de datos de sistemas operativos a partir del archivo CSV proporcionado, el cual contiene información sobre diferentes sistemas operativos, la empresa que los distribuye y sus cantidades de descargas. Utilice las bibliotecas csv y pandas para cargar, procesar y analizar los datos respectivamente.
Entrada: El archivo CSV que contiene los datos de los sistemas operativos. (check)
Salida: Estadísticas que muestren el análisis de los datos de los sistemas operativos. Estas deben incluir: 

el valor más alto de descarga, 
el valor más bajo de descarga y 
el promedio de valor de descarga por empresa

Pasos:
•	Cargar datos desde CSV: Utilizando la biblioteca csv, cargue los datos del archivo CSV que contiene información sobre los sistemas operativos. (check)
•	Procesar datos: Utilizando la biblioteca pandas, convierta los datos CSV en un DataFrame para un procesamiento más sencillo y eficiente. Calcule las estadísticas solicitadas a partir de los datos del DataFrame. (check)
•	Mostrar resultados: Muestre las siguientes estadísticas:
o	El valor de descarga más alto (check)
o	El valor de descarga más bajo (check)
o	El promedio de valor de descarga por empresa. ()
Restricciones:
•	Valide que los campos del archivo CSV estén correctamente formateados y no contengan valores faltantes o un tipo de dato incorrecto. (check)
Entregable:
•	Archivo con la siguiente estructura: nombre-apellido-ejercicio-02.py

"""

# importaciones de librerias 

import pandas as pd 
import csv

# Get data

def cargar_datos_csv(archivo):
    with open(archivo, newline="", encoding='utf-8') as csarchivo:
        lector_csv = csv.DictReader(csarchivo) 
        data = list(lector_csv)
        return data 


def obtener_datos(datos):
    df= pd.DataFrame(datos)
    valores_faltantes = df.isnull().sum()
    print("\nValores faltantes:")
    print(valores_faltantes)
    return df


# convertir a number

def convertir_columna_a_numeros(df, columna):
   df[columna] = pd.to_numeric(df[columna], errors='coerce')

    
# Estadística

def valor_mas_alto_descargas(data_frame):
    valor_mas_alto_descargas = round(data_frame["Descargas (millones)"].max())
    print("+"*100)
    print(f"El valor más alto en descargas de sistema operativo es: {valor_mas_alto_descargas} millones en descargas")
    
    
def valor_mas_bajo_descargas(data_frame):
    valor_mas_bajo_descargas = round(data_frame["Descargas (millones)"].min())
    print("+"*100)
    print(f"El valor más bajo en descargas de sistema operativo es: {valor_mas_bajo_descargas} millones en descargas")
    
    
def promedio_valor_descarga_empresa(data_frame):
    promedio_valor_descarga_empresa = data_frame.groupby('Empresa')['Descargas (millones)'].mean().round(2)
    print("+"*100)
    print(f"El promedio de descarga por Empresa es el siguiente: {promedio_valor_descarga_empresa}")



def main():
    
    # get data
    archivo = "datos-ejercicio-02.csv"
    datos = cargar_datos_csv(archivo)
    data_frame = obtener_datos(datos)
    
    # convertir a number
    convertir_columna_a_numeros(data_frame, "Descargas (millones)")
    
    # estadística 
    valor_mas_alto_descargas(data_frame)
    valor_mas_bajo_descargas(data_frame)
    promedio_valor_descarga_empresa(data_frame)
    

   
main()

