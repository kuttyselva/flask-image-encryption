from flask_restful import Resource
import os
from cryptosteganography import CryptoSteganography
from flask import Flask , request ,jsonify
import base64
import logging as logger
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome import Random
from PIL import Image

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]

class Another(Resource):
    def post(self):
        file = request.files['image'].read()
        passcode = request
        cipher = AESCipher('mysecretpassword')
        encrypted = cipher.encrypt(file)
        decrypted = cipher.decrypt(encrypted)
        crypto_steganography = CryptoSteganography('My secret password key')
        # Save the encrypted file inside the image
        crypto_steganography.hide('img.jpg', 'output_image_file.png', encrypted)
        with open('output_image_file.png', "rb") as output:
            message = output.read()
        os.remove('output_image_file.png')
        img_base64 = base64.b64encode(message)
        return jsonify({'status':str(img_base64)[2:-1]})

class AESCipher:

    def __init__( self, key ):
        self.key = bytes(key, 'utf-8')

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] )).decode('utf8')

        