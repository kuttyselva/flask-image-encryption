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

class Another(Resource):
    def post(self):
        try:
            file = request.files['image'].read()
            filename=str(time.time_ns())+'.png'
            with open(filename, 'wb') as f:
                f.write(file)  
            enc.encrypt_file(filename)
            with open(filename+'.enc', 'rb') as f:
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
        except:
            return 'no image',status.HTTP_404_NOT_FOUND

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')
