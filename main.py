from img_procesor import img_procesor
import numpy as np
import tensorflow as tf
from dog_list import dog_class
from flask import Flask, jsonify , request 
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS

model = tf.keras.models.load_model('./modelo/modelo_perros.h5')

# Flask

app = Flask(__name__)

UPLOAD_FOLDER = "./imagenes"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
  return jsonify(author="Api by jhon.")


@app.route('/api/upload', methods=['POST'])
def ProccesarImage():
    
    if request.method == 'POST':
        if 'chandozo' not in request.files:
            return  jsonify(success=False, msg="No hay imagen enviada.")
        file = request.files['chandozo']
        if file.filename == '':
            return  jsonify(success=False, msg="Imagen incorrecta")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            imgpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(imgpath)
            img_path = imgpath
            img = img_procesor.procs_img(img_path)  
            print("ruta de imagen ",img_path)
            predictions = model.predict(img)
            score = predictions[0]
            top_index_list = np.argsort(score)[::-1][:3]
            jsonData = '[{"raza": "' +  dog_class.dogindex(top_index_list[0]) + '", "procentaje": "' + "{:.2f}".format(score[top_index_list[0]]*100) + '"}, {"raza": "' +  dog_class.dogindex(top_index_list[1]) + '" , "procentaje": "' + "{:.2f}".format(score[top_index_list[1]]*100) + '"} , {"raza": "' +  dog_class.dogindex(top_index_list[2]) + '" ,  "procentaje": "' + "{:.2f}".format(score[top_index_list[2]]*100) + '"}]'
            return  jsonify(success=True, msg="Todo correcto.", data=jsonData)       
        else:
            return jsonify(success=False, msg="Error SERVER")

if __name__ == '__main__':
    CORS(app)
    app.run()
    



