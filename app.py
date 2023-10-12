import atexit
import json
import os.path
import socket
from flask import Flask, render_template, request, jsonify
import numpy as np
from keras.models import load_model
from PIL import Image
from werkzeug.utils import secure_filename

from ImageProcessor import ImageProcessor as ip

app = Flask(__name__, template_folder='templates')

# Load your trained model
try:
    model = load_model('DigitRecogModel.hdf5')
except Exception as e:
    print("Error loading the model:", str(e))

# Define the upload folder
app.config['UPLOAD_FOLDER'] = 'Uploads'


# Function to preprocess the input
def preprocess_input(image):
    # Your preprocessing code here
    preprocessed_image = ip(image).process()
    preprocessed_image = preprocessed_image.reshape(1, 784)
    return preprocessed_image


@app.route('/')
def home():
    return render_template('index.html', recognized_digit=None)


@app.route('/recognize', methods=['POST'])
def recognize_digit():
    try:
        # Check if a file was uploaded
        if 'digit_image' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['digit_image']

        # Check if the file has a filename
        if file.filename == '':
            return render_template('index.html', recognized_digit=None)

        if file:
            # Read the image from the request
            filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(filename)


            # image = Image.open(os.path.abspath(file.filename))
            # print(type(os.path.abspath(file.filename)))
            # # Preprocess the image
            preprocessed_image = preprocess_input(filename)

            # Make predictions using the model
            predictions = model.predict(preprocessed_image)

            recognized_digit = str(np.argmax(predictions))
            return render_template('index.html', recognized_digit=recognized_digit)

    except Exception as e:
        return jsonify({'error': str(e)})
    
# Cleanup function to delete saved images
def cleanup():
    folder = app.config['UPLOAD_FOLDER']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {str(e)}")

# Register the cleanup function to run at exit
atexit.register(cleanup)


if __name__ == '__main__':
    app.run(debug=True, host=socket.gethostbyname(socket.gethostname()))
