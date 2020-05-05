from cryptosteganography import CryptoSteganography

message = None
with open('filename_pi.obj.enc', "rb") as f:
    message = f.read()

crypto_steganography = CryptoSteganography('My secret password key')

crypto_steganography.hide('pip.jpg', 'output_image_file.png', message)

crypto_steganography = CryptoSteganography('My secret password key')
decrypted_bin = crypto_steganography.retrieve('output_image_file.png')

# Save the data to a new file
with open('decrypted_sample.mp3', 'wb') as f:
    f.write(secret_bin)