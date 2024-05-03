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
    print("///", df)
    return df

# def mostrar_datos(datos):
#     df= pd.DataFrame(datos[1:], columns=datos[0])
#     valores_faltantes = df.isnull().sum()
#     print("\nValores faltantes+:")
#     print("valores faltantes+: ",valores_faltantes)
#     print(df)

def mostrar_datos(datos):
    df = obtener_datos(datos)  # Reutiliza la función obtener_datos
    # Calcular valores faltantes
    valores_faltantes = df.isnull().sum()
    print("\nValores faltantes:")
    print(valores_faltantes)
    
    # Opción 1: Eliminar filas con valores null
    df_limpio = df.dropna()
    print("\nDataFrame sin filas con valores null:")
    print(df_limpio)

    # Opción 2: Rellenar los valores null con un valor predeterminado, por ejemplo, 0 o una cadena vacía
    df_rellenado = df.fillna(0)  # Cambia 0 por cualquier otro valor predeterminado relevante
    print("\nDataFrame con valores null rellenados con 0:")
    print(df_rellenado)

    # Opción 3: Más complejo, como rellenar con la media de la columna si es numérica
    for columna in df.columns:
        if df[columna].dtype in ['float64', 'int64']:  # Solo para columnas numéricas
            df[columna].fillna(df[columna].mean(), inplace=True)
    print("\nDataFrame con valores null en columnas numéricas rellenados con la media:")
    print(df)



# prueba de lectura 
def muestra_series(datos):
    nuevo_df= pd.Series(datos)
    print("=>", nuevo_df)
    return nuevo_df


def muestra_series3(df, nombre_columna):
    print("nombre columna", nombre_columna)
    if nombre_columna in df.columns:
        nuevo_df = pd.Series(df[nombre_columna].values, name=nombre_columna)
        print("=>", nuevo_df)
        return nuevo_df
    else:
        print(f"Error: La columna '{nombre_columna}' no existe en el DataFrame.")
        return None
    

def muestra_series4(df, nombres_columnas):
    # Asegurarse de que todas las columnas especificadas existen en el DataFrame
    if all(columna in df.columns for columna in nombres_columnas):
        # Crear un nuevo DataFrame solo con las columnas especificadas
        nuevo_df = df[nombres_columnas]
        print("------->", nuevo_df)
        return nuevo_df
    else:
        # Identificar las columnas faltantes para mostrar en el mensaje de error
        columnas_faltantes = [columna for columna in nombres_columnas if columna not in df.columns]
        print(f"Error: Las columnas {columnas_faltantes} no existen en el DataFrame.")
        return None



def convertir_columna_a_numeros(df, columna):
   df[columna] = pd.to_numeric(df[columna], errors='coerce')



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
    # muestra_series2(datos)

    # df = pd.DataFrame(datos, columns=['ID', 'Título', 'Género', 'Director', 'Recaudación (EUR MM)'])
    df = pd.DataFrame(datos, columns=['Director'])
    serie_columna = muestra_series3(df, 'Director')
    print(serie_columna)


    df_other = pd.DataFrame(datos)
    columnas_deseadas= ['Director', 'Título']
    df_resultado = muestra_series4(df_other, columnas_deseadas)
    print(df_resultado)


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

"""

# Supongamos que tienes una lista de listas con datos
datos = [['1', 'Avengers: Endgame', 'Acción', 'Anthony Russo', '2518.0'],
         ['2', 'Avatar', 'Ciencia ficción', 'James Cameron', '2511.4'],
         ...]

# Convertir la lista a DataFrame
df = pd.DataFrame(datos, columns=['ID', 'Título', 'Género', 'Director', 'Recaudación (EUR MM)'])

def muestra_series3(df, nombre_columna):
    if nombre_columna in df.columns:
        nuevo_df = pd.Series(df[nombre_columna].values, name=nombre_columna)
        print("=>", nuevo_df)
        return nuevo_df
    else:
        print(f"Error: La columna '{nombre_columna}' no existe en el DataFrame.")
        return None

# Llamar a la función con el DataFrame y el nombre de la columna que deseas
serie_columna = muestra_series3(df, 'Director')

"""