import Crypto
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pss

#Part 2
# Read key
key_in = open('PrivateKey.pem','r')
private_key = RSA.import_key(key_in.read())

# Take input and create RSA signature
data = input("Enter Alice's message to Bob: ").encode()
h = SHA256.new(data)
signature = pss.new(private_key).sign(h)

# Print
print('Signature: %s' %signature)

# Send signature to sigtext.txt
output_file = 'sigtext.txt' # Output file
file_out = open(output_file, "wb") # Open file
file_out.write(data) # Write the message to mactext.txt
file_out.write("\n".encode())
file_out.write(signature) # Write the signature to the file.
file_out.close()
