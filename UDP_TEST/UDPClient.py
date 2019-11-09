from socket import *
serverName = '10.211.55.9'    # this is my vm linux hostname
serverPort = 12000            # Port
clientSocked = socket(AF_INET, SOCK_DGRAM) # AF_INET: use IPv4, SOCK_DGRAM: use UDP
while True:
    message = input('Input lowercase sentence(q for quit)\n')
    if message == 'q' :
        break
    clientSocked.sendto(message.encode(), (serverName, serverPort)) # encode: string -> bype 
    modifiedMessage, serverAddress = clientSocked.recvfrom(2048) # modifiedMessage is the ToUpper , 2048 is the lenthgh of cache
    print(modifiedMessage.decode())
clientSocked.close() 