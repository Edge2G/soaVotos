import socket
from time import sleep
# -*- coding: utf-8 -*-

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))
s.send('00010sinitnomma'.encode()) 
bus_response = ''
bus_response = s.recv(5000).decode()
print (bus_response)

def separar(nombre):
	return(nombre[11:])
def v_votacion(nvotacion,query):
	if len(nvotacion+query)>=10:
		largo=7+len(nvotacion)
		salida='000'+str(largo)+query+nvotacion
	else:
		largo=7+len(nvotacion)
		salida='0000'+str(largo)+query+nvotacion
	return salida		

Bool=True
while (Bool):
	nombre_materia = s.recv(5000).decode()
	#print(usuario)
	if nombre_materia== None :#and contrasena == None:
		sleep(10)
	if nombre_materia[5:11]=='nomma1':
		msg= '00005query2'+separar(nombre_materia)
		s.send(msg.encode())

	if nombre_materia =='00010queryOKALL':
		msg = '00005nomma1'
		s.send(msg.encode())
		
