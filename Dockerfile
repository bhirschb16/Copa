######## CONTENEDOR POSTGRES ########

# Usa la imagen oficial de PostgreSQL como base
FROM postgres

# Establece una variable de entorno para la contraseña de PostgreSQL
ENV POSTGRES_PASSWORD Copa_pw

# Expone el puerto 5432 para permitir conexiones a la base de datos
EXPOSE 5432