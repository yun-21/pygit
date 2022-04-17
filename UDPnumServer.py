#!/usr/bin/python3

import socket

host = ''
port = 13110
BUFF_SIZE=128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address=(host, port)
sock.bind(server_address)

while True:
    print("\nwaiting for request...")
    message, client_address = sock.recvfrom(BUFF_SIZE)

    print("echo request from {} port {}".format(client_address[0],client_address[1]))
    print("echo message:{}".format(message.decode()))
    try:
        if(int(message)%2==0):
            ans="짝수입니다"

        elif(int(message)%2==1):
            ans="홀수입니다"

    except:
        ans="숫자가 아닙니다"

    sock.sendto(ans.encode(),client_address)

sock.close()