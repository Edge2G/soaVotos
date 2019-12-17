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
	return(nombre[10:])

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
	else:
		print(nombre_opcion)
		#if nombre_opcion=='00009opcionulo':
		#	s.send(nombre_opcion.encode())
		n_mat=separar(nombre_opcion)
		v_op=v_opcion(n_mat,'query5_')
		s.send(v_op.encode())
		print(v_op) #v_vot[5:11]
		exito=''
		exito = s.recv(5000).decode()
		print(exito)
		s.send('00007opciook'.encode())
		#print(contrasena)
		#conexion con la base de datos
		# si se ecuentra en la base de datos
		#respuesta='00023autenticarvotacionexito'
		#respuesta='00022autenticarvotacionfallo'
		#s.send(respuesta.encode()) 