# server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))

s.listen(4)

print("Server has started")

client, address = s.accept()
print("Client has connected from the address", address)

while True:
	server_message = input("Server :: ")
	client.send(bytes(server_message, "utf-8"))
	client_message = client.recv(100)
	print("Client ::", client_message.decode("utf-8"))