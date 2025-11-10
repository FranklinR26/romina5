import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# === Configuración de carpetas ===
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# === Ruta principal ===
@app.route('/')
def index():
    return render_template('index.html')


# === Ruta para subir imágenes ===
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No se envió ningún archivo", 400

    file = request.files['file']
    if file.filename == '':
        return "Archivo no válido", 400

    # Guardar archivo
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(save_path)

    return redirect(url_for('gallery'))


# === Ruta de galería ===
@app.route('/gallery')
def gallery():
    # Listar archivos en la carpeta uploads
    image_folder = app.config['UPLOAD_FOLDER']
    images = []
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            images.append(url_for('static', filename=f'uploads/{filename}'))
    return render_template('gallery.html', images=images)


# === Arranque local ===
if __name__ == '__main__':
    app.run(debug=True)
