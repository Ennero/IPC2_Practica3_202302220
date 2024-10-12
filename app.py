from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/subir-xml', methods=['POST'])
def subir_xml():
    if 'archivo' not in request.files:
        return 'No se ha enviado el archivo', 400

    archivo=request.files['archivo']
    if archivo.filename == '':
        return 'No se ha enviado el archivo', 400
    
    try:
        tree = ET.parse(archivo)
        root = tree.getroot()

        datos = [float(item.find('valor').text) for item in root.findall('.//item')]

        return jsonify(datos), 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
