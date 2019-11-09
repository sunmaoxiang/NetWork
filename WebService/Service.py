from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)  # use IPv4 and TCP connect

# Prepare a server socket

#Fill in start
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1000)
#Fill in end

while True:
    # Establish the connection
    print("Ready to serve")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        print(message)
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(header.encode())
        for i in outputdata:
            connectionSocket.send(i.encode())
        connectionSocket.close()
    except IOError:  # can't find this file then response 404 page
        header = 'HTTP/1.1 404 Found'
        print(header)
        connectionSocket.send(header.encode())
        connectionSocket.close()
serverSocket.close()