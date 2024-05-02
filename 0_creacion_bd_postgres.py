import psycopg2

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="Copa_pw",
    host="172.18.0.2",
    port="5432"
)

conn.autocommit = True

cursor = conn.cursor()


sql = "CREATE DATABASE aviacion_db";

## executing above query
cursor.execute(sql)
print("Base de Datos aviacion_db creada exisotamente!!");
 
# Closing the connection
conn.close()