from socket import *
serverport=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverport))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024).decode()
    print(sentence)
    capitalizedSentence=sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()