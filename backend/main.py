from flask import Flask,request,Response
import tensorflow as tf
import numpy as np
import os
from PIL import Image
import io
import base64
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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


def getModel():
    current_dir = os.getcwd()
    model = tf.keras.models.load_model(os.path.join(current_dir, 'mobile_net.h5'))
    model.build([None,224,224,3])
    return model

def predict(model,image_array):
    image_array = tf.image.resize(image_array,(224,224))
    image_array = image_array / 255.0
    pred = model.predict(np.expand_dims(image_array,axis=0))
    pred = np.argmax(pred)
    return pred


@app.route('/predict',methods=["POST"])
@cross_origin()
def handlePredict():
    data = request.get_data()
    base64_decoded = base64.b64decode(data)
    image = Image.open(io.BytesIO(base64_decoded))
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image_array = np.array(image)
    model = getModel()
    pred = predict(model,image_array)
    prediction = ''
    for key, value in classes.items():
        if value == pred:
            prediction = key
    return Response(prediction.capitalize())

if __name__ == '__main__':
    app.run( debug=False)