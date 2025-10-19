from flask import Flask, render_template, request, jsonify
import numpy as np
import base64
import re
from io import BytesIO
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)


model = load_model('mnist_cnn.h5')

def preprocess_image(image_data):

    image_data = re.sub('^data:image/.+;base64,', '', image_data)


    image = Image.open(BytesIO(base64.b64decode(image_data)))

    image = image.convert('L') 
    
 
    image_array = np.array(image, dtype=np.float32)

    inverted_image_array = 255.0 - image_array


    normalized_image = inverted_image_array / 255.0

    return normalized_image.reshape(1, 28, 28, 1)

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
    
        data = request.get_json()
        image_array = preprocess_image(data['image'])


        prediction = model.predict(image_array)
      
        predicted_digit = int(np.argmax(prediction, axis=1)[0])

        return jsonify({'prediction': predicted_digit})

    except Exception as e:
   
        print(f"Prediction Error: {e}")
        return jsonify({'prediction': f"Server Error: {str(e)}"}), 500


if __name__ == '__main__':

    app.run(debug=True)