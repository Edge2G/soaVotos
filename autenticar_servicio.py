import socket

#def clean_msg(msg):


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

trans = '00010sinitautcl'
print "Sending: ", trans
s.send(trans.encode())

resp = s.recv(5000).decode()
print "Recieved: ", resp
print "\n"

while True:
    print "Hearing..."

    resp = s.recv(5000).decode()
    print "Recieved: ", resp

    if resp[5:11] == 'autclb':

        msg = '00005query1'+resp[11:]
        print "Sending: ", msg
        s.send(msg.encode())
        print "\n"

    if resp == '00010queryOKALL':
        msg = '00005autcl1'
        print "Sending: ", msg
        s.send(msg.encode())
        print "\n"

    if resp == '00010queryOKNOL':
        msg = '00005autcl2'
        print "Sending: ", msg
        s.send(msg.encode())
        print "\n"


s.close () 