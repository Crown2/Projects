from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# Part 2
# Read key
public_key = RSA.import_key(open('PublicKey.pem').read())

# Read the message data from the file
data_file = 'sigtext.txt'
data_in = open(data_file, 'rb') # Open the file
message = data_in.readline().rstrip('\n'.encode())
signature = data_in.readline()
data_in.close()

# Verify signature using public key
h = SHA256.new(message)
verifier = pss.new(public_key)
try:
	verifier.verify(h, signature)
	print ('Signature successfully verified')
except (ValueError, TypeError):
	print ('Signature verification unsuccessful')
