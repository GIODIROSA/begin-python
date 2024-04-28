import pandas as pd
import csv

"""
s = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(s.size)

datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
    'edad':[18, 22, 20, 21],
    'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
    'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
}

df = pd.DataFrame(datos)

print("\n")
print("*"*50)
print(df)
print("*"*50)

"""

# with open("datos-ejercicios-1.csv", newline="") as archivo_csv:
#     datos = list(csv.render(archivo_csv))
    
    
# df= pd.DataFrame(datos[1:], columns=datos[0]) #olumns para agregar las columnas a la tabla

# df["edad"] = pd.to_numeric(df["edad"], errors="coerce")

# promedio_edad = round(df["edad"].mean(), 2)
# mediana_edad = round(df["edad"].median(), 2)

# suma_horas_uso_diario_por_rango_edad = df.groupby("rango_edad")["horas_uso_diario"].sum()

# print(df)
# print(promedio_edad)
# print(mediana_edad)

with open("datos-paises-latam.csv", newline="", encoding='utf-8') as paises_archivo_cvg:
    datos = list(csv.reader(paises_archivo_cvg))

# print("datos=>", datos)

df= pd.DataFrame(datos[1:], columns=datos[0])

print("=>", df)


# def mostrar_cantidad_paises_por_idioma(data_frame):
#     cantidad_por_idioma = data_frame.groupby("Idioma").size()
#     print("Cantidad de países por idioma", cantidad_por_idioma)

