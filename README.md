# Vetsoft

Aplicación web para veterinarias utilizada en la cursada 2024 de Ingeniería y Calidad de Software. UTN-FRLP

## Dependencias

- python 3
- Django
- sqlite
- playwright
- ruff

## Instalar dependencias

`pip install -r requirements.txt`

## Iniciar la Base de Datos

`python manage.py migrate`

## Iniciar app

`python manage.py runserver`

## Integrantes:

* Milagros Soberon
* Nuria Robledo  
* Leo Sebastián Gonzáles Tello
* Juan Ignacio Frangolini  

## Levantar Docker:

`docker-compose up --build`

## Commits
- Convencional commits => feat:..., fix:...
- No mencionar el nombre del archivo en el mensaje del commit


## PR
- Seleccionar nuestro repositorio (no el de la catedra)
- Seleccionar rama develop
- Seleccionar Reviewer: Juan Ignacio => Milagros => Sebastián => Nuria => Juan Ignacio
- Seleccionar Assignees (el que solicita el PR)
- Una rama por cada ticket

## Convención PR
    # Descripción del PR

    breve descripción

    ## Lista de cambios

    - Realicé ...
    - Agregué ...
    - Modifiqué ...


### Acceder a la aplicación
[Link de la aplicación](http://localhost:8000/)