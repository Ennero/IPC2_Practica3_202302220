# Ventas por departamento desde XML con Flask y Django

API Flask para procesar archivos XML y generar un resumen de ventas por departamento, con gráficas Plotly y un frontend Django para cargar y consultar los resultados.

## Requisitos

Python 3.12 o superior y requirements.txt. Backend y frontend se ejecutan como dos procesos; Django usa SQLite local.

## Ejecución

Los comandos parten de la raíz del repositorio, salvo donde se indica otra terminal.

```bash
python -m pip install -r requirements.txt
python backend.py

# Otra terminal, desde la raíz:
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

## Recorrido de demostración

Abrir http://127.0.0.1:8000, cargar uno de los XML de archivosPrueba/ y consultar el resumen o la gráfica. El frontend llama a Flask en http://127.0.0.1:5000.

## Organización

Carpetas de la entrega: [`MiApp/`](MiApp/), [`archivosPrueba/`](archivosPrueba/), [`frontend/`](frontend/).

## Alcance y límites

Los archivos salida.xml se generan en la carpeta de ejecución. SQLite se crea con migrate y no se distribuye una copia personal. Los datos y gráficos dependen del último XML cargado.

## Contexto y licencia

Trabajo académico o de aprendizaje conservado en el portafolio de [Enner Mendizabal](https://github.com/Ennero). Los créditos de los trabajos en grupo se conservan en sus entregas y manuales.

Consultar [LICENSE](LICENSE) para la licencia de la raíz. Las dependencias y los componentes con avisos o licencias propios conservan sus condiciones.
