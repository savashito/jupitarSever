import socket

UDP_IP = "192.168.0.236" #"192.180.180.119"
UDP_PORT = 8080
msg = "bark"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
    data, addr = sock.recvfrom(1280*720*3)
    print "msg "+str(len(data))
    print "addr "+str(addr)
    

'''
from socket import *
import sys
import select
address = ('localhost', 6005)
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(address)

while(1):
    print "Listening"
    recv_data, addr = server_socket.recvfrom(2048)
    print recv_data
    if recv_data == "Request 1" :
        print "Received request 1"
        server_socket.sendto("Response 1", address)
    elif recv_data == "Request 2" :
        print "Received request 2"
        data = "Response 2"
        server_socket.sendto(data, address)
'''
