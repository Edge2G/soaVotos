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
		largo=6+len(nvotacion)
		salida='000'+str(largo)+query+nvotacion
	else:
		largo=6+len(nvotacion)
		salida='0000'+str(largo)+query+nvotacion
	return salida		

Bool=True
while (Bool):
	nombre_opcion = s.recv(5000).decode()
	print "Recieved: ", nombre_opcion
	#print(usuario)
	if nombre_opcion== '00007opciono':
		s.send('00007opciook'.encode())
	if nombre_opcion[5:11] =='opcio1':
		msg = v_opcion(separar(nombre_opcion), 'query5')
		print "Sending: ", msg
		s.send(msg.encode())
	if nombre_opcion[5:] == 'queryOK5nopcok':
		#print "asdsadsad"
		msg = '00005opcio'
		print "Sending: ", msg
		s.send(msg.encode())
	if nombre_opcion[5:] == 'queryNk5nopcok':
		msg = '00010opcioERROR'
		print "Sending: ", msg
		s.send(msg.encode())
		