import html
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
import plotly.graph_objs as go
from django.views.decorators.csrf import csrf_exempt
import requests



# Create your views here.
@csrf_exempt
def carga(request): 
    if request.method == 'POST': #Si se envia un archivo
        archivo=request.FILES['archivo'] #Se obtiene el archivo

        with open('archivo.xml', 'w', encoding='utf-8') as destination: #Se crea un archivo en modo escritura
            for chunk in archivo.chunks(): #Se recorre el archivo leido
                destination.write(chunk.decode('utf-8')) #Se escribe el archivo leido en archivo.xml

        with open('archivo.xml', 'r', encoding='utf-8') as file: #Se abre el archivo en modo lectura
            contenido=file.read()
        
        #print(contenido)
        response = requests.post('http://127.0.0.1:5000/carga', files={'archivo': contenido})


        if response.status_code == 200:
            datos = response.json()
        else:
            return HttpResponse("Error :)")
        
        return redirect("ver") #Se redirige a la vista visualizar

    documento="""
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Super carros GT</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</head>

<body class="bg-warning-subtle position-absolute top-50 start-50 translate-middle">

    <div class="card border warning-danger-subtle" style="width: 40rem;">
        <img src="https://www.pnguniverse.com/wp-content/uploads/2020/10/Rayo-McQueen.png" class="card-img-top"
            alt="El Rayo">
        <div class="card-body">
            <div class="row">
                <div class="col-md-12 mx-auto">
                    <h1 class="card-title " align="center">Super Autos GT</h1>
                    <h5 align="center" style="color: grey;">Carga de Archivos de Registro</h5> 
                </div>
            </div>
        </div>
        <div class="card-body" align="center"   >
            <form method="POST" enctype="multipart/form-data">

                <div class="input-group mb-3">
                <input type="file" name="archivo" accept=".xml" class="form-control" id="inputGroupFile02" aria-describedby="inputGroupFileAddon03" aria-label="Upload" required>
                <button class="btn btn-outline-danger" type="submit" id="inputGroupFileAddon03">Subir</button>
                </div>
                <br>
                <a href="/info/" class="btn btn-outline-secondary" role="button">Mostrar Datos del Estudiante</a>
            </form>
            <br>
        </div>
    </div>
</body>

</html>
"""
    return HttpResponse(documento) #Aqui se retorna el documento html

@csrf_exempt
def ver(request):

    with open('salida.xml', 'r', encoding='utf-8') as file: #Se abre el archivo en modo lectura
        contenido=file.read()

    contenidoArreglado=html.escape(contenido) #Se escapa el contenido para evitar inyección de código
    print(contenidoArreglado)

    documento=f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Super carros GT</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</head>

<body class="bg-warning-subtle position-absolute top-50 start-50 translate-middle">

    <div class="card border warning-danger-subtle" style="width: 40rem;">

        <div class="card-body" align="center">
        <div class="col-md-12 mx-auto">
                    <h3 align="center" style="color: grey;">Revisión de Datos procesados</h3> 
                </div>
            <div class="overflow-auto border p-3" style="max-height: 400px; background-color: #f8f9fa; width: 35rem;"> <!-- Scrollable area -->
                <pre>{contenidoArreglado}</pre> <!-- Aquí se muestra el contenido del archivo -->
            </div>
            <br>
"""+"""
            <a href="/" class="btn btn-danger" role="button">Regresar</a>
            <a href="/grafico/" class="btn btn-success" role="button">Graficar</a>
        </div>
    </div>
</body>

</html>
"""
    
    return HttpResponse(documento) #Aqui se retorna el documento html




#Mostrar gráfica a partir del XML
@csrf_exempt
def grafico(request):
    # Leer y enviar el archivo XML a Flask
    with open('salida.xml', 'r', encoding='utf-8') as salida:
        response = requests.post('http://127.0.0.1:5000/grafica', files={'salida': salida})

    if response.status_code == 200:
        datos = response.text #Obtengo los datos que me devolvió el backend
        print(datos)

        documento=f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Super carros GT</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</head>

<body class="bg-warning-subtle d-flex position-absolute top-50 start-50 translate-middle">

    <div class="card border warning-danger-subtle" style="width: 85rem; height: 40rem;">
        <div class="card-body" align="center">
                    <h3 align="center" style="color: grey;">Grafica de los datos procesados</h3> 
            <div class="overflow-auto border p-3" style="max-height: 35rem; background-color: #f8f9fa; width: 80rem;"> <!-- Scrollable area -->
                {datos} <!-- Aquí se muestra el contenido del archivo -->
            </div>
            
"""+""" <br>
            <a href="/ver/" class="btn btn-danger" role="button">Regresar</a>
            <br>
        </div>
    </div>
</body>

</html>
"""

        return HttpResponse(documento) #Aqui se retorna el documento html
    else:
        return HttpResponse("Error :)")



#Esto es para mostar la información del estudiante
@csrf_exempt
def info(request): 
    if request.method == 'POST': #Si se envia un archivo
        archivo=request.FILES['archivo'] #Se obtiene el archivo

        with open('archivo.xml', 'w', encoding='utf-8') as destination: #Se crea un archivo en modo escritura
            for chunk in archivo.chunks(): #Se recorre el archivo leido
                destination.write(chunk.decode('utf-8')) #Se escribe el archivo leido en archivo.xml

        with open('archivo.xml', 'r', encoding='utf-8') as file: #Se abre el archivo en modo lectura
            contenido=file.read()
        
        #print(contenido)
        response = requests.post('http://127.0.0.1:5000/carga', files={'archivo': contenido})

        if response.status_code == 200:
            datos = response.json()
        else:
            return HttpResponse("Error :)")
        
        return redirect("ver") #Se redirige a la vista visualizar

    documento="""
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Super carros GT | login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</head>

<body class="bg-warning-subtle position-absolute top-50 start-50 translate-middle">

    <div class="card" style="width: 35rem;">
        <h1 align="center">Información del Estudiante</h1>
        <div class="card-body " >
            <ul>
                <li>
                    <p><b>Nombre: </b>Enner Esaí Mendizabal Castro</p>
                </li>
                <li>
                    <p><b>Carnet:</b> 202302220</p>
                </li>
            </ul>
            <div align="center">
                <a href="/" class="btn btn-danger">Regresar</a>
            </div>
        </div>
    </div>
</body>

</html>
"""
    return HttpResponse(documento) #Aqui se retorna el documento html