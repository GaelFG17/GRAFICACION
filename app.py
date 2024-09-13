from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Cargar y convertir la imagen
            img = Image.open(file.stream)
            img = img.convert('L')  # Convertir a escala de grises
            matriz = np.array(img).tolist()  # Convertir a lista para almacenar en variable
            print(matriz)
            app.config['MATRIZ'] = matriz

            return redirect(url_for('confirmation'))
    return render_template('index.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
