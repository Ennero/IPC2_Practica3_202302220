import xml.etree.ElementTree as ET
#Función para crear la salida con listas

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

    pXn = []

    posiblesDepartamentos = [
    "Alta Verapaz",
    "Baja Verapaz",
    "Chimaltenango",
    "Chiquimula",
    "Guatemala",
    "El Progreso",
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
    "San Marcos",
    "Santa Rosa",
    "Sololá",
    "Suchitepéquez",
    "Totonicapán",
    "Zacapa"
]


    contenido='''<?xml version="1.0" encoding="UTF-8"?>
<Resumen>
    <ListadoVentas>
        <Venta departamento="Guatemala">
            <Fecha>01/01/2024</Fecha>
        </Venta>
        <Venta departamento="Alta Verapaz">
            <Fecha>02/01/2024</Fecha>
        </Venta>
        <Venta departamento="Baja Verapaz">
            <Fecha>03/01/2024</Fecha>
        </Venta>
        <Venta departamento="Chimaltenango">
            <Fecha>04/01/2024</Fecha>
        </Venta>
        <Venta departamento="Chiquimula">
            <Fecha>05/01/2024</Fecha>
        </Venta>
        <Venta departamento="El Progreso">
            <Fecha>06/01/2024</Fecha>
        </Venta>
        <Venta departamento="Escuintla">
            <Fecha>07/01/2024</Fecha>
        </Venta>
        <Venta departamento="Huehuetenango">
            <Fecha>08/01/2024</Fecha>
        </Venta>
        <Venta departamento="Izabal">
            <Fecha>09/01/2024</Fecha>
        </Venta>
        <Venta departamento="Jalapa">
            <Fecha>10/01/2024</Fecha>
        </Venta>
        <Venta departamento="Jutiapa">
            <Fecha>11/01/2024</Fecha>
        </Venta>
        <Venta departamento="Petén">
            <Fecha>12/01/2024</Fecha>
        </Venta>
        <Venta departamento="Quetzaltenango">
            <Fecha>13/01/2024</Fecha>
        </Venta>
        <Venta departamento="Quiché">
            <Fecha>14/01/2024</Fecha>
        </Venta>
        <Venta departamento="Retalhuleu">
            <Fecha>15/01/2024</Fecha>
        </Venta>
        <Venta departamento="Sacatepéquez">
            <Fecha>16/01/2024</Fecha>
        </Venta>
        <Venta departamento="San Marcos">
            <Fecha>17/01/2024</Fecha>
        </Venta>
        <Venta departamento="Santa Rosa">
            <Fecha>18/01/2024</Fecha>
        </Venta>
        <Venta departamento="Sololá">
            <Fecha>19/01/2024</Fecha>
        </Venta>
        <Venta departamento="Suchitepéquez">
            <Fecha>20/01/2024</Fecha>
        </Venta>
        <Venta departamento="Totonicapán">
            <Fecha>21/01/2024</Fecha>
        </Venta>
        <Venta departamento="Zacapa">
            <Fecha>22/01/2024</Fecha>
        </Venta>
        <Venta departamento="Guatemala">
            <Fecha>23/01/2024</Fecha>
        </Venta>
        <Venta departamento="Alta Verapaz">
            <Fecha>24/01/2024</Fecha>
        </Venta>
        <Venta departamento="Baja Verapaz">
            <Fecha>25/01/2024</Fecha>
        </Venta>
        <Venta departamento="Chimaltenango">
            <Fecha>26/01/2024</Fecha>
        </Venta>
        <Venta departamento="Chiquimula">
            <Fecha>27/01/2024</Fecha>
        </Venta>
        <Venta departamento="El Progreso">
            <Fecha>28/01/2024</Fecha>
        </Venta>
        <Venta departamento="Escuintla">
            <Fecha>29/01/2024</Fecha>
        </Venta>
        <Venta departamento="Huehuetenango">
            <Fecha>30/01/2024</Fecha>
        </Venta>
        <Venta departamento="Izabal">
            <Fecha>31/01/2024</Fecha>
        </Venta>
        <Venta departamento="Jalapa">
            <Fecha>01/02/2024</Fecha>
        </Venta>
        <Venta departamento="Jutiapa">
            <Fecha>02/02/2024</Fecha>
        </Venta>
        <Venta departamento="Petén">
            <Fecha>03/02/2024</Fecha>
        </Venta>
        <Venta departamento="Quetzaltenango">
            <Fecha>04/02/2024</Fecha>
        </Venta>
        <Venta departamento="Quiché">
            <Fecha>05/02/2024</Fecha>
        </Venta>
        <Venta departamento="Retalhuleu">
            <Fecha>06/02/2024</Fecha>
        </Venta>
        <Venta departamento="Sacatepéquez">
            <Fecha>07/02/2024</Fecha>
        </Venta>
        <Venta departamento="San Marcos">
            <Fecha>08/02/2024</Fecha>
        </Venta>
        <Venta departamento="Santa Rosa">
            <Fecha>09/02/2024</Fecha>
        </Venta>
        <Venta departamento="Sololá">
            <Fecha>10/02/2024</Fecha>
        </Venta>
        <Venta departamento="Suchitepéquez">
            <Fecha>11/02/2024</Fecha>
        </Venta>
        <Venta departamento="Totonicapán">
            <Fecha>12/02/2024</Fecha>
        </Venta>
        <Venta departamento="Zacapa">
            <Fecha>13/02/2024</Fecha>
        </Venta>
        <Venta departamento="Guatemala">
            <Fecha>14/02/2024</Fecha>
        </Venta>
    </ListadoVentas>
</Resumen>
'''

    try:
        arbol = ET.ElementTree(ET.fromstring(contenido))  # Se lee el contenido XML desde una cadena
        #arbol = ET.parse(contenido) #Se lee el archivo XML
        ramas = arbol.getroot() #Se obtiene la raíz del archivo XML
        for i in ramas.iter("ListadoVentas"):
            for j in i.iter("Venta"):
                departamento=(j.get("departamento"))
                departamentos.append(departamento)
                print(departamento)
        
        for i in departamentos:
            raiz=ET.Element("Resultados")
            rama=ET.SubElement(raiz,"Departamentos")
            for i in posiblesDepartamentos:
                n=0
                for j in departamentos:
                    if i==j:
                        n+=1
                if n>0:
                    ramita=ET.SubElement(rama,i)
                    ramitita=ET.SubElement(ramita,"cantidadVentas")
                    ramitita.text=str(n)

                    #Creo la lista con los datos
                    pXn.append([i,n])

        salida=ET.ElementTree(raiz)
        paisVnumero=pXn
        ET.dump(raiz) #La verdad no entiendo nada de esta parte xd
        indent(raiz)
        salida.write("salida.xml",encoding="utf-8",xml_declaration=True)

    except Exception as e:
        print(e)
        
    

crearSalida("archivo.xml")
