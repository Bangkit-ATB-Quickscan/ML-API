import os
from PIL import Image as PilImage
from google.cloud import storage
import tensorflow as tf
from io import BytesIO
from flask import Flask, request, jsonify
from keras.models import load_model
import numpy as np
from tensorflow.keras.applications.mobilenet import preprocess_input

app = Flask(__name__)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'atbq-credentials.json'
storage_client = storage.Client()

# model_filename = 'atbq_model_fix.h5'
# model_bucket = storage_client.get_bucket('atbq_bucket')
# model_blob = model_bucket.blob(model_filename)
# model_blob.download_to_filename(model_filename)
# model = load_model(model_filename, custom_objects={'req': req})
model = load_model('atbq_model_fix.h5')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            image_bucket = storage_client.get_bucket(
                'atbq_bucket')
            filename = request.json['filename']
            img_blob = image_bucket.blob('predict_uploads/' + filename)
            img_path = BytesIO(img_blob.download_as_bytes())
        except Exception:
            respond = jsonify({'message': 'Error loading image file'})
            respond.status_code = 400
            return respond


        img = PilImage.open(img_path)
        x = np.array(img)
        x = tf.image.resize(x, [224, 224])
        x = PilImage.fromarray(x.numpy().astype(np.uint8))
        images = np.expand_dims(x, axis=0)
        

        # model predict
        pred_paru = model.predict(images)
        # find the max prediction of the image
        maxx = pred_paru.max()

        prediksi = ['negatif', 'positif']
        
        # for respond output from prediction if predict <=0.4
        if maxx <= 0.75:
            respond = jsonify({
                'message': 'paru tidak terdeteksi'
            })
            respond.status_code = 400
            return respond

        result = {
            "prediksi": prediksi[np.argmax(pred_paru)]
        }

        respond = jsonify(result)
        respond.status_code = 200
        return respond

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')