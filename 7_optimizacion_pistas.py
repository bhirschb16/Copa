from datetime import datetime, timedelta
import pandas as pd
import pulp
import psycopg2

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
    cursor.execute("SELECT * FROM Departures WHERE substring(cast(actual as varchar), 1, 10) = '2024-03-24'")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
    
    cursor.close()
    conn.close()

    # Convertir las columnas de tiempo programado y estimado en objetos datetime
    df['scheduled'] = pd.to_datetime(df['scheduled'])
    df['estimated'] = pd.to_datetime(df['estimated'])

    # Calcular la diferencia de tiempo entre el tiempo programado y estimado
    df['Time_Difference'] = (df['estimated'] - df['scheduled']).dt.total_seconds() / 60

    # Ordenar los vuelos por hora de despegue programada
    df_sorted = df.sort_values(by='scheduled')

    # Obtener la lista de nombres de los vuelos ordenados
    flight_names = df_sorted.index.tolist()

    # Crear el problema de optimización
    prob = pulp.LpProblem("Optimización de asignación de pistas de despegue", pulp.LpMinimize)

    # Variables de decisión
    pista_A = pulp.LpVariable.dicts("Pista_A", flight_names, cat='Binary')
    pista_B = pulp.LpVariable.dicts("Pista_B", flight_names, cat='Binary')

    # Función objetivo: minimizar la suma de diferencias de tiempo entre despegues
    prob += pulp.lpSum(df_sorted.loc[flight_name, 'Time_Difference'] * (pista_A[flight_name] + pista_B[flight_name])
                    for flight_name in flight_names)

    # Restricciones: cada vuelo debe ser asignado a una pista exactamente una vez
    for flight_name in flight_names:
        prob += pista_A[flight_name] + pista_B[flight_name] == 1

    # Resolver el problema de optimización
    prob.solve()

    # Mostrar resultados
    for flight_name in flight_names:
        if pulp.value(pista_A[flight_name]) == 1:
            print(f"Vuelo {flight_name} asignado a la Pista A")
        else:
            print(f"Vuelo {flight_name} asignado a la Pista B")

    # Mostrar la suma total de diferencias de tiempo entre despegues
    print("Total de tiempo entre despegues optimizado:", pulp.value(prob.objective))
    
    
except psycopg2.Error as e:
    print("Error al conectar a PostgreSQL:", e)