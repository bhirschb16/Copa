import psycopg2
import requests

# Definición de la clase Departures
class Departures:
    def __init__(self, airport, timezone, iata, icao, terminal, gate, delay, scheduled, estimated, actual, estimated_runway, actual_runway):
        self.airport = airport
        self.timezone = timezone
        self.iata = iata
        self.icao = icao
        self.terminal = terminal
        self.gate = gate
        self.delay = delay
        self.scheduled = scheduled
        self.estimated = estimated
        self.actual = actual
        self.estimated_runway = estimated_runway
        self.actual_runway = actual_runway

# URL base de la API
base_url = "https://api.aviationstack.com/v1/flights"

# Parámetros de la solicitud inicial
params = {
    'access_key': '5bd034884c1c1a0fc35ddd1fc0cd7aab',  
    'dep_iata': 'PTY',
    'limit': 100,  
    'offset': 0    
}

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

# Función para insertar datos de vuelo en la tabla 'vuelos'
def insertar_departures(departure):
    insert_query = """
    INSERT INTO Departures (airport, timezone, iata, icao, terminal, gate, delay, scheduled, estimated, actual, estimated_runway, actual_runway)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (
        departure.airport,
        departure.timezone,
        departure.iata,
        departure.icao,
        departure.terminal,
        departure.gate,
        departure.delay,
        departure.scheduled,
        departure.estimated,
        departure.actual,
        departure.estimated_runway,
        departure.actual_runway
    ))

# Función para hacer una solicitud a la API y obtener datos paginados
def obtener_datos_paginados(url, params, num_paginas):
    datos_totales = []
    for _ in range(num_paginas):
        response = requests.get(url, params=params, verify=False)
        data = response.json()
        datos_pagina = data['data']
        datos_totales.extend(datos_pagina)
        pagination = data['pagination']
        total_registros = pagination['total']
        offset_actual = pagination['offset']
        if offset_actual + len(datos_pagina) >= total_registros:
            break
        params['offset'] += len(datos_pagina)
    return datos_totales

# Obtener todos los datos paginados
num_paginas_deseadas = 390
datos_totales = obtener_datos_paginados(base_url, params, num_paginas_deseadas)

# Parsear los datos y estructurarlos como instancias de Departures
for departure_data in datos_totales:
    departure_instance = Departures(
        airport=departure_data['departure']['airport'],
        timezone=departure_data['departure']['timezone'],
        iata=departure_data['departure']['iata'],
        icao=departure_data['departure']['icao'],
        terminal=departure_data['departure'].get('terminal'),  
        gate=departure_data['departure'].get('gate'),          
        delay=departure_data['departure'].get('delay'),        
        scheduled=departure_data['departure']['scheduled'],
        estimated=departure_data['departure']['estimated'],
        actual=departure_data['departure'].get('actual'),      
        estimated_runway=departure_data['departure'].get('estimated_runway'),  
        actual_runway=departure_data['departure'].get('actual_runway')         
    )
    
    # Insertar los datos de Departures en la base de datos
    insertar_departures(departure_instance)

# Confirmar la transacción y cerrar la conexión
conn.commit()
conn.close()

print("Datos insertados exitosamente en la tabla 'departures' de la base de datos.")