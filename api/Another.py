from flask_restful import Resource
import os
from cryptosteganography import CryptoSteganography
from flask import Flask , request ,jsonify
import base64
import logging as logger
from .Encryptor import Encryptor
from Cryptodome import Random
from Cryptodome.Cipher import AES
import datetime
import os.path
from os import listdir
from os.path import isfile, join
import time
import numpy as np
import pickle 
from PIL import Image
import pywt
class Another(Resource):
    def post(self):
        file = request.files['image'].read()
        filename=str(time.time_ns())+'.png'
        with open(filename, 'wb') as f:
            f.write(file)

        imgObj = Image.open(filename)
        img = np.array(imgObj)
        res_pywt = pywt.dwt2(img, "haar")
        file_pi = open('filename_pi.obj', 'wb')
        pickle.dump(res_pywt, file_pi)

        enc.encrypt_file('filename_pi.obj')
        with open('filename_pi.obj'+'.enc', 'rb') as f:
            encrypted_image= f.read()
        passcode = request.form['passcode']
        crypto_steganography = CryptoSteganography(passcode)
        # Save the encrypted file inside the image
        crypto_steganography.hide('img.jpg', 'output_image_file.png', encrypted_image)
        with open('output_image_file.png', "rb") as output:
            message = output.read()
        os.remove('output_image_file.png')
        img_base64 = base64.b64encode(message)
        return jsonify({'status':str(img_base64)[2:-1]})
key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')
