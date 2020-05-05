from flask_restful import Resource
import os, urllib.request
from io import BytesIO
from cryptosteganography import CryptoSteganography
from flask import Flask, request, jsonify
import base64, logging as logger
from .Encryptor import Encryptor
import time
import numpy as np
import pickle 
from PIL import Image
import pywt
class Task(Resource):
    def post(self):
            file_url = request.form['image_url']
            filename=str(time.time_ns())
            urllib.request.urlretrieve(file_url,filename+'.png')
            passcode = request.form['passcode']
            crypto_steganography = CryptoSteganography(passcode)
            decrypted_img = crypto_steganography.retrieve(filename+'.png')
            with open(filename+'.obj'+'.enc', 'wb') as f:
                f.write(decrypted_img)  
            enc.decrypt_file(filename+'.obj'+'.enc')


            file_pi2 = open(filename+'.obj', 'rb') 
            object_pi2 = pickle.load(file_pi2)
            response = pywt.idwt2(object_pi2, "haar")
            response = response.astype('uint8')
            print('hii')
            res = Image.fromarray(response, "RGBA")
            res.save(filename+'.png')
            res.save('123'+'.png')
            with open(filename+'.png', "rb") as output:
                message = output.read()
            img_base64 = base64.b64encode(message)
            # os.remove(filename+'.png')
            return jsonify({'status':str(img_base64)[2:-1]})
key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')
  