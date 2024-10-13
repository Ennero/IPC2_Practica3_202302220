from flask import Flask, request, jsonify

import backend2 as b2

app = Flask(__name__)

@app.route('/carga', methods=['POST'])
def subir_xml():
    if 'archivo' not in request.files:
        return jsonify({'error': 'No se subió ningún archivo XML'}), 400

    archivo = request.files['archivo']
    if archivo.filename == '':
        return jsonify({'error': 'El nombre del archivo está vacío'}), 400

    contenido = archivo.read().decode('utf-8')
    print(contenido)

    b2.crearSalida(contenido)
    try:
        # Parsear el archivo XML
        #print(archivo) 
        tree = ET.parse(contenido)
        root = tree.getroot()


        # Extraer los datos (ajustar según la estructura del XML)
        datos = [float(item.find('valor').text) for item in root.findall('.//item')]

        # Devolver los datos como JSON
        return jsonify(datos), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
