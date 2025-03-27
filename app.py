from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para almacenar puntuaciones
puntuaciones = []

@app.route('/enviar_puntuacion', methods=['POST'])
def enviar_puntuacion():
    data = request.get_json()
    if not data or 'nombre' not in data or 'puntuacion' not in data:
        return jsonify({"error": "Datos inválidos, se requieren 'nombre' y 'puntuacion'"}), 400
    
    try:
        puntuacion = int(data['puntuacion'])
    except ValueError:
        return jsonify({"error": "La puntuación debe ser un entero"}), 400

    puntuaciones.append({
        "nombre": data['nombre'],
        "puntuacion": puntuacion
    })
    return jsonify({"mensaje": "Puntuación registrada correctamente"}), 200

@app.route('/ranking', methods=['GET'])
def ranking():
    # Ordena de mayor a menor
    ranking_ordenado = sorted(puntuaciones, key=lambda x: x['puntuacion'], reverse=True)
    return jsonify(ranking_ordenado)

if __name__ == '__main__':
    # Corre en 127.0.0.1:5000
    app.run(host='127.0.0.1', port=5000, debug=True)
