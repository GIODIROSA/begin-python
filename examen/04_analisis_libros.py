"""
Ejercicio 4 / Análisis de datos de libros
•Descripción: Realice un script que permita realizar un análisis de datos de libros a partir del archivo CSV proporcionado, el cual contiene 
información sobre diferentes libros, incluyendo su título, autor, género, año de publicación y número de páginas. Utilice las bibliotecas csv y pandas 
para cargar, procesar y analizar los datos respectivamente.
•Entrada: El archivo CSV que contiene los datos de los libros.
•Salida: Estadísticas que muestren el análisis de los datos de los libros. Estas deben incluir: el libro más antiguo, el libro más reciente, el promedio de 
páginas por género y el autor con más libros en el conjunto de datos.
Pasos:
1. Cargar datos desde CSV: Utilizando la biblioteca csv, cargue los datos del archivo CSV que contiene información sobre los libros. (check)
2. Procesar datos: Utilizando la biblioteca pandas, convierta los datos CSV en un DataFrame para un procesamiento más sencillo y eficiente. (check)
Calcule las estadísticas solicitadas a partir de los datos del DataFrame.
3. Muestre las siguientes estadísticas:

3.1 El año del libro más antiguo, (check)
3.2 el año del libro más reciente (check)
3.3 el promedio de páginas por género. (check)

Retricciones:
•Valide que los campos del archivo CSV estén correctamente formateados y no contengan valores faltantes o un tipo de dato incorrecto
"""

import pandas as pd #type:ignore
import csv


def cargar_datos_csv(archivo):
    with open(archivo, newline="", encoding='utf-8') as csarchivo:
        lector_csv = csv.DictReader(csarchivo)
        data = list(lector_csv)
        return data 


def obtener_datos(datos):
    df= pd.DataFrame(datos[1:], columns=datos[0])
    valores_faltantes = df.isnull().sum()
    print("\nValores faltantes:")
    print(valores_faltantes)
    return df


def convertir_columna_a_numeros(df, columna):
   df[columna] = pd.to_numeric(df[columna], errors='coerce')
   

def libro_mas_antiguo(data_frame):
    libro_mas_antiguo = round(data_frame["Año de publicación"].min())
    indice_libro_mas_antiguo = data_frame["Año de publicación"].idxmin() 
    titulo_libro_mas_antiguo = data_frame.loc[indice_libro_mas_antiguo, "Título"]
    autor_libro_mas_antiguo = data_frame.loc[indice_libro_mas_antiguo, "Autor"]
    print(f"El libro más antiguo: ++++{titulo_libro_mas_antiguo}++++, del autor: {autor_libro_mas_antiguo} y data del año: {libro_mas_antiguo} D.C")



def libro_mas_reciente(data_frame):
    df= data_frame[data_frame['Año de publicación'] != False]
    libro_mas_reciente = round(df["Año de publicación"].max())
    indice_libro_mas_reciente = df["Año de publicación"].idxmax() 
    titulo_libro_mas_reciente = df.loc[indice_libro_mas_reciente, "Título"]
    autor_libro_mas_reciente = df.loc[indice_libro_mas_reciente, "Autor"]
    print(f"El libro más antiguo: ++++{titulo_libro_mas_reciente}++++, del autor: {autor_libro_mas_reciente} y data del año: {libro_mas_reciente} D.C")



def promedio_pagina_genero(data_frame):
    promedio_pagina_genero = data_frame.groupby('Género')['Número de páginas'].mean().round(2)
    print(promedio_pagina_genero)



def main():
    archivo = "datos-ejercicio-4.csv"
    datos = cargar_datos_csv(archivo)
    data_frame = obtener_datos(datos)

    convertir_columna_a_numeros(data_frame, "Año de publicación")
    convertir_columna_a_numeros(data_frame, "Número de páginas")
    
    libro_mas_antiguo(data_frame)
    libro_mas_reciente(data_frame)
    promedio_pagina_genero(data_frame)
    

   
main()


