import random
import string
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generar_contraseña', methods=['POST'])
def generar_contraseña():
    data = request.json
    longitud = int(data.get('longitud', 12))  # Convierte a entero aquí
    usar_letras = data.get('usar_letras', True)
    usar_numeros = data.get('usar_numeros', True)
    usar_caracteres = data.get('usar_caracteres', True)

    caracteres = ''
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_caracteres:
        caracteres += string.punctuation

    if not caracteres:  # Si no se selecciona ningún tipo de carácter
        return jsonify(contraseña="No se seleccionó ningún tipo de carácter."), 400

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return jsonify(contraseña=contraseña)

if __name__ == '__main__':
    app.run(debug=True)
