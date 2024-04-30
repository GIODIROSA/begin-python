import csv
import pandas as pd #type:ignore

def cargar_datos_desde_csv(nombre_archivo):
    with open(nombre_archivo, newline='') as csvarchivo:
        lector_csv = csv.DictReader(csvarchivo)
        datos = list(lector_csv)
    return datos

def obtener_data_frame(datos):
    df = pd.DataFrame(datos, columns=datos[0])
    return df

def convertir_columna_a_numeros(df, columna):
    df[columna] = pd.to_numeric(df[columna], errors='coerce')

def mostrar_estadisticas_habitantes(data_frame):
    print("Promedio de habitantes", data_frame["Habitantes"].mean())
    print("Máximo de habitantes", data_frame["Habitantes"].max())
    print("Mínimo de habitantes", data_frame["Habitantes"].min())
    print("Suma de habitantes", data_frame["Habitantes"].sum())
    print("Mediana de habitantes", data_frame["Habitantes"].median())
    print("Desviación estándar de habitantes", data_frame["Habitantes"].std())

def mostrar_estadisticas_superficie(data_frame):
    print("Promedio de superficie", data_frame["Superficie (km2)"].mean())
    print("Máximo de superficie", data_frame["Superficie (km2)"].max())
    print("Mínimo de superficie", data_frame["Superficie (km2)"].min())
    print("Suma de superficie", data_frame["Superficie (km2)"].sum())
    print("Mediana de superficie", data_frame["Superficie (km2)"].median())
    print("Desviación estándar de superficie", data_frame["Superficie (km2)"].std())

def mostrar_cantidad_paises_por_idioma(data_frame):
    cantidad_por_idioma = data_frame.groupby("Idioma").size()
    print("Cantidad de países por idioma", cantidad_por_idioma)

def main():
    datos = cargar_datos_desde_csv("datos-paises-latam.csv")
    data_frame = obtener_data_frame(datos)

    # print(data_frame.dtypes) # Tipo de dato del DataFrame (columnas)
    # print(data_frame['Habitantes'].dtype) # Tipo de dato de la columna Habitantes
    # print("*"*50)
    # print(data_frame.sample(2))
    # print("*"*50)
    # print(data_frame.dtypes)

    # convertir_columna_a_numeros(data_frame, 'Habitantes')
    # mostrar_estadisticas_habitantes(data_frame)

    # convertir_columna_a_numeros(data_frame, 'Superficie (km2)')
    # mostrar_estadisticas_superficie(data_frame)
    
    # mostrar_cantidad_paises_por_idioma(data_frame)

main()
