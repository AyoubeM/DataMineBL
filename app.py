from flask import Flask, render_template
import os

app = Flask(__name__)

# Dossier contenant les images
IMAGE_FOLDER = "static/Texture2D"
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def index():
    # Liste tous les fichiers dans le dossier d'images
    image_files = [f for f in os.listdir(app.config['IMAGE_FOLDER']) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]
    return render_template('index.html', images=image_files)

if __name__ == '__main__':
    app.run(debug=True)