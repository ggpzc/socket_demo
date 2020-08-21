from socket import *
import struct
import os
import configparser
import json


config=configparser.ConfigParser()
config.read("config/tcp.txt")                                   # read default file, which can be modified by config.py


serverport=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverport))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket,addr=serverSocket.accept()
    filename=connectionSocket.recv(1024).decode()

    filepath=config['filepath'][filename]
    filesize=os.path.getsize(filepath)

    filename=filename

    dirc = {
        'filename': filename,
        'filesize': filesize,
    }
    head_info = json.dumps(dirc)
    head_info_len = struct.pack('i', len(head_info))

    connectionSocket.send(head_info_len)
    connectionSocket.send(head_info.encode('utf-8'))

    with open(filepath, 'rb') as f:
        data = f.read()
        connectionSocket.sendall(data)

    connectionSocket.close()