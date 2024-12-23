from flask import Flask, render_template, url_for
import os
import urllib.parse

app = Flask(__name__)

# Racine du dossier à parcourir
BASE_FOLDER = "static/bl"

def normalize_url_path(path):
    """
    Remplace les antislashs par des slashs pour les URLs.
    """
    return path.replace("\\", "/")

def get_folders_with_images(base_folder):
    """
    Parcourt récursivement le dossier de base pour trouver les sous-dossiers contenant des images.
    """
    folders_with_images = {}
    for root, dirs, files in os.walk(base_folder):
        # Filtrer les fichiers d'images
        images = [f for f in files if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]
        if images:
            # Obtenir le chemin relatif et normalisé
            relative_path = normalize_url_path(os.path.relpath(root, base_folder))
            folders_with_images[relative_path] = images
    return folders_with_images

@app.route('/')
def index():
    """
    Page d'accueil : affiche un sommaire des dossiers contenant des images.
    """
    folders_with_images = get_folders_with_images(BASE_FOLDER)
    return render_template('index.html', folders=folders_with_images)

@app.route('/folder/<path:folder_path>')
def show_folder(folder_path):
    """
    Page affichant les images d'un dossier sélectionné.
    """
    # Décoder et normaliser le chemin
    folder_path = urllib.parse.unquote(folder_path)
    folder_abs_path = os.path.normpath(os.path.join(BASE_FOLDER, folder_path))
    
    # Récupérer les fichiers d'images
    images = [f for f in os.listdir(folder_abs_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]
    images = [normalize_url_path(f) for f in images]
    
    return render_template('folder.html', folder=normalize_url_path(folder_path), images=images)

if __name__ == '__main__':
    app.run(debug=True)
