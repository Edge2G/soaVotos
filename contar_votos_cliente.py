import socket
import sys

def decode_vote_results(msg):
    msg = msg[12:]

    primera_fila = True
    vote_name = ""
    results = {}
    opcion = ""
    valor = ""

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(0, len(msg)):
        #print i, " ", msg[i]
        if msg[i] == ' ' or msg[i] == '|' or msg[i] == '':
            continue
        if msg[i] == '\n':
            if primera_fila == True:
                vote_name = opcion
                primera_fila = False
                continue
            else:
                results[opcion] = valor
                opcion = ""
                valor = ""
                continue
        if msg[i] in numbers:
            valor = valor + str(msg[i])
            continue
        else:
            opcion = opcion + str(msg[i])
            continue

    return vote_name, results

def code_msg(msg):
    n = len(msg) + 5

    if n < 10:
        return "0000" + str(n) + "covot" + msg
    if n >= 10:
        return "000" + str(n) + "covot" + msg


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

trans = '00009covotCALL'
#print "Sending: ", trans
s.send(trans.encode())

resp = s.recv(5000).decode()
print resp
#print "Recieved: ", resp
#data = decode_vote_results(resp)
#print(data)


s.close () 