import requests
import plotly.graph_objs as go
from django.shortcuts import render, redirect


def subir_xml(request):
    if request.method== 'POST':
        archivo = request.FILES['archivo']

        #Aquí guardo el archivo xml temporalmente
        with open('archivo.xml', 'wb+') as f:
            for chunk in archivo.chunks():
                f.write(chunk)

        return redirect('ver_xml')
    return render(request, 'subir.html')

def ver_xml(request):
    
    with open('archivo.xml', 'r') as archivo: #Aquí se lee el archivo xml
        contenido = archivo.read()

    return render(request, 'simple_app/ver_xml.html', {'xml_contenido': contenido}) #Aquí se muestra el contenido del archivo xml



def ver_grafica(request):
    # Leer y parsear el archivo XML
    tree = ET.parse('archivo.xml')
    root = tree.getroot()

    # Obtener los datos del XML (ajustar según la estructura del archivo)
    datos = [float(item.find('valor').text) for item in root.findall('.//item')]

    # Crear la gráfica
    grafica = go.Figure(data=[go.Scatter(x=list(range(len(datos))), y=datos, mode='lines+markers')])
    grafica_html = grafica.to_html(full_html=False)

    # Mostrar la gráfica en el template
    return render(request, 'simple_app/grafica.html', {'grafica_html': grafica_html})



    