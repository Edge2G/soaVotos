import socket

# funcion para generar la transaccion final
def final_msg(query):
    query = query[13:]
    n = len(query) + 5      

    if n < 10:
        return "0000" + str(n) + "covot" + query
    if n >= 10 and n < 100:
        return "000" + str(n) + "covot" + query
    if n >= 100 and n < 1000:
        return "00" + str(n) + "covot" + query

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

trans = '00010sinitcovot'
print "Sending: ", trans
s.send(trans.encode())

resp = s.recv(5000).decode()
print "Recieved: ", resp
print "\n"

while True:
    print "Hearing..."

    resp = s.recv(5000).decode()
    print "Recieved: ", resp

    if resp == '00009covotCALL':
        msg = '00006query3'
        print "Sending: ", msg
        s.send(msg.encode())
        print "\n"

    if resp[5:13] == 'queryOK3':
        msg = final_msg(resp)
        print "Sending: ", msg
        s.send(msg.encode())
        print "\n"

    if resp == '00009covotVIEW':
        msg = '00006query6'
        print "Sending: ", msg
        s.send(msg.encode())
        print "\n"

    if resp[5:13] == 'queryOK6':
        msg = final_msg(resp)
        print "Sending: ", msg
        s.send(msg.encode())
        print "\n"




s.close () 