## Creacion del Network para el proyecto 
$ docker network create copa_test_network



######## CONTENEDOR POSTGRES ########
## Improtamos la ultima versión de Postgres en Docker 
$ docker pull postgres

## Creación del Contenedor con Postgres
$ docker run --name Copa_Test_DB --network copa_test_network -e POSTGRES_PASSWORD=Copa_pw -d -p 5432:5432 postgres

## Ingresar al contenedor de Postgres
$ docker exec -it Copa_Test_DB bash


######## CONTENEDOR UBUNTU ########
## Improtamos la ultima versión de Ubuntu en Docker 
$ docker pull ubuntu
## Creación del Contenedor con Ubuntu 
$ docker run --name Copa_Test_Ubuntu --network copa_test_network -it ubuntu /bin/bash
##Ingresar el contenedor del Ubuntu
$ docker exec -it Copa_Test_Ubuntu bash
## Instalacion de Updates
$ apt update
## Instalacion de GIT
$ apt install git
## Instalacion de Python
$ apt install python3
## America
$ 2
## Panama
$ 114 
## Instalacion de Python3-pip
$ apt install python3.12-venv
## Creacion de la carpeta de trabajo
$ mkdir Copa_Test
## Creación del Entorno de Trabajo
$ python3 -m venv Copa_Venv
## Activación del Entorno de Trabajo
$ source Copa_Venv/bin/activate
## Instalación de Librerias
$ pip install psycopg2-binary





#################
## Creacion del Network para el proyecto 
$ docker network create copa_test_network

##
docker build -t postgres -f Dockerfile .

##
docker build -t ubuntu -f Dockerfile-app .

##
docker run --name Copa_Test_Ubuntu --network copa_test_network -it ubuntu /bin/bash

##
docker run --name Copa_Test_DB --network copa_test_network -e POSTGRES_PASSWORD=Copa_pw -d -p 5432:5432 postgres

