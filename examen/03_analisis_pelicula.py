"""
Ejercicio 3 / Análisis de datos de películas
•Descripción: Realice un script que permita realizar un análisis de datos de películas a partir del archivo CSV proporcionado, el cual contiene 
información sobre diferentes películas, incluyendo su título, género, director y recaudación en millones de dólares. Utilice las bibliotecas csv y 
pandas para cargar, procesar y analizar los datos respectivamente.
•Entrada: El archivo CSV que contiene los datos de las películas.
•Salida: Estadísticas que muestren el análisis de los datos de las películas. Estas deben incluir: la película con mayor recaudación, la película con 
menor recaudación y el promedio de recaudación por género.
Pasos:
1. Cargar datos desde CSV: Utilizando la biblioteca csv, cargue los datos del archivo CSV que contiene información sobre las películas. (check)

2. Procesar datos: Utilizando la biblioteca pandas, convierta los datos CSV en un DataFrame para un procesamiento más sencillo y eficiente. (check)

2.1 Calcule las estadísticas solicitadas a partir de los datos del DataFrame. (check)

3. Muestre las siguientes estadísticas:

3.1 El valor de la película con mayor recaudación (check)
3.2 el valor de la película con menor recaudación (check)
3.4 el promedio valor de recaudación por género. (check)

Retricciones:
•Valide que los campos del archivo CSV estén correctamente formateados y no contengan valores faltantes o un tipo de dato incorrecto.
    
"""

import pandas as pd #type:ignore
import csv


# function cargar datos desde el csv 
def cargar_datos_csv(archivo):
    with open(archivo, newline="", encoding='utf-8') as csvarchivo:
        lector_csv = csv.DictReader(csvarchivo)
        data = list(lector_csv)
        return data


def obtener_datos(datos):
    df= pd.DataFrame(datos[1:], columns=datos[0])
    # print(df)
    return df

# prueba de lectura 
def muestra_series(datos):
    nuevo_df= pd.Series(datos)
    print("=>", nuevo_df)
    return nuevo_df


def convertir_columna_a_numeros(df, columna):
   df[columna] = pd.to_numeric(df[columna], errors='coerce')


def mostrar_datos(datos):
    df= pd.DataFrame(datos[1:], columns=datos[0])
    valores_faltantes = df.isnull().sum()
    print("\nValores faltantes:")
    print("valores faltantes: ",valores_faltantes)
    #print(df)


def mayor_recaudación(data_frame):
    maximo_recaudado = round(data_frame["Recaudación (EUR MM)"].max(), 2)
    indice_maximo_recaudado = data_frame["Recaudación (EUR MM)"].idxmax() # idxmax
    pelicula_maxima_recaudada = data_frame.loc[indice_maximo_recaudado, "Título"]
    print(f"La película ****{pelicula_maxima_recaudada}**** recaudó más, con una cifra de: € {maximo_recaudado} millones")


def mayor_recaudacion(data_frame):
    maximo_recaudado = round(data_frame["Recaudación (EUR MM)"].max(), 2)
    indice_maximo_recaudado = data_frame["Recaudación (EUR MM)"].idxmax() # idxmax
    pelicula_maxima_recaudada = data_frame.loc[indice_maximo_recaudado, "Título"]
    print(f"La película ****{pelicula_maxima_recaudada}**** recaudó más, con una cifra de: € {maximo_recaudado} millones")


def minimo_recaudacion(data_frame):
    minimo_recaudado = round(data_frame["Recaudación (EUR MM)"].min(), 2)
    indice_minimo_recaudado = data_frame["Recaudación (EUR MM)"].idxmin() # idxmin
    pelicula_minimo_recaudada = data_frame.loc[indice_minimo_recaudado, "Título"]
    print(f"La película ****{pelicula_minimo_recaudada}**** obtuvo la menor recaudación, con una cifra de: € {minimo_recaudado} millones")



def promedio_genero_recaudacion(data_frame):
    promedio_por_genero = data_frame.groupby('Género')['Recaudación (EUR MM)'].mean().round(2)
    print(promedio_por_genero)





 # function principal - se gestiona la invocación de las function
def main():
    ####################### Get data ##############################
    datos = cargar_datos_csv("datos-ejercicio-3.csv")
    data_frame = obtener_datos(datos) 
    ##################### Conversiones #########################
    convertir_columna_a_numeros(data_frame, "Recaudación (EUR MM)")
    ################## Estadística ############################
    mostrar_datos(datos)
    mayor_recaudacion(data_frame)
    minimo_recaudacion(data_frame)
    promedio_genero_recaudacion(data_frame)
    muestra_series(datos)



main()


#print("Mínimo de superficie", data_frame["Superficie (km2)"].min())



"""
def validar_tipo_de_dato(file_path):
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(file_path)

    # Verificar los tipos de datos de cada columna
    tipos_de_dato_correctos = {
        "ID": int,
        "Título": str,
        "Género": str,
        "Director": str,
        "Recaudación (EUR MM)": float
    }

    for columna, tipo in tipos_de_dato_correctos.items():
        if df[columna].dtype == tipo:
            print(f"La columna '{columna}' tiene el tipo de dato correcto: {tipo}.")
        else:
            print(f"La columna '{columna}' tiene un tipo de dato incorrecto. Se esperaba {tipo} pero se encontró {df[columna].dtype}.")

# Llamar a la función para validar el archivo CSV
validar_tipo_de_dato('tu_archivo.csv')

"""
