import socket
import random

class Account:
	# Construct an Account object
	def __init__(self, id, balance):
		self.id = id
		self.balance = balance

	def getBalance(self):
		return self.balance

	def withdraw(self, amount):
		self.balance -= amount

	def deposit(self, amount):
		self.balance += amount


def main():

	account = Account(1, 10000)
	serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serv.bind(('0.0.0.0', 8080))
	serv.listen(5)

	#initialize transaction
	while True:
		conn, addr = serv.accept()
		from_client = ''
		data = conn.recv(4096)
		from_client = data
		if from_client == 'hello':
			# ATM Processes
			while True:
				data = conn.recv(4096)
				from_client = data

				if from_client == '1':
					#execute option 1
					conn.send(str(account.getBalance()))
					print('USER REQUEST TYPE: VIEW BALANCE: $%s' %str(account.getBalance()))
					continue

				elif from_client == '2':
					#execute option 2
					data = conn.recv(4096)
					if data == 'error':
						print('ERROR: incorrect input')
						continue

					if int(data) <= account.getBalance():
						account.withdraw(int(data))
						print('USER REQUEST TYPE: WITHDRAW\t AMOUNT: $%s' % data)
						conn.send(data)
					else:
						print('ERROR: INSUFFICIENT FUNDS FOR WITHDRAWL')
						conn.send('error')
					continue

				elif from_client == '3':
					#execute option 3
					data = conn.recv(4096)
					if data == 'error':
						print('ERROR: incorrect input\n')
						continue
					print(data)
					account.deposit(int(data))
					print('USER REQUEST TYPE: DEPOSIT\t AMOUNT: $%s' % data)
					conn.send(data)
					continue

				elif from_client == '4':
					#execute option 4
					break

				elif from_client == '2319': #used to manually kill the server via client so I dont have to restart the terminal 500 billion times while debugging
					#execute option secret
					print('Server kill requested by client\nShutting down...')
					conn.close()
					exit()
				else:
					print('INVALID USER REQUEST TYPE')
		conn.close()
		print('client disconnected')

	print('Server shutting down')

# Main function
main()