import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# a) Crear DataFrame de tareas
tareas_df = pd.DataFrame({"Nombre": [f"Tarea_{i}" for i in range(1, 46)]})

# b) Crear DataFrame de personal
# Generar datos aleatorios para el personal
nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Laura"]
edades = np.random.standard_t(df=10, size=60) * 10 + 35
edades = edades.astype(int)
cargos = ["Analista", "Gerente", "Asistente", "Desarrollador"]

personal_df = pd.DataFrame({
    "Nombre": np.random.choice(nombres, size=60),
    "Edad": edades,
    "Cargo": np.random.choice(cargos, size=60)
})

# c) Crear DataFrame de horarios
fechas = pd.date_range(start="2024-01-01", end="2024-12-31", periods=60)

# Generar horas de entrada y salida aleatorias
hora_entrada = [datetime.strptime(np.random.choice(["08:00", "09:00", "10:00"]), "%H:%M") for _ in range(60)]
hora_salida = [entrada + timedelta(hours=int(np.random.standard_t(df=10) * 2)) for entrada in hora_entrada]

horarios_df = pd.DataFrame({
    "Hora_Entrada": hora_entrada,
    "Hora_Salida": hora_salida
}, index=fechas)

# Imprimir los DataFrames
print("DataFrame de tareas:")
print(tareas_df.head())

print("\nDataFrame de personal:")
print(personal_df.head())

print("\nDataFrame de horarios:")
print(horarios_df.head())