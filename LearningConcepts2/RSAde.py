import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

key_in = open('RSAkeyPair.pem','r')
keyPair = RSA.import_key(key_in.read())

input_file = 'ctext.txt' # Input file
file_in = open(input_file, 'rb') # Open the file to read bytes
ciphered_data = file_in.read() # Read the rest of the data
file_in.close()
print("Received encryption:", binascii.hexlify(ciphered_data))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(ciphered_data)
print('Decrypted: %s' %decrypted.decode('utf-8'))
