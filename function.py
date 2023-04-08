import os

def handleRecClient(conn , addr , path):
    print('Connected')
    if os.path.exists(path):
        fileName = path.split('/')[-1]
        print(fileName)
        conn.send(str.encode(fileName)) # Sending the name of the file so that a file with the same name can be created in the directory of the user
        print('File name sent')

        fileSize = str(os.lstat(path).st_size).encode()
        conn.send(fileSize) # Sending the size of the file to the client so it can recv it
        print('File size send')

        with open(path , 'rb') as file:
            conn.send(file.read()) # Sending the binaries of the file
            print('File sent')


        
        