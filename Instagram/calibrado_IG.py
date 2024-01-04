import pandas as pd
import numpy as np

# Rutas de los archivos Excel
excel_file_path1 = 'C:/Users/pepec/Desktop/4ºGIIADE/Seminario_ABM_Happiness/Instagram/3145_data_clean_IG.xlsx'
excel_file_path2 = 'C:/Users/pepec/Desktop/4ºGIIADE/Seminario_ABM_Happiness/Instagram/model_IG.xlsx'

# Leer los archivos Excel en DataFrames
df1 = pd.read_excel(excel_file_path1)
df2 = pd.read_excel(excel_file_path2)

# Seleccionar la tercera columna del primer DataFrame y la primera columna del segundo DataFrame
happiness_data = df1.iloc[:, 2]
happiness_model = df2.iloc[:, 0]

# Calcular la media de cada columna
mean_data = happiness_data.mean()
mean_model = happiness_model.mean()

# Calcular las desviaciones con respecto a la media
deviation_data = happiness_data - mean_data
deviation_model = happiness_model - mean_model

# Calcular la suma de los productos de las desviaciones
sum_of_products = (deviation_data * deviation_model).sum()

# Calcular las sumas de los cuadrados de las desviaciones
sum_of_squares_data = (deviation_data ** 2).sum()
sum_of_squares_model = (deviation_model ** 2).sum()

# Calcular la raíz cuadrada del producto de las sumas de los cuadrados de las desviaciones
sqrt_product_of_sums_of_squares = np.sqrt(sum_of_squares_data * sum_of_squares_model)

# Calcular el coeficiente de correlación
if sqrt_product_of_sums_of_squares != 0:
    correlation_coefficient = sum_of_products / sqrt_product_of_sums_of_squares
    print(f"El coeficiente de correlación entre las columnas es: {correlation_coefficient}")
else:
    print("No se puede calcular el coeficiente de correlación. La raíz cuadrada del producto de las sumas de los cuadrados de las desviaciones es cero.")
