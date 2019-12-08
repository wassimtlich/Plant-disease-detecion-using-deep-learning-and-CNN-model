import os
import subprocess
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from recognize import recognize
app = Flask(__name__)
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
ALLOWED_EXTENSIONS = {'png','jpg', 'jpeg'}
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) 

app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER


@app.route('/uploads/<filename>')
def uploaded_file(filename):
   return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)


def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
       if 'file' not in request.files:
           print('No file attached in request')
           return redirect(request.url)
       file = request.files['file']
       if file.filename == '':
           print('No file selected')
           return redirect(request.url)
       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(os.path.join(UPLOAD_FOLDER, filename))
   return render_template('index.html')
@app.route('/recognizefun',methods=['GET', 'POST'])
def recognizefun():
   file = request.args.get('file', None)
   aa=recognize(file)
   return render_template('recognizefun.html',aa=aa)


if __name__ == "__main__":
	app.run()
