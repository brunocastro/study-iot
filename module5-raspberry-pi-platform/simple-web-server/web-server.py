import socket
import sys

mysock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.bind(("",1235))
except socket.error:
    print("Whoops! Something went wrong.")
    sys.exit()
mysock.listen(5)
while True:
    print("Yeah! All right with this connection.")
    myconnection, addr = mysock.accept()
    data = myconnection.recv(1000)
    if not data:
        break
    myconnection.sendall(data)

myconnection.close()
mysock.close()
