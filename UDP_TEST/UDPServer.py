from socket import *
serverPort = 12000
ServerSocked = socket(AF_INET, SOCK_DGRAM)
ServerSocked.bind(('', serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = ServerSocked.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    ServerSocked.sendto(modifiedMessage.encode(), clientAddress)