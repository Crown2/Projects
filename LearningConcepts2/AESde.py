import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

# import secret key
key_file = 'AESKey.txt'

# Read the key from the file
key_in = open(key_file, 'rb') # Open the file to read bytes
key = key_in.read()
key_in.close()

input_file = 'ctext.txt' # Input file

# Read the data from the file
file_in = open(input_file, 'rb') # Open the file to read bytes
iv = file_in.read(16) # Read the iv
read_data = file_in.read() # Read the remaining data
file_in.close()
print('Received ciphered data: %s' %read_data)

# Decrypt ciphered data
cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher
original_data = unpad(cipher.decrypt(read_data), AES.block_size) # Decrypt and then up-pad the result

print('Original data: %s' %original_data.decode('utf-8'))