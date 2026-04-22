from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from PIL import Image
import pillow_heif
pillow_heif.register_heif_opener()

app = Flask(__name__)
app.config['MAX_CONTENT-LENGTH'] = 50 * 1024 * 1024
app.secret_key = "" 

UPLOAD_FOLDERS = {
    "art": "static/art",
    "photos": "static/photos"
}

ALLOWED_EXTENSIONS = {'png' , 'jpg', 'jpeg', 'gif', 'heic'}
UPLOAD_PASSWORDS = {
    "art": "",
    "photos": ""
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/<portal>')
def index(portal):
    if portal not in UPLOAD_FOLDERS:
        return "Portal not found", 404
    images = os.listdir(UPLOAD_FOLDERS[portal])
    images.sort()
    return render_template("index.html", images=images, portal=portal)

@app.route('/<portal>/upload', methods=['GET', 'POST'])
def upload(portal):
    if portal not in UPLOAD_FOLDERS:
        return "Portal not found", 404

    if request.method == "POST":
        password = request.form.get("password")
        if password != UPLOAD_PASSWORDS[portal]:
            flash("Incorrect password!")
            return redirect(request.url)

        file = request.files.get("file")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(UPLOAD_FOLDERS[portal], filename)

            file.save(save_path)
            if filename.lower().endswith(".heic"):
                img = Image.open(save_path)
                new_filename = os.path.splitext(filename)[0] + ".jpeg"
                new_save_path = os.path.join(UPLOAD_FOLDERS[portal], new_filename)
                img.convert("RGB").save(new_save_path, "JPEG")
                os.remove(save_path)
                filename = new_filename

            flash("I see magic happening!!!")
            return redirect(request.url)
        else:
            flash("Invalid file type!")
            return redirect(request.url)

    return render_template("upload.html", portal=portal)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
