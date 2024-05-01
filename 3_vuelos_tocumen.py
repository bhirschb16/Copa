import psycopg2
import polars as pl
import pandas as pd
from datetime import datetime

try:
    # Conexión a la base de datos
    conn = psycopg2.connect(
        dbname="aviacion_db",
        user="postgres",
        password="Copa_pw",
        host="172.18.0.2",
        port="5432"
    )

    # Crear un cursor
    cursor = conn.cursor()

    # Ejecutar la consulta SQL para seleccionar todos los registros de la tabla Departures
    cursor.execute("SELECT * FROM Departures")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
    
    #### Ejecución en SQL ####
    conteo_sql_query = "SELECT COUNT(*) FROM Departures WHERE SUBSTRING(CAST(estimated as varchar),1,10) = '2024-03-24'"
    conteo = cursor.execute(conteo_sql_query)
    print("En SQL la cantidad de vuelos que salieron de Tocumen par el día especifico es: ", cursor.fetchall())
    
    
    cursor.close()
    conn.close()
    
    
    #### Ejecución en Python ####
    ## Crear un DataFrame de Polars para mejor manipulación de datos y procesamiento en paralelo.     
    departures = pl.from_pandas(df)

    can_vueltos_dep_fec_string = departures.with_columns(
        pl.col("estimated")
        .dt.strftime("%Y-%m-%d")
        .alias("fecha_vuelo")
    ).group_by("airport") \
        .agg(
            cant_vuelos = pl.col("airport").filter(pl.col("fecha_vuelo") == '2024-03-24').count(),
        )
    
    print("En Python la cantidad de vuelos que salieron de Tocumen par el día especifico es: ")
    print(can_vueltos_dep_fec_string)
    
    
except psycopg2.Error as e:
    print("Error al conectar a PostgreSQL:", e)