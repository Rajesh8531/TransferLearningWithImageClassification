from flask import Flask, render_template, request, url_for
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
from PIL import Image
import base64
from io import BytesIO

app = Flask(__name__)

classes = {'antelope': 0, 'badger': 1, 'bat': 2, 'bear': 3, 'bee': 4, 'beetle': 5, 'bison': 6,
           'boar': 7, 'butterfly': 8, 'cat': 9, 'caterpillar': 10, 'chimpanzee': 11, 'cockroach': 12,
           'cow': 13, 'coyote': 14, 'crab': 15, 'crow': 16, 'deer': 17, 'dog': 18, 'dolphin': 19,
           'donkey': 20, 'dragonfly': 21, 'duck': 22, 'eagle': 23, 'elephant': 24, 'flamingo': 25,
           'fly': 26, 'fox': 27, 'goat': 28, 'goldfish': 29, 'goose': 30, 'gorilla': 31,
           'grasshopper': 32, 'hamster': 33, 'hare': 34, 'hedgehog': 35, 'hippopotamus': 36,
           'hornbill': 37, 'horse': 38, 'hummingbird': 39, 'hyena': 40, 'jellyfish': 41,
           'kangaroo': 42, 'koala': 43, 'ladybugs': 44, 'leopard': 45, 'lion': 46, 'lizard': 47,
           'lobster': 48, 'mosquito': 49, 'moth': 50, 'mouse': 51, 'octopus': 52, 'okapi': 53,
           'orangutan': 54, 'otter': 55, 'owl': 56, 'ox': 57, 'oyster': 58, 'panda': 59, 'parrot': 60,
           'pelecaniformes': 61, 'penguin': 62, 'pig': 63, 'pigeon': 64, 'porcupine': 65, 'possum': 66,
           'raccoon': 67, 'rat': 68, 'reindeer': 69, 'rhinoceros': 70, 'sandpiper': 71, 'seahorse': 72,
           'seal': 73, 'shark': 74, 'sheep': 75, 'snake': 76, 'sparrow': 77, 'squid': 78, 'squirrel': 79,
           'starfish': 80, 'swan': 81, 'tiger': 82, 'turkey': 83, 'turtle': 84, 'whale': 85, 'wolf': 86,
           'wombat': 87, 'woodpecker': 88, 'zebra': 89}


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
    app.run( debug=False)
