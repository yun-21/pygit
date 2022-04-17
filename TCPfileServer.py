#!/usr/bin/python3
import socket
host =''
port=13110
BUFF_SIZE=1024
BACKLOG = 5

conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_address = (host,port)

conn_sock.bind((server_address))

conn_sock.listen(BACKLOG)
s='0'
while True:
    print("waiting for requests...")
    data_sock, address = conn_sock.accept()
    print("echo request from {} port {}".format(address[0],address[1]))
    message = data_sock.recv(BUFF_SIZE)
    try:
        fd = open(message.decode(),'r')

        for line in fd:
            data_sock.sendall(line.encode('utf-8'))
        fd.close()
    except:
        ans="파일이 없습니다"
        data_sock.sendall(ans.encode())

    data_sock.close()
conn_sock.close()