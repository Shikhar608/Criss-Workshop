import socket

server IP='172.17.29.22'
serverPORT= 6000

serveraddress= (serverIP,serverPORT)
bufferSize= 1024

UDPClientSocket= socket.socket(family=socket.AF_INEt, type=socket.SOCK_DGRAM)
message= 'HI guys I m Shikhar agarwal 2022A3PS0528P'

bytestosend= str.encode(message)

UDPClientSocket.sendto(bytestosend, serveraddress)