from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/subir-xml', methods=['POST'])
def subir_xml():
    if 'archivo' not in request.files:
        return jsonify({'error': 'No se subió ningún archivo XML'}), 400

    archivo = request.files['archivo']
    if archivo.filename == '':
        return jsonify({'error': 'El nombre del archivo está vacío'}), 400

    try:
        # Parsear el archivo XML
        tree = ET.parse(archivo)
        root = tree.getroot()

        # Extraer los datos (ajustar según la estructura del XML)
        datos = [float(item.find('valor').text) for item in root.findall('.//item')]

        # Devolver los datos como JSON
        return jsonify(datos), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
