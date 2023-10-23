# Plataforma web para jugar online.
# ***GamesX***
## Integrantes del equipo:
* **Luis Eduardo Poot Poot**

## Descripción
Esta es una plataforma web para jugar de manera online, los usuarios pueden acceder a la liga para registrarse, posteriormente se inicia sesión con las credenciales creadas para poder visualizar los distintos juegos disponibles. El usuario podrá jugar diversos juegos tales como las torres de hanoi y tictactoe, además existen tutoriales de cómo jugar.
Este proyecto tiene una arquitectura que permite una rápida escalabilidad.

## Juegos disponibles
* **Tic Tac Toe (Gato)**
* **Torres de Hanoi**
## Arquitectura
El sistema utiliza la arquitectura de servicios web REST, la cual contiene 4 nodos:
* Usuario
* Plataforma
* BD
* Servidor de juegos

## Herramientas y tecnologías usadas
1. Python
2. HTML
3. JS
4. CSS
5. Django
6. MySQL
7. Azure

## Como trabajar con el proyecto
1. Clonar el repositorio de GitHub:

    `git clone <URL_del_repositorio`
    
2. Crear un entorno virtual de Python

    `python3 -m venv entornoVirtual`
    
3. Activa el entorno virtual
    
    `entornoVirtual\Scripts\activate`
    
4. Instalar las dependencias
    
    `pip install -r requirements.txt`
    
5. Crea tu propia base de datos local:
    En el archivo settings.py cambia la variable DATABASES

    `
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
`

6. Realiza las migraciones a la BD
    
    `python manage.py makemigrations`
    
    `python manage.py migrate`
    
7. Ejecuta el servidor
    
    `python manage.py runserver`
    
8. Abre en el navegador
    
    `localhost:8000`

## Acceder a la plataforma
* La plataforma se encuentra disponible para uso en el siguiente enlace: [https://gamesx.azurewebsites.net/](https://gamesx.azurewebsites.net/)
* Registrate y juega
