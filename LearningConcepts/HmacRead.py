import hmac
import hashlib
import binascii

# Part 1
def create_sha256_signature(key, message):
	byte_key = binascii.unhexlify(key)
	message = message.encode()
	return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()

def verify_signature(key, msg, h):
	verify = create_sha256_signature(key, msg)
	print('Verification HMAC: %s' %verify)
	if verify == h:
		print('HMAC Verified Successfully')
		return True
	else:
		print('HMAC Verification Failed')
		return False


key_file = 'SHAKey.txt'
data_file = 'mactext.txt'

# Read the key from the file
key_in = open(key_file, 'r') # Open file
key = key_in.read()
key_in.close()

# Read the message data from the file
data_in = open(data_file, 'r')
msg = data_in.readline().rstrip('\n') # Message
h = data_in.readline() # HMAC
data_in.close()

print('\nMessage Contents: %s' %msg)
print('HMAC Sent: %s\n' %h)

# Check HMAC
check = verify_signature(key, msg, h)

