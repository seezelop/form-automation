from flask import Flask, request, jsonify
from flask_cors import CORS  
from enviar_correo_param import enviar_correo_param  # Importo función parametrizada

app = Flask(__name__)
CORS(app)

@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        correo = request.form['correo']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']
        archivo = request.files['archivo']

        # Guardar el archivo temporalmente
        archivo_ruta = archivo.filename
        archivo.save(archivo_ruta)

        print(f"Datos recibidos: correo={correo}, asunto={asunto}, mensaje={mensaje}, archivo={archivo.filename}")
        enviar_correo_param(correo, asunto, mensaje, archivo_ruta)

        return jsonify({'status': 'success', 'message': 'Correo enviado correctamente.'}), 200
    except Exception as e:
        print(f"Error al procesar la solicitud: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
