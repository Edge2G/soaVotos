import socket
from time import sleep
import subprocess

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

def separar(valor):
	valor_opcion=valor[11:]
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
	if voto[5:11]== 'votos1':
		msg = '00005query7'+separar(voto)
		s.send(msg.encode())
		
	if voto[5:]== 'queryOK7PASS':
		s.send('00005votos1'.encode())
	if voto[5:]== 'queryNK7PASS':
		s.send('00005votos2'.encode())
