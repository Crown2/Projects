import socket

#check if input is an integer
def check(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
from_server = ''
amount = 0
greeting = 'hello'
client.send(greeting)
while True:
	print('Please select an option:\n 1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ')
	select = input()
	client.send(select)

	#View Balance
	if select == '1':
		from_server = client.recv(4096)
		print('Available Balance: $%s' % from_server)

	#Withdraw
	elif select == '2':
		print('Input the amount to withdraw:')
		amount = input()
		if check(amount) == False:
			print('Error: This query requires a integer value\n')
			client.send('error')
		else:
			client.send(amount)
			from_server = client.recv(4096)

			if from_server == amount:
				print('WITHDREW: $%s' % from_server)
				continue

			else:
				print('Error: Insufficient funds necessary to complete request\n')
				continue

	#Deposit
	elif select == '3':
		print('Input the amount to deposit:')
		amount = input()
		if check(amount) == False:
			print('Error: This query requires a integer value\n')
			client.send('error')

		else:
			print(amount)
			client.send(amount)
			from_server = client.recv(4096)
			print('DEPOSITED: $%s' % from_server)

	#Exit
	elif select == '4':
		break

	elif select == '2319':
		print('\nSuper secret code activated')
		break
	else:
		print('Error: Invalid Input\nValid Inputs: 1,2,3,4\n')
print('\nTransaction is now complete')
print('\nClient shutting down...')
client.close()

