
import pandas as pd
import csv


def cargar_datos_csv(archivo):
    with open(archivo, newline="", encoding='utf-8') as csvarchivo:
        lector_csv = csv.DictReader(csvarchivo)
        data = list(lector_csv)
        return data


def obtener_datos(datos):
    df= pd.DataFrame(datos[1:], columns=datos[0])
    # print(df)
    return df

def convertir_columna_a_numeros(df, columna):
    df[columna] = pd.to_numeric(df[columna], errors='coerce')


def convertir_columna_a_string(df, columna):
    df[columna] = df[columna].astype(str)


def mostrar_paises_por_idioma(data_frame):
    cantidad_por_idioma = data_frame.groupby("pais")["idioma"].size()
    print("Idiomas usados en cada país:", cantidad_por_idioma)

def mostrar_paises_republicanos(data_frame):
    paises_con_sistema_republicano = data_frame[data_frame["tipo_gobierno"] == "República"]
    print("Paises con sistema de gobierno republicano: ", paises_con_sistema_republicano["pais"].tolist())

def mostrar_paises_socialista(data_frame):
    paises_con_sistema_republicano = data_frame[data_frame["tipo_gobierno"] == "Socialista"]
    print("Paises con sistema de gobierno socialista: ", paises_con_sistema_republicano["pais"].tolist())

def mostrar_paises_monarquico(data_frame):
    paises_con_sistema_republicano = data_frame[data_frame["tipo_gobierno"] == "Monarquía constitucional"]
    print("Paises con sistema de gobierno monarquía constitucional: ", paises_con_sistema_republicano["pais"].tolist())

def promedio_IPC(data_frame):
    promedio = round(data_frame["ipc"].mean(), 2)
    print("Promedio del IPC entre los países de América", promedio)
    

def maximo_IPC(data_frame):
    maximo_IPC = round(data_frame["ipc"].max(), 2)

    # busca el indice del pais con el ipc mas alto.
    indice_maximo_IPC = data_frame["ipc"].idxmax()

    # trae el nombre del pais con el indice buscado anteriormente
    pais_maximo_IPC = data_frame.loc[indice_maximo_IPC, 'pais']

    print("El máximo IPC entre los países de América es", maximo_IPC, "y corresponde a", pais_maximo_IPC)


def paises_habla_espanol_con_menor_ipc(data_frame):
    # Agrupar por idioma
    paises_habla_espanol = data_frame[data_frame["idioma"] == "Español"]

    # Sacar el minimo de ipc a los paises agrupados
    menor_IPC = round(data_frame["ipc"].min(), 2)

    # Buscar el indice dentro de los paises con menor ipc
    indice_menor_IPC = paises_habla_espanol["ipc"].idxmin()
    
    # Al obtener el indice del país buscar el nombre de pais
    pais_menor_IPC_hispano_hablante = data_frame.loc[indice_menor_IPC, "pais"]

    print(f"El menos IPC entre los países hispano-hablante es: {menor_IPC} y corresponde a: {pais_menor_IPC_hispano_hablante} ")


def desviación_superficie(data_frame): 
        superficie= round(data_frame["superficie"].std(), 2)
        print(f"La desviación de la superficie entre paises es: {superficie}")

def grupo_paises_zona_horaria(data_frame):
        grupo_paises = data_frame[(data_frame["zona_horaria"] == "UTC-4") | (data_frame["zona_horaria"] == "UTC-6")]
        print("Idiomas usados en cada país:", grupo_paises["pais"].tolist())

def total_habitante_en_continente_americano(data_frame):
     total_habitante = data_frame["habitantes"].sum(), 2
     print(f"Total de habitante en el continente americano es: {total_habitante}")


def promedio_habla_inglesa(data_frame):
     paises_habla_ingles= data_frame[data_frame["idioma"] == "Inglés"]
     media_habitantes = round(paises_habla_ingles["habitantes"].mean())

     print(f"La media de paises de habla inglesa es: {media_habitantes}")



def main():
    datos = cargar_datos_csv("datos-paises-latam.csv")
    data_frame = obtener_datos(datos)
    # mostrar_paises_por_idioma(data_frame)
    # convertir_columna_a_numeros(data_frame, "habitantes")
    # convertir_columna_a_string(data_frame, "pais")
    # convertir_columna_a_string(data_frame, "tipo_gobierno")
    # mostrar_paises_socialista(data_frame)
    # mostrar_paises_monarquico(data_frame)
    #mostrar_paises_republicanos(data_frame)
    convertir_columna_a_numeros(data_frame, "ipc")
    convertir_columna_a_numeros(data_frame, "superficie")
    convertir_columna_a_numeros(data_frame, "habitantes")
    # promedio_IPC(data_frame)
    # maximo_IPC(data_frame)
    # paises_habla_espanol_con_menor_ipc(data_frame)
    # desviación_superficie(data_frame)
    # grupo_paises_zona_horaria(data_frame)
    # total_habitante_en_continente_americano(data_frame)
    promedio_habla_inglesa(data_frame)



    # print("=>number", data_frame['habitantes'].dtype)
    # print("=>strg", data_frame['pais'].dtype)


    

main()



# print("Mediana de superficie", data_frame["Superficie (km2)"].median())