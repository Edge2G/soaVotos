import socket
import sys

def code_msg(msg):
    n = len(msg) + 5

    if n < 10:
        return "0000" + str(n) + "autclb" + msg
    if n >= 10:
        return "000" + str(n) + "autclb" + msg


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#args = sys.argv[1]
#trans = '00005getsv'
#trans = code_msg(args)
usuario= sys.argv[1]
contrasena=sys.argv[2]
msj=usuario+'$'+contrasena
trans = code_msg(msj)
s.send(trans.encode())
resp = s.recv(5000).decode()
print resp


s.close () 