import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),457))
s.listen(5)
while True:
    msg, address = s.accept();
    print("Connection Established from ",address)
    msg.send(bytes("Thanks",'utf-8'))
    msg.close()