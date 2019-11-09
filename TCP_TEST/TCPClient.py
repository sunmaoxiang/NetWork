from socket import *
serverName = '10.211.55.9'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) # IPv4 and tcp
clientSocket.connect((serverName, serverPort))
while True:
    sentence = input('Input lowercase sentence(q for quit)\n')
    if sentence == 'q' :
        break
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())
clientSocket.close()
