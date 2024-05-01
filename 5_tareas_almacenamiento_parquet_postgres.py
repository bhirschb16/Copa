import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Parámetros de conexión a la base de datos PostgreSQL
db_user = 'postgres'
db_password = 'Copa_pw'
db_host = '172.18.0.2'
db_port = '5432'
db_name = 'aviacion_db'

# Crear la cadena de conexión
conn_str = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

## Este parametro es dinamico. 
num_tareas = 5
num_trabajadores = 9

## Crear DataFrame de tareas
tareas_df = pd.DataFrame({"Tarea": [f"Tarea_{i+1}" for i in range(num_tareas)]})

## Crear DataFrame de trabajadores
trabajadores_df = pd.DataFrame({"Trabajador": [f"Trabajador_{i+1}" for i in range(num_trabajadores)]})

## Asegurarse de que cada trabajador esté asignado al menos dos veces
trabajadores_repetidos = np.tile(trabajadores_df["Trabajador"], 2)

## Asignar a cada tarea tres trabajadores aleatorios de la lista generada
asignaciones = np.random.choice(trabajadores_repetidos, size=(num_tareas, 3), replace=False)

## Crear DataFrame de asignaciones
asignaciones_df = pd.DataFrame(asignaciones, columns=["Trabajador_1", "Trabajador_2", "Trabajador_3"])

## Combinar los DataFrames de tareas y asignaciones
tareas_asignadas_df = pd.concat([tareas_df, asignaciones_df], axis=1)

### Gaurdar el DataFrame en formato Parquet ####
tareas_asignadas_df.to_parquet("/Copa_Test/tareas_asignadas.parquet")
print("DataFrame guardado en local en formato parquet con éxito.")

#### Gaurdar los datos en PostgreSQL ####
# Crear un motor SQLAlchemy
engine = create_engine(conn_str)
tareas_asignadas_df.to_sql('TareasAsignadas', engine, if_exists='replace', index=False)
print("DataFrame guardado en PostgreSQL con éxito.")