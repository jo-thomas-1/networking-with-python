# client.py

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

server_socket.connect((HOST_NAME, PORT))

while True:
	server_message = server_socket.recv(100)
	print("Server ::", server_message.decode("utf-8"))
	client_message = input("Client :: ")
	server_socket.send(bytes(client_message, "utf-8"))