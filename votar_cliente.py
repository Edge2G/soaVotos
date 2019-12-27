import socket
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

def largo(entrada):
	if len(entrada)>=5:
		largo=5+len(entrada)
		salida='000'+str(largo)+'votos1'+entrada
	else:
		largo=5+len(entrada)
		salida='0000'+str(largo)+'votos1'+entrada
	return salida

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
opcion=sys.argv[1]
s.send(largo(opcion).encode())
#voto='00006votos'+opcion
#s.send(voto.encode())
data = ''
data = s.recv(5000).decode()
print (data)
s.close ()
