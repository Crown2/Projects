import Crypto
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pss
import time

# Part 3
print('Key Size: 2048 bits')
private_key = RSA.generate(2048)
public_key = private_key.publickey()

#Take user input for the message to be encrypted/decrypted
data = input("Enter Alice's message to Bob: ").encode()
h = SHA256.new(data)
# Start clock used to monitor encryption times
start = time.time()

for loop in range(100):
	signature = pss.new(private_key).sign(h)

#End clock for encryptions
end = time.time()
totaltime = end - start
averagetime = totaltime/100
print ('\nTotal time taken: %ss' % totaltime)
print('Average time per signature: %ss' %averagetime)

# Start clock used to monitor verification times
start = time.time()

for loop in range(100):
	verifier = pss.new(public_key)
	try:
		verifier.verify(h, signature)
		check = 0
	except (ValueError, TypeError):
		check = 1

if check == 0:
	print('The signature is authentic')
elif check == 1:
	print('The signature is not authentic')

#End clock for decryptions
end = time.time()
totaltime = end - start
averagetime = totaltime/100
print ('\nTotal time taken: %ss' % totaltime)
print('Average time per verification: %ss' %averagetime)