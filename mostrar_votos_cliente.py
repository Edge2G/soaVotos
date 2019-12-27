import socket
import sys


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

trans = '00009covotVIEW'
#print "Sending: ", trans
s.send(trans.encode())

resp = s.recv(5000).decode()
print resp
#print "Recieved: ", resp
#data = decode_vote_results(resp)
#print(data)


s.close () 