from socket import *

servername='localhost'
serverport=12000

clientSocket=socket(AF_INET,SOCK_DGRAM)
message=input("input:")
clientSocket.sendto(message.encode(),(servername,serverport))
modifiedmessage,serverAddress=clientSocket.recvfrom(2048)
print(serverAddress)
print(modifiedmessage.decode())
clientSocket.close()