import psycopg2

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname="aviacion_db",
    user="postgres",
    password="Copa_pw",
    host="172.18.0.2",
    port="5432"
)

# Creación del cursor
cursor = conn.cursor()

# Query para crear la tabla Departures
create_departures_table_query = """
CREATE TABLE IF NOT EXISTS Departures (
    id SERIAL PRIMARY KEY,
    airport VARCHAR(100),
    timezone VARCHAR(100),
    iata VARCHAR(10),
    icao VARCHAR(10),
    terminal VARCHAR(10),
    gate VARCHAR(10),
    delay INTEGER,
    scheduled TIMESTAMP,
    estimated TIMESTAMP,
    actual TIMESTAMP,
    estimated_runway TIMESTAMP,
    actual_runway TIMESTAMP
);
"""

# Ejecutar el query para crear la tabla Departures
cursor.execute(create_departures_table_query)

# Confirmar la transacción y cerrar la conexión
conn.commit()
conn.close()

print("Tabla 'Departures' creada exitosamente en la base de datos.")