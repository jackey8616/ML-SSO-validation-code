import os, sys, traceback
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys, random
import numpy as np
from keras.models import *
from keras.layers import *

from Fetcher import getImage
from Captcha.SSOCaptcha import SSOCaptcha
from Captcha.Vocab import Vocab

generator = SSOCaptcha()
characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
width = generator.width
height = generator.height
n_len = generator.len
n_class = generator.vocab.size
print(width, height, n_len, n_class)

# Captcha generator from method.
def gen(batch_size=32):
    X = np.zeros((batch_size, height, width, 3), dtype=np.uint8)
    y = [np.zeros((batch_size, n_class), dtype=np.uint8) for i in range(n_len)]
    generator = SSOCaptcha()
    while True:
        for i in range(batch_size):
            img, text = generator.get_captcha()
            X[i] = img
            for j, ch in enumerate(text):
                y[j][i, :] = 0
                y[j][i, characters.find(ch)] = 1
        yield X, y

def genFromImages(imageTuple):
    X = np.zeros((len(imageTuple), height, width, 3), dtype=np.uint8)
    y = [np.zeros((len(imageTuple), n_class), dtype=np.uint8) for i in range(n_len)]
    while True:
        for i in range(len(imageTuple)):
            img, text = imageTuple[i]
            X[i] = img
            for j, ch in enumerate(text):
                y[j][i, :] = 0
                y[j][i, characters.find(ch)] = 1
        yield X, y

def decode(y):
    y = np.argmax(np.array(y), axis=2)[:,0]
    return ''.join([characters[x] for x in y])

class SSOModel(object):

    def __init__(self, debug=False):
        self.debug = debug

    def create(self):
        input_tensor = Input((height, width, 3))
        x = input_tensor
        for i in range(4):
            x = Convolution2D(32*2**i, kernel_size=(3, 3), padding='same', activation='relu')(x)
            x = Convolution2D(32*2**i, kernel_size=(3, 3), padding='same', activation='relu')(x)
            x = MaxPooling2D((2, 2))(x)

        x = Flatten()(x)
        x = Dropout(0.25)(x)
        x = [Dense(n_class, activation='softmax', name='c%d'%(i+1))(x) for i in range(4)]

        self.model = Model(input=input_tensor, output=x)
        if self.debug:
            print('Model Created')

    def summary(self):
        print(self.model.summary())

    def compile(self):
        self.model.compile(loss='categorical_crossentropy',
                           optimizer='adadelta',
                           metrics=['accuracy'])
        if self.debug:
            print('Model Compiled')
    
    def train(self, stepsPerEpoch=10000, epochs=1, validationSteps=1280):
        self.model.fit_generator(gen(),
                                 validation_data=gen(),
                                 steps_per_epoch=stepsPerEpoch,
                                 epochs=epochs,
                                 validation_steps=validationSteps)

    def productionPredict(self, cookies):
        try:
            X = np.zeros((1, height, width, 3), dtype=np.uint8)
            img, text = getImage(cookies)
            X[0] = img
            y_pred = self.model.predict(X)
            print('pred:%s' % decode(y_pred))
            return decode(y_pred)
        except Exception as e:
            traceback.print_exc()
            return None

    def testPredict(self, batch_size=1):
        X, y = next(gen(batch_size=batch_size))
        y_pred = self.model.predict(X)
        print('real: %s\npred:%s'%(decode(y), decode(y_pred)))    

    def save(self):
        modelJson = self.model.to_json()
        with open('./model/sso.model.json', 'w') as jsonFile:
            jsonFile.write(modelJson)
        self.model.save_weights('./model/sso.weights.h5')
        if self.debug:
            print('Model Saved.')

    def load(self):
        modelJson = None
        with open('./model/sso.model.json', 'r') as jsonFile:
            modelJson = jsonFile.read()
        self.model = model_from_json(modelJson)
        self.model.load_weights('./model/sso.weights.h5')
        self.compile()
        if self.debug:
            self.testPredict()
            print('Model Loaded')

if __name__ == "__main__":
    model = SSOModel(debug=True)
    model.load()
    model.testPredict()

