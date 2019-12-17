import socket
from time import sleep
import subprocess

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

def opcion(valor):
	valor_opcion=valor[10]
	return valor_opcion
def v_voto(opcion,votac,query):
	if len(opcion+votac+query)>=10:
		largo=6+len(opcion)+len(votac)
		salida='000'+str(largo)+query+opcion+votac
	else:
		largo=6+len(opcion+votac)
		salida='0000'+str(largo)+query+opcion+votac
	return salida	

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))
s.send('00010sinitvotos'.encode())
bus_response = ''
bus_response = s.recv(5000).decode()
print (bus_response)


Bool=True
while (Bool):
	voto = s.recv(5000).decode()
	print(voto)
	if voto== None:
		sleep(10)
	if voto== '00006votos9':
		s.send('00007votosok'.encode())
		s.close()
		Bool=False
	else:		
		p=opcion(voto)
		s.send('00006query4'.encode())
		votac=''
		votac = s.recv(5000).decode()
		print(votac) #00009queryOK23
		v_ins=v_voto(p,votac[13:],'query3')
		print(v_ins)
		s.send(v_ins.encode())
		exito=''
		exito = s.recv(5000).decode()
		print(exito)
		s.send('00007votosok'.encode())
		
