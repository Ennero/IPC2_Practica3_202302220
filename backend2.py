import xml.etree.ElementTree as ET
import plotly.graph_objs as go
import poo
paisVnumero=[]

def indent(elem, level=0, hor='\t', ver='\n'): # Función para indentar el archivo (solo lo copié y lo pegué xd)
    i = ver + level * hor
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + hor
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1, hor, ver)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def crearSalida(contenido):
    global paisVnumero
    departamentos = []

    #Limpio la lista
    paisVnumero.clear()

    posiblesDepartamentos = [
    "AltaVerapaz",
    "BajaVerapaz",
    "Chimaltenango",
    "Chiquimula",
    "Guatemala",
    "ElProgreso",
    "Escuintla",
    "Huehuetenango",
    "Izabal",
    "Jalapa",
    "Jutiapa",
    "Petén",
    "Quetzaltenango",
    "Quiché",
    "Retalhuleu",
    "Sacatepéquez",
    "SanMarcos",
    "SantaRosa",
    "Sololá",
    "Suchitepéquez",
    "Totonicapán",
    "Zacapa"
]

    try:
        arbol = ET.ElementTree(ET.fromstring(contenido))  # Se lee el contenido XML desde una cadena
        #arbol = ET.parse(contenido) #Se lee el archivo XML
        ramas = arbol.getroot() #Se obtiene la raíz del archivo XML
        for i in ramas.iter("ListadoVentas"):
            for j in i.iter("Venta"):

                #Quito el espacio :)
                departamento=(j.get("departamento")).replace(" ", "")
                departamentos.append(departamento)
                print(departamento)
        
        for k in departamentos:
            raiz=ET.Element("Resultados")
            rama=ET.SubElement(raiz,"Departamentos")
            for departamento in posiblesDepartamentos:
                n = 0
                for venta in departamentos:
                    if departamento == venta.replace(" ", ""):
                        n += 1
                        
                if n > 0:
                    ramita = ET.SubElement(rama, departamento)
                    ramitita = ET.SubElement(ramita, "cantidadVentas")
                    ramitita.text = str(n)

        salida=ET.ElementTree(raiz)
        ET.dump(raiz) #La verdad no entiendo nada de esta parte xd
        indent(raiz)
        salida.write("salida.xml",encoding="utf-8",xml_declaration=True)

    except Exception as e:
        print(e)

    
def grafico():
    global paisVnumero

    arbol=ET.parse("salida.xml")
    raiz=arbol.getroot()
    for departamento in raiz.iter("Departamentos"):
        for i in departamento:
            for j in i.iter("cantidadVentas"):
                paula=poo.departamento(i.tag, int(j.text))
                paisVnumero.append(paula)

    #Creación de gráfica de barras


    fig = go.Figure([go.Bar(x=[i.nombre for i in paisVnumero], y=[i.ventas for i in paisVnumero])])

    
    fig.update_layout(title_text='Ventas por departamento', xaxis_title='Departamento', yaxis_title='Ventas')

    grafica=fig.to_html(full_html=False)
    return grafica

