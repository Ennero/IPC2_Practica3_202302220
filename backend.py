from flask import Flask, request, jsonify

import backend2 as b2

app = Flask(__name__)

@app.route('/carga', methods=['POST'])
def subir_xml():
    if 'archivo' not in request.files:  # Si no se subió ningún archivo
        return jsonify({'error': 'No se subió ningún archivo XML'}), 400 # Bad request

    archivo = request.files['archivo'] # Se obtiene el archivo XML

    if archivo.filename == '': # Si el nombre del archivo está vacío
        return jsonify({'error': 'El nombre del archivo está vacío'}), 400

    contenido = archivo.read().decode('utf-8') # Se lee el contenido del archivo XML

    b2.crearSalida(contenido) # Se crea el archivo de salida
    return jsonify({'mensaje': 'Archivo XML recibido correctamente'}), 200
    

@app.route('/grafica', methods=['POST'])
def grafico():
    if 'salida' not in request.files:  # Si no se subió ningún archivo
        return jsonify({'error': 'No se subió ningún archivo XML'}), 400 # Bad request
    
    salida=request.files['salida']

    if salida.filename == '': # Si el nombre del archivo está vacío
        return jsonify({'error': 'El nombre del archivo está vacío'}), 400

    return b2.grafico()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
