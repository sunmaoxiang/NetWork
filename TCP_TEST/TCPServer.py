from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)  # 1 is the most number of connect.
print("the server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    print(addr)           # print the addr of socket sender, is the different from UDP.
    # UDP is recv message directly, but TCP is recv socket instead.
    # this make it more safe
    sentence = connectionSocket.recv(1024).decode()
    res = sentence.upper()
    connectionSocket.send(res.encode())
connectionSocket.close()