import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import time

#Process user input for key size selection.
while True:
	select = input("\nInput 1, 2, or 3 to select a key size:\n(1) 128 bits\n(2) 192 bits\n(3) 256 bits\n")
	if select == '1':
		print('Key Size: 128 bits')
		key = get_random_bytes(16) # 16 bytes * 8 = 128 bits
		break
	elif select == '2':
		print('Key Size: 192 bits')
		key = get_random_bytes(24) # 24 bytes * 8 = 192 bits
		break
	elif select == '3':
		print('Key Size: 256 bits')
		key = get_random_bytes(32) # 32 bytes * 8 = 256 bits
		break
	else:
		print('Error: Invalid Input\nValid Inputs: 1,2,3,4\n')

#Take user input for the message to be encrypted/decrypted
data = input("Enter Alice's message to Bob: ").encode()

# Start clock used to monitor encryption times
start = time.process_time()

for loop in range(100):
	# Create cipher object and encrypt the data
	cipher = AES.new(key, AES.MODE_CBC) # Create a AES cipher object with the key using the mode CBC
	ciphered_data = cipher.encrypt(pad(data, AES.block_size)) # Pad the input data and then encrypt
	#print("Encryption %s" %loop)

#End clock for encryptions
end = time.process_time()
totaltime = end - start
averagetime = totaltime/100
print ('\nTotal time taken: %ss' % totaltime)
print('Average time per encryption: %ss' %averagetime)

# Start clock used to monitor decryption times
start = time.process_time()

for loop in range(100):
	cipher = AES.new(key, AES.MODE_CBC, iv=cipher.iv)  # Setup cipher
	original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) # Decrypt and then up-pad the result

#End clock for decryptions
end = time.process_time()
totaltime = end - start
averagetime = totaltime/100
print ('\nTotal time taken: %ss' % totaltime)
print('Average time per decryption: %ss' %averagetime)

print('\nOriginal data: %s' %original_data.decode('utf-8'))