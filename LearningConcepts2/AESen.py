import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

# Generate Key
# key = get_random_bytes(24) # 24 bytes * 8 = 192 bits (1 byte = 8 bits)

#import secret key
key_file = 'AESKey.txt'

# Read the key from the file
key_in = open(key_file, 'rb') # Open the file to read bytes
key = key_in.read()
key_in.close()

data = input("Enter Alice's message to Bob: ").encode() # Convert to bytes.

# Create cipher object and encrypt the data
cipher = AES.new(key, AES.MODE_CBC) # Create a AES cipher object using key and CBC mode
ciphered_data = cipher.encrypt(pad(data, AES.block_size)) # Padding before encryption
print('Send ciphered data: %s' %ciphered_data)

# Send encryption to ctext.txt
output_file = 'ctext.txt' # Output file
file_out = open(output_file, "wb") # Open file to write bytes
file_out.write(cipher.iv) # Write the iv to ctext.txt
file_out.write(ciphered_data) # Write the cipher text to the file.
file_out.close()
