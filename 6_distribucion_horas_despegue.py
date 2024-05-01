import psycopg2
import polars as pl
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


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
    cursor.execute("SELECT * FROM Departures WHERE actual between '2024-03-24' and '2024-03-29'")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
    
    cursor.close()
    conn.close()
    
    #### Ejecución en Python ####  
    departures_hours = pl.from_pandas(df)
    departures_hours = departures_hours.with_columns(
        pl.col("actual")
        .dt.hour()
        .alias("hora_despegue")
    )
    
    # Ajustar una regresión polinómica a los datos
    X = departures_hours.select(pl.col("hora_despegue")).to_numpy().reshape(-1, 1)
    y = np.arange(len(departures_hours)) 
    model = LinearRegression()
    model.fit(X, y)
    
    # Generar puntos para la curva ajustada
    x_values = np.linspace(0, 23, 100)
    y_values = model.predict(x_values.reshape(-1, 1))
    
    plt.scatter(departures_hours['hora_despegue'], y, label='Datos de despegue', color='blue')
    plt.plot(x_values, y_values, label='Curva ajustada', color='red')
    plt.xlabel('Hora de despegue')
    plt.ylabel('Número de vuelo')
    plt.title('Ajuste de curva para la hora de despegue de vuelos')
    plt.legend()
    plt.grid(True)
    plt.savefig('/Copa_Test/curva_ajustada_despegue.png')
    plt.show()
    
    
    
except psycopg2.Error as e:
    print("Error al conectar a PostgreSQL:", e)