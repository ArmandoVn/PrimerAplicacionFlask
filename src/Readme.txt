INSTALACION DE FLASK

    pip install flask



CREACION DE UN NUEVO ENTORNO VIRTUAL DE PYTHON

Como este proyecto se subira a un servidor remoto necesitamos crear un entorno virtual propio
para este proyecto, con el cual nos aseguraremos de que nuestra aplicacion si corra en el
servidor.

Para crear un entorno virtual con Python debemos hacer lo siguiente:
    - Debemos instalar el modulo de venv para Python con el comando:
                " pip install virtualenv "
    
    - Para crear el entorno virtual, nos posicionaremos dentro de nuestro proyecto
      y teclearemos el siguiente comando:
                " python -m venv nombre_carpeta_entorno "
    El comando anterior creara un nuevo entorno virtual dentro de nuestro proyecto y una
    vez lo hayamos realizado debemos instalar flask nuevamente, pero esta vez dentro de
    nuestro proyecto.

    - Para hacer uso de Python y los comandos del entorno virtual en general debemos ingresar
    a la carpeta del entorno virtual/Scripts, donde encontraremos todos los Script generados
    por el modulo venv

    - Ya situados dentro de la carpeta Scripts, comprobamos que Python y pip funcionen correctamente
    con un python --version y pip --version

    - Como flask no viene instalado por defecto con Python debemos instalarlo nuevamente en
    nuestro proyecto con:
                " pip install flask "
    
    - Una vez instalado flask comprobamos que nuestro proyecto funcione correctamente con el entorno
    virtual creado:
                " python nombre_archivo_carga.py "


SUBIR EL PROYECTO A HEROKU

Esto proyecto se subio a un servidor de la plataforma Heroku, para obtener una guia completa
de comandos e instalacion del cliente Heroko ir a su pagina oficial.

Heroku necesita el complento gunicorn de Python para correr el servidor http:
        pip install gunicorn

Para subir nuestro nuevo proyecto a Heroku necesitamos los siguientes archivos con los siguientes
datos:

    - Procfile:
        Encargado de iniciar el proyecto
        tipoProyecto: nombreModulo archivoAEjecutar: variableAEjecutar, lo colocamos de la siguiente manera:
        web: gunicorn index:nombre_variable_flask
    - requirements.txt:
        Lista los modulos necesarios para nuestra aplicacion, para saber que modulos requiero hacemos uso
        del comando:
            pip freeze > rutaArchivoRequirements/requirements.txt
    - runtime.txt:
        Le indica a Heroku la version de Python que usa nuestro proyecto, se coloca (ejem.):
            python-3.7.1

Una vez tenemos todo lo anterior nuestro proyecto ya esta listo para subirse al servidor Heroku, debemos
seguir los siguientes pasos:

    - Iniciamos un repo de git dentro de la carpeta src de nuestro proyecto
    - Agregamos los archivos al stage y hacemos el commit
    - Creamos una aplicacion de Heroku:
        heroku create
    - heroku git:remote nombreAplicacionHeroku
        Debe mostrar la url del repo remoto en heroku
    - Hacemos un push al servidor:
        git push heroku master