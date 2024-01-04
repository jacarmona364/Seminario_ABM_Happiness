import pandas as pd
import numpy as np
import os

def calculate_happiness(alpha, factores, decimales=0):
    # Calcular el nivel de felicidad para cada factor y redondear al número de decimales especificado
    current_happiness = [round(((factor**alpha * 8**(1-alpha)) * 5) / 11, 0) for factor in factores]
    return current_happiness

def simulated_happiness(num_agentes, archivo_excel_data, archivo_excel_results):
    # Solicitar al usuario que ingrese un valor alpha entre 0 y 1
    alpha = float(input("Ingrese un valor alpha entre 0 y 1: "))
    
    # Verificar que el valor alpha esté en el rango correcto
    while not (0 <= alpha <= 1):
        print("El valor alpha debe estar entre 0 y 1.")
        alpha = float(input("Ingrese un valor alpha entre 0 y 1: "))

    # Leer todos los valores de la primera columna desde el archivo Excel
    df = pd.read_excel(archivo_excel_data)
    primer_factores = df.iloc[:, 2].tolist()

    # Calcular los niveles de felicidad para cada agente
    happiness_score = calculate_happiness(alpha, primer_factores)

    # Crear un DataFrame con los niveles de felicidad
    df_resultado = pd.DataFrame({"Nivel_Felicidad": happiness_score})

    # Guardar el DataFrame en un archivo Excel
    df_resultado.to_excel(archivo_excel_results, index=False)
    
    print(f"Se han generado y guardado los niveles de felicidad en {archivo_excel_results}")

if __name__ == "__main__":
    # Parámetros
    num_agentes = 3000
    archivo_excel_data = "C:/Users/pepec/Desktop/4ºGIIADE/Seminario_ABM_Happiness/FaceBook/3145_data_clean_FB.xlsx"
    archivo_excel_results = "C:/Users/pepec/Desktop/4ºGIIADE/Seminario_ABM_Happiness/FaceBook/model_FB.xlsx"
    # Generar niveles de felicidad y guardar en Excel
    simulated_happiness(num_agentes, archivo_excel_data, archivo_excel_results)
