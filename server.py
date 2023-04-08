import socket
import os 
from function import handleRecClient


# Welcome
print('Hello Welcome to FileShare \nDo you want to share(0) or recieve(1) file')
method = int(input('Enter 0 or 1: '))

if method == 0:
        # Creating a server

        port = 8080
        host = socket.gethostbyname(socket.gethostname())
        server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        server.bind((host, port ))
        server.listen(1)

        # Asking for file path 
        print('Please enter the path of the file you want to share')
        path = input("=> ")
        print(path)

        # Waiting until the client connects to the server
        print(f'Waiting for a client to connect\nPlease enter {host} and {port} into the recivers pc')
        conn , addr = server.accept()
        handleRecClient(conn , addr , path)

elif method == 1: # users wants to receive a file
    host = input('Please enter the host name: ')
    port = int(input('Please enter the port: '))
    client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    client.connect((host, port))
    print('Connected to host')

    # receiving some data about the file
    fileName = client.recv(1024).decode()
    fileSize = int(client.recv(1024).decode())
    fileData = client.recv(fileSize)
    with open(fileName , 'wb') as file: # creating the file if not exist
        file.write(fileData) # Writing the bytes


elif method not in [0 , 1]:
    print('Please enter a number either 1 or 0')





