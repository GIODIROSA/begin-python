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

with open("datos-ejercicios-1.csv", newline="") as archivo_csv:
    datos = list(csv.render(archivo_csv))
    
    
df= pd.DataFrame(datos[1:], columns=datos[0]) #olumns para agregar las columnas a la tabla

df["edad"] = pd.to_numeric(df["edad"], errors="coerce")



print(df)