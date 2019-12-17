import socket
from time import sleep 
import sys
# -*- coding: utf-8 -*-

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

def largo(entrada):
	if len(entrada)>=5:
		largo=5+len(entrada)
		salida='000'+str(largo)+'opcio'+entrada
	else:
		largo=5+len(entrada)
		salida='0000'+str(largo)+'opcio'+entrada
	return salida

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
numero_opciones=sys.argv[1]
#for x in range(numero_opciones):
#	opciones_votacion=raw_input('ingrese opciones ')
#	s.send(largo(opciones_votacion).encode())
 	
#s.send(largo('1blanco').encode())
#data = ''
#data = s.recv(5000).decode()
#sleep(2)
#s.send(largo('2nulo').encode())
#data = ''
#data = s.recv(5000).decode()
#sleep(2)
opciones_votacion=sys.argv[1] #1opcion
s.send(largo(opciones_votacion).encode()) 
data = s.recv(5000).decode()
print (data)

s.close ()