import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

#keyPair = RSA.generate(2048)

key_in = open('RSApublicKey.pem','r')
pubKey = RSA.import_key(key_in.read())

data = input("Enter Alice's message to Bob: ").encode()
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(data)
print("Sent encryption:", binascii.hexlify(encrypted))

output_file = 'ctext.txt' # Output file
file_out = open(output_file, "wb") # Open file to write bytes
file_out.write(encrypted) # Write the varying length cipher text to the file (this is the encrypted data)
file_out.close()
