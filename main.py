from flask import Flask, render_template, request, url_for
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
from PIL import Image
import base64
from io import BytesIO
from test import classes

app = Flask(__name__)

classes = classes


@app.route('/')
def index():
    return render_template('main.html', animals=class_names)


current_dir = os.getcwd()
model = tf.keras.models.load_model(os.path.join(current_dir, 'model.h5'),
                                   custom_objects={'KerasLayer': hub.KerasLayer}, compile=False)

model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])


class_names = list(classes.keys())


def image_nparray_to_base64(np_array):
    # Convert the NumPy array to a Pillow image
    image = Image.fromarray(np_array)

    # Create a buffer to store the image data
    buffered = BytesIO()

    # Save the image as PNG to the buffer
    image.save(buffered, format="PNG")

    # Get the byte data from the buffer
    image_data = buffered.getvalue()

    # Encode the image data to Base64
    base64_encoded = base64.b64encode(image_data).decode('utf-8')

    return base64_encoded


def predict(image_file):
    image = Image.open(image_file)
    # print("THIS IS FROM PIL IMAGE", image)
    image = np.array(image)
    base64_encoded = image_nparray_to_base64(image)
    img = tf.keras.preprocessing.image.smart_resize(image, (224, 224))
    img = img / 255.0
    pred = model.predict(np.expand_dims(img, axis=0))
    pred = np.argmax(pred)
    for key, value in classes.items():
        if value == pred:
            return key, base64_encoded
# ... (previous code)


@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file part'
    image_file = request.files['image']
    # print("THIS IS THE IMAGE FILE", image_file)

    if image_file.filename == '':
        return 'No selected file'

    if image_file:
        width = "300px"
        height = "300px"
        # Change the 'uploads' folder path to the directory where you want to store the images.
        prediction, bas64_array = predict(image_file)
        src = 'data:image/jpeg;base64,' + bas64_array
        return render_template('output.html', data=src, name=prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=True, debug=True)
