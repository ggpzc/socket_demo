from socket import *

servername='localhost'
serverport=12000

clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((servername,serverport))
sentence=input("input:")
clientSocket.send(sentence.encode())
modifieSentence=clientSocket.recv(1024)
print(modifieSentence.decode())
clientSocket.close()