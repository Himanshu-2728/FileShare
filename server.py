import socket
import os 
from function import handleRecClient



print('Hello Welcome to FileShare \nDo you want to share(0) or recieve(1) file')
method = int(input('Enter 0 or 1: '))

if method == 0:
        port = 8080
        host = socket.gethostbyname(socket.gethostname())
        server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        server.bind(('localhost', port ))
        server.listen(1)


        print('Please enter the path of the file you want to share')
        path = input("=> ")
        print(path)

        print(f'Waiting for a client to connect\nPlease enter {host} and {port} into the recivers pc')
        conn , addr = server.accept()
        handleRecClient(conn , addr , path)

elif method == 1:
    host = input('Please enter the host name: ')
    port = int(input('Please enter the port: '))
    client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    client.connect((host, port))
    print('Connected to host')
    fileName = client.recv(1024).decode()
    fileSize = int(client.recv(1024).decode())
    fileData = client.recv(fileSize)
    with open(fileName , 'wb') as file:
        file.write(fileData)


elif method not in [0 , 1]:
    print('Fuck you')





