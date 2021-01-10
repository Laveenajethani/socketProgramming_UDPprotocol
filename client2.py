import socket
client_protocol=socket.SOCK_DGRAM
client_address_family=socket.AF_INET
s=socket.socket(client_address_family,client_protocol)
server_IP=input("Enter Server IP: ")
server_port=int(input("Enter Server Port: "))

def client_sender():
    while True:
        data=input("what msg you want to send to server: ")
        mydata=data.encode()
        s.sendto(mydata,(server_IP,server_port))
        x=s.recvfrom(100)
        data=x[0].decode()
        if(data=='okay exit the chat'):
            break
        print(data)

client_sender()
