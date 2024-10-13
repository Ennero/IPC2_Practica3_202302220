from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render




# Create your views here.
def carga(request): 
    if request.method == 'POST':
        archivo=request.FILES['archivo']
    


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
                <input type="file" name="archivo" accept=".xml">
                <button type="submit">Subir</button>
            </form>
            <br>
        </div>
    </div>
</body>

</html>
"""
    return HttpResponse(documento) #Aqui se retorna el documento html



