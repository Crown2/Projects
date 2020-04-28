import hmac
import hashlib
import binascii
import time

# Part 3
def create_sha256_signature(key, message):
	byte_key = binascii.unhexlify(key)
	message = message.encode()
	return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()

def verify_signature(key, msg, sig):
	verify = create_sha256_signature(key, msg)
	#print('Verification HMAC: %s' %verify)
	if verify == sig:
		return True
	else:
		return False

key_file = 'SHAKey.txt'

# Read the key from the file
key_in = open(key_file, 'r') # Open file
key = key_in.read()
key_in.close()

data = input("Enter Alice's message to Bob: ")

# Start clock used to monitor signing times
start = time.time()

for loop in range(100):
	sig = create_sha256_signature(key, data)


#End clock for HMAC generation
end = time.time()
totaltime = end - start
averagetime = totaltime/100
print ('\nTotal time taken: %ss' % totaltime)
print('Average time per HMAC generation: %ss' %averagetime)

# Start clock used to monitor verification times
start = time.time()

for loop in range(100):
	check = verify_signature(key, data, sig)

#End clock for verifications
end = time.time()
totaltime = end - start
averagetime = totaltime/100
print ('\nTotal time taken: %ss' % totaltime)
print('Average time per verification: %ss' %averagetime)