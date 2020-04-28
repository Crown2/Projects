import hmac
import hashlib
import binascii

# Part 1
def create_sha256_signature(key, message):
	byte_key = binascii.unhexlify(key)
	message = message.encode()
	return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()

key_file = 'SHAKey.txt'

# Read the key from the file
key_in = open(key_file, 'r') # Open the file
key = key_in.read()
key_in.close()

# Create HMAC
data = input("Enter Alice's message to Bob: ")
hmac = create_sha256_signature(key, data)

# Send to mactext.txt
output_file = 'mactext.txt' # Output file
file_out = open(output_file, "w") # Open file
file_out.write(data) # Write the message to mactext.txt
file_out.write("\n")
file_out.write(hmac) # Write the hmac to the file.
file_out.close()
