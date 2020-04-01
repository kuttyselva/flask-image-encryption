from flask_restful import Resource
import os, urllib.request
from io import BytesIO
from cryptosteganography import CryptoSteganography
from flask import Flask, request, jsonify
import base64, logging as logger
from .Encryptor import Encryptor
import time

class Task(Resource):
    def post(self):
            file_url = request.form['image_url']
            filename=str(time.time_ns())+'.png'
            urllib.request.urlretrieve(file_url,filename)
            passcode = request.form['passcode']
            crypto_steganography = CryptoSteganography(passcode)
            decrypted_img = crypto_steganography.retrieve(filename)
            with open(filename+'.enc', 'wb') as f:
                f.write(decrypted_img)  
            enc.decrypt_file(filename+'.enc')
            with open(filename, "rb") as output:
                message = output.read()
            img_base64 = base64.b64encode(message)
            return jsonify({'status':str(img_base64)[2:-1]})


            # with open(filename, 'rb') as f:
            # encrypted_image= f.read()
            # # Save the encrypted file inside the image
            # crypto_steganography.hide('img.jpg', 'output_image_file.png', encrypted_image)
            # with open('output_image_file.png', "rb") as output:
            #     message = output.read()
            # os.remove('output_image_file.png')
            # img_base64 = base64.b64encode(message)
            # return jsonify({'status':str(img_base64)[2:-1]})
key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')
  