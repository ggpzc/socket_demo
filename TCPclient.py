
support={
    'windows_terminal': 'Microsoft.WindowsTerminalPreview_1.0.1402.0_8wekyb3d8bbwe.msixbundle'
}



from socket import *
import struct
import json
import os
import sys
import time

servername='59.78.18.73'
serverport=12000
buffersize=1024


clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((servername,serverport))
sentence=input("input:")
clientSocket.send(sentence.encode())

head_struct = clientSocket.recv(4)

head_len = struct.unpack('i', head_struct)[0]                       # 解析出报头的字符串大小
data = clientSocket.recv(head_len)                                  # 接收长度为head_len的报头内容的信息 (包含文件大小,文件名的内容)

head_dir = json.loads(data.decode('utf-8'))
filesize_b = head_dir['filesize']
filename = head_dir['filename']



recv_len = 0
recv_mesg = b''
old = time.time()
f = open(support[filename], 'wb')
while recv_len < filesize_b:                                        # 每次最多传输buffersize长度，最后一次传完整个文件
    if filesize_b - recv_len > buffersize:

        recv_mesg = clientSocket.recv(buffersize)
        f.write(recv_mesg)
        recv_len += len(recv_mesg)
    else:
        recv_mesg = clientSocket.recv(filesize_b - recv_len)
        recv_len += len(recv_mesg)
        f.write(recv_mesg)


    print("{}/{}".format(recv_len,filesize_b))


now=time.time()
stamp=int(now-old)
print("time used: {}".format(stamp))

f.close()

clientSocket.close()