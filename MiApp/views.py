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

        with open('archivo.xml', 'w', encoding='utf-8') as destination: #Se abre el archivo
            for chunk in archivo.chunks(): #Se recorre el archivo
                destination.write(chunk.decode('utf-8')) #Se escribe el archivo

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

    <div class="card border warning-danger-subtle" style="width: 30rem;">
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
                <input type="file" name="archivo" accept=".xml" class="form-control" id="inputGroupFile02" aria-describedby="inputGroupFileAddon03" aria-label="Upload">
                <button class="btn btn-outline-secondary" type="submit" id="inputGroupFileAddon03">Subir</button>
                </div>

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

    with open('archivo.xml', 'r', encoding='utf-8') as file: #Se abre el archivo en modo lectura
        contenido=file.read()
    #print(contenido)

    documento=f"""
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

    <div class="card border warning-danger-subtle" style="width: 30rem;">
        <div class="card-body">
            <div class="row">
                <div class="col-md-12 mx-auto">
                    <h5 align="center" style="color: grey;">Revisión de Datos procesados</h5> 
                </div>
            </div>
        </div>
        <div class="card-body" align="center"   >
        
        <pre>{contenido}</pre> <!-- Aquí se muestra el contenido del archivo -->

                <form method="POST" enctype="multipart/form-data">
                
                <button class="btn btn-danger" type="submit" id="inputGroupFileAddon03">Regresar</button>
                <button class="btn btn-success" type="submit" id="inputGroupFileAddon03">Graficar</button>

            </form>
            <br>
        </div>
    </div>
</body>

</html>



"""
    
    return HttpResponse("Se pudo!!!!")
    #return HttpResponse(documento) #Aqui se retorna el documento html




# 3. Mostrar gráfica a partir del XML
@csrf_exempt
def grafico(request):
    # Leer y enviar el archivo XML a Flask
    with open('archivo.xml', 'rb') as archivo:
        response = requests.post('http://127.0.0.1:5000/subir-xml', files={'archivo': archivo})

    if response.status_code == 200:
        datos = response.json()

        # Crear gráfica con los datos devueltos por Flask
        grafica = go.Figure(data=[go.Scatter(x=list(range(len(datos))), y=datos, mode='lines+markers')])
        grafica_html = grafica.to_html(full_html=False)

        return render(request, 'simple_app/grafica.html', {'grafica_html': grafica_html})
    else:
        return render(request, 'simple_app/error.html', {'error': response.json()})