# Networking With Python

As the name suggests, network refers to handling data, connections and other related aspects on a network.

Python provides two levels of access to network services. At a low level, it can access the basic socket support in the underlying operating system, which allows to implement clients and servers for both connection-oriented and connectionless protocols.

Python also has libraries that provide higher-level access to specific application-level network protocols, such as FTP, HTTP, and so on.

## IP Address

IP stands for "Internet Protocol," which is the set of rules governing the format of data sent via the internet or local network.

IP addresses are the identifier that allows information to be sent between devices on a network. They contain location information and make devices accessible for communication. It is a numerical label assigned to each device connected to a computer network that uses internet protocols for communication. There has been many versions that have been implimented. Currently the versions in use are IPv4 and IPv6.

IPv4 deployed in 1981, is a 32-bit address. It has a capacity of 4.3 buillion address and needs to be reused and masked. It requires DHCP or manual configuration. It has the format `X.X.X.X`. Here 'X' is decimal (positive integer) value that ranges from 0 to 255. Values are separated by a dot '.'. eg: 127.0.0.1

IPv6 deployed in 1998, is a 32-bit address. It has a capacity of 7.9x10^28 address and so every device can have a unique address. It supports automatic configuration. It has the format `X:X:X:X:X:X`. Here 'X' is hexadecimal value that ranges from 0000 to FFFF. Values are separated by a colon ':'. eg: 127.0.0.1

DHCP (Dynamic Host Configuration Protocol) is a network protocol that is used to configure network devices to communicate on an IP network. A DHCP client uses the DHCP protocol to acquire configuration information, such as an IP address, a default route, and one or more DNS server addresses from a DHCP server.

Devices have both public IP and private IP. As the name suggests, public IP is used to share devide address to the outside network and is for use within internal or local network or internal devices. Public IP's are usually used by devices like routers, modems, servers, etc.

## Ping

A ping (Packet Internet or Inter-Network Groper) is a basic Internet program that allows a user to test and verify if a particular destination IP address exists and can accept requests in computer network administration. The acronym was contrived to match the submariners term for the sound of a returned sonar pulse.

To ping to any given address provide the command `pind [address]` in command tool.

eg: `ping 127.0.0.1`

## Domain Name

A domain name is a string that identifies a realm of administrative autonomy, authority or control within the Internet. Domain names are often used to identify services provided through the Internet, such as websites, email services and more. For example, "google.com". As of 2017, 330.6 million domain names had been registered.

Domain names are used to serve memory. It is easier to remember a name than a numerical label. Devices on a network do not undertand this string value. They connect to a DNS (Domain Name Server) that provides the IP address of the nearest server of the required domain and then this IP address is used by the system to connect to the corresponding system.

Ping to a domain name to identify the IP address of the domain. Note that some service providers may use multiple servers at different location to make sure service is available to all without difficulty. In such cases the IP adress shared by the DNS will be of the nearest available server.

For example, for the command `ping google.com`, the system would show test packets send to the IP `142.250.183.238`.

## Port

A port or port number is a number assigned to uniquely identify a connection endpoint and to direct data to a specific service. At the software level, within an operating system, a port is a logical construct that identifies a specific process or a type of network service.

Port numbers are usually given along with the IP address after acolon. In the IP address `127.0.0.1:8002`, 8002 is the port to which user gets connected.

Some common ports are,

- 20 - FTP (File Transfer Protocol) Data Transfer
- 21 - FTP Command Control
- 22 - SSH (Secure Shell) Login
- 23 - Telnet
- 25 - SMTP (Simple Mail Transfer Protocol) Email Routing
- 53 - DNS (Domain Name System)
- 67, 68 - DHCP (Dynamic Host Configuration Protocol)
- 80 - HTTP (Hyper Text Transfer Protocol)
- 110 - POP3 (Post Office Protocol)
- 119 - NNTP (Network News Transfer Protocol)
- 123 - NTP (Network Time Protocol)
- 143 - IMAP (Internet Message Access Protocol)
- 161 - SNMP (Simple Network Management Protocol)
- 194 - IRC (Internet Relay Chat)
- 443 - HTTPS (Hyper Text Transfer Protocol Secure)

## Socket

It is a software structure within a network node of a computer network that serves as an endpoint for sending and receiving data across the network. The structure and properties of a socket are defined by an application programming interface for the networking architecture.

A network socket is one endpoint in a communication flow between two programs running over a network. Sockets are created and used with a set of programming requests or "function calls" sometimes called the Application Programming Interface (API).

Socket address, is IP address along with the port number. eg: `127.0.0.1:8002`.

- for creating a socket in python, `import socket`
- for simulating a socket connection both server and client are required

```
# server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))

s.listen(4)

while True:
	client_address = s.accept()
	print("Client has connected from the address", client_address)
```

```
# client.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))
```

## Example Projects

The following are some sample projects created based on the above documentation.

| # | Name | Action |
|---|---|---|
| 1 | Socket Connection | [Go to code]() |