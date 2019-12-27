import socket
from time import sleep 
import sys
# -*- coding: utf-8 -*-

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

def largo(entrada):
	if len(entrada)>=5:
		largo=6+len(entrada)
		salida='000'+str(largo)+'opcio1'+entrada
	else:
		largo=6+len(entrada)
		salida='0000'+str(largo)+'opcio1'+entrada
	return salida

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
opciones_votacion=sys.argv[1] #1opcion
s.send(largo(opciones_votacion).encode()) 
data = s.recv(5000).decode()
print (data)

s.close ()