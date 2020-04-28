import hashlib
import random
import string

# Part 4
def create_hash(message):
	result = hashlib.sha256(message.encode())
	return result.hexdigest()

# initializing variables
N = 18 # random string size
i = 0 # part selection
x = 0 # count number of trials
total = 0 # total number of trials
compare_string1 = '' # hashed string 1
compare_string2 = '' # hashed string 2

#select Part 4A or Part 4B
while True:
	select = input("\nInput 1, 2 to Part 4A or Part 4B:\n(1) Part 4A\n(2) Part 4B\n")
	if select == '1':
		i = 1
		break
	elif select == '2':
		i = 20
		break
	else:
		print('Error: Invalid Input\nValid Inputs: 1, 2\n')

# loop either 1 or 20 time(s) for each loop a while loop is executed that generates random strings untill two strings have the same hash
for loop in range(i):
	x = 0
	current_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k = N)) # generate random string 1
	h = create_hash(current_string)
	compare_string1 = h[0:2]
	if i == 1:
		print("Random string: " + str(current_string) + "\tHash Value: " + h)
	while compare_string1 != compare_string2:
		x += 1
		test_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k = N)) # generate random string 2
		test_h = create_hash(test_string)
		compare_string2 = test_h[0:2]
		# If both hashed strings match and their source strings dont
		if compare_string1 == compare_string2 and test_string != current_string:
			# if Part 4A is selected
			if i == 1:
				print("String_1: " + str(current_string) + "\tHash Value: " + h)
				print("String_2: " + str(test_string) + "\tHash Value: " + h)
				print("Number of tries before collision: %s" %x)
			total += x

if i == 20:
	average = total / i
	print('Average number of tries before collision: %s' %average)










