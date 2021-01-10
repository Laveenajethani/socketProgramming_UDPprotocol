import socket
import threading as th
count=1
#udp protocol
myp=socket.SOCK_DGRAM
#network family
afn=socket.AF_INET
s=socket.socket(afn,myp)
ip="192.168.43.97"
port=1234
s.bind((ip,port))
def server():
    while True:
        x = s.recvfrom(30)
        data = x[0].decode()
        client_IP = x[1][0]
        client_port = x[1][1]
        print(client_IP +" : "+data)
        #sending reply to client
        reply=input("What reply you want to send to client {}::".format(client_IP))
        myreply=reply.encode()
        s.sendto(myreply,(client_IP,client_port))


x1=th.Thread(target=server)
x2=th.Thread(target=server)

x1.start()
x2.start()
