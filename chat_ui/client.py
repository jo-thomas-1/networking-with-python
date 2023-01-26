# client.py

import socket
from tkinter import *

# user inteface functions
def send(listbox, entry):
	message = entry.get()
	server_socket.send(bytes(message, "utf-8"))
	listbox.insert('end', "Client :: " + message)
	entry.delete(0, END)

def recieve(listbox):
	message = server_socket.recv(100)
	listbox.insert('end', "Server :: " + message.decode("utf-8"))

# user interface
root = Tk()

entry = Entry()
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack()
send_button = Button(root, text='send', command=lambda: send(listbox, entry))
send_button.pack(side=BOTTOM)
recieve_button = Button(root, text='recieve', command=lambda: recieve(listbox))
recieve_button.pack(side=BOTTOM)

root.title("Client")

# socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

server_socket.connect((HOST_NAME, PORT))

# execute UI
root.mainloop()