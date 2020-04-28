import base64
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#Process user input for key size selection.
while True:
	select = input("\nInput 1, 2, or 3 to select a key size:\n(1) 1024 bits\n(2) 2048 bits\n(3) 4096 bits\n")
	if select == '1':
		print('Key Size: 1024 bits')
		keyPair = RSA.generate(1024)
		pubKey = keyPair.publickey()
		break
	elif select == '2':
		print('Key Size: 2048 bits')
		keyPair = RSA.generate(2048)
		pubKey = keyPair.publickey()
		break
	elif select == '3':
		print('Key Size: 4096 bits')
		keyPair = RSA.generate(4096)
		pubKey = keyPair.publickey()
		break
	else:
		print('Error: Invalid Input\nValid Inputs: 1,2,3,4\n')

#Take user input for the message to be encrypted/decrypted
data = input("Enter Alice's message to Bob: ").encode()


# Start clock used to monitor encryption times
start = time.process_time()

for loop in range(100):
	encryptor = PKCS1_OAEP.new(pubKey)
	encrypted = encryptor.encrypt(data)
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
	decryptor = PKCS1_OAEP.new(keyPair)
	decrypted = decryptor.decrypt(encrypted)

#End clock for decryptions
end = time.process_time()
totaltime = end - start
averagetime = totaltime/100
print ('\nTotal time taken: %ss' % totaltime)
print('Average time per decryption: %ss' %averagetime)


