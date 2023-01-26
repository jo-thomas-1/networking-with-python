import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))

message = s.recv(100)
print(message.decode("utf-8"))