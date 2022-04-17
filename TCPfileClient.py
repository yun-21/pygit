import socket
host ='127.0.0.1'
port=13110
BUFF_SIZE=1024


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
print("connectiong to {} port {}".format(server_address[0], server_address[1]))
sock.connect((server_address))
message = input("file 이름 적으세요: ")
message = bytes(message, encoding='utf-8')
sock.sendall(message)
data = sock.recv(BUFF_SIZE)
try:
    fd = open(message.decode(), 'w')
    while data:
        fd.write(data.decode())
        print("파일 내용:{}".format(data.decode()))
        data = sock.recv(BUFF_SIZE)


except Exception as e:
    print("Exception: {} ".format(str(e)))
