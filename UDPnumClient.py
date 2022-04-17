import socket
host = '127.0.0.1'
port = 13110
BUFF_SIZE = 128
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host, port)
message = input("숫자를 적으세요: ")
message = bytes(message, encoding='utf-8')

try:
    bytes_sent = sock.sendto(message, server_address)
    data, address = sock.recvfrom(BUFF_SIZE)
    print("Rceived from server: {}".format(data.decode()))

except Exception as e:
    print("Exception: {}".format(str(e)))

sock.close()