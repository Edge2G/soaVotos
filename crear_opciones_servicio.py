import socket
from time import sleep
# -*- coding: utf-8 -*-

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))
s.send('00010sinitopcio'.encode()) 
bus_response = ''
bus_response = s.recv(5000).decode()
print (bus_response)

def separar(nombre):
	return(nombre[11:])

def v_opcion(nvotacion,query):
	if len(nvotacion+query)>=10:
		largo=7+len(nvotacion)
		salida='000'+str(largo)+query+nvotacion
	else:
		largo=7+len(nvotacion)
		salida='0000'+str(largo)+query+nvotacion
	return salida		

Bool=True
while (Bool):
	nombre_opcion = s.recv(5000).decode()
	#print(usuario)
	if nombre_opcion== '00007opciono':
		s.send('00007opciook'.encode())
		s.close()
		Bool=False
	if nombre_opcion[5:11] =='opcio1':
		msg = '00005query5'+separar(nombre_opcion)
		s.send(msg.encode())
	if nombre_opcion[5:] == 'query0k5nopcok':
		msg = '00005opcio1'
		s.send(msg.encode())
	if nombre_opcion[5:] == 'queryNk5nopcok':
		msg = '00005opcioERROR'
		s.send(msg.encode())
		