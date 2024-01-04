import pandas as pd

# Ruta del archivo Excel
excel_file_path = 'C:/Users/pepec/Desktop/4ºGIIADE/Seminario_ABM_Happiness/3145_data.xlsx'

# Especificar las columnas que deseas extraer
columnas_deseadas = ["P65", "P69", "P60A", "P21A05"]

# Cargar el archivo Excel en un DataFrame y seleccionar las columnas deseadas
df = pd.read_excel(excel_file_path, usecols=columnas_deseadas)

# Filtrar las filas donde la primera columna es igual a 1 y la segunda columna es igual a 1
filas_con_uno = df[(df.iloc[:, 0] == 1) & (df.iloc[:, 1] == 1) & (df.iloc[:, 2] != 99)].copy()

# Cambiar el rango de valores de la tercera columna de 0-10 a 0-5
filas_con_uno.loc[:, "P69"] = filas_con_uno["P69"].replace({0:0, 1:0, 2:1, 3:1, 4:2, 5:2, 6:3, 7:3, 8:4, 9:4, 10:5})

# Mostrar las filas filtradas
print(filas_con_uno)

# Guardar las filas filtradas en un nuevo archivo Excel
nuevo_excel_path = 'C:/Users/pepec/Desktop/4ºGIIADE/Seminario_ABM_Happiness/Instagram/3145_data_clean_IG.xlsx'
filas_con_uno.to_excel(nuevo_excel_path, index=False)
