import socket
from time import sleep
import subprocess

# funcion para generar la transaccion final
def final_msg(query, service):
    # n es el largo de la transaccion
    # se suma 8 por la palabra 'query' mas 'OK' mas el numero del servicio
    n = len(query) + 8
    serv = ""

    # se define que servicio esta llamando
    if service == '1':
        serv = "query1"
    if service == '2':
        serv = "query2"
    if service == '3':
        serv = "query3"
    if service == '4':
        serv = "query4"
    if service == '5':
        serv = "query5"
    if service == '6':
        serv = "query6"
    if service == '7':
        serv = "query7"

    if n < 10:
        return "0000" + str(n) + serv + query
    if n >= 10 and n < 100:
        return "000" + str(n) + serv + query
    if n >= 100 and n < 1000:
        return "00" + str(n) + serv + query

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

trans = '00010sinitquery'
print "Sending: ", trans
s.send(trans.encode())

resp = s.recv(5000).decode()
print "Recieved: ", resp
print "\n"

while True:
    print "Hearing..."

    resp = s.recv(5000).decode()
    print "Recieved: ", resp

    if resp[5:11] == 'query1': # query de autentificacion
    	autenticacion=resp[11:]
    	print(autenticacion)
    	pos_bs=autenticacion.find(chr(01))
        q_usr=autenticacion[:pos_bs]
        q_pass=autenticacion[pos_bs+1:]
        print(q_usr,q_pass)	
        j= "'"+q_usr+"'"
        l="'"+q_pass+"'"
        select7 = 'PGPASSWORD=postgres psql -U nico -d soa -t -c"SELECT nombre From Usuario WHERE Nombre='+j+' and Contra ='+l+'"'
        a = subprocess.check_output(select7,shell=True)
        print(a)
        if a[1:-2]==q_usr:        				
    		msg = '00005queryALL'
    		print "Sending: ", msg
    		s.send(msg.encode())
    	if a[1:-2]!=q_usr:
    		msg = '00005queryNOL'
    		print "Sending: ", msg
    		s.send(msg.encode())

    if resp[5:11]=='query2': # query de insertar nombre materia
        nom_mat=resp[11:]
        print len(nom_mat), " ", nom_mat
        j= "'"+nom_mat+"'"	
        insvot1 = 'PGPASSWORD=postgres psql -U nico -d soa -t -c"INSERT INTO Votacion (nombre,Fecha_v) VALUES ('+j+',current_timestamp);"'
        subprocess.call(insvot1,shell=True)	
        msg = '00005queryALL'
        s.send(msg.encode())
        print "\n"

    if resp[5:11] == 'query3': # query mostrar resultados
        cmd = 'PGPASSWORD=postgres psql -U nico -d soa -t -c"select opcion.opcion,count(*) from voto,opcion where opcion.id_op=voto.id_opcion and voto.id_votacion=(select max(id_votacion) from voto) group by opcion.opcion;"'
        query_results = str(subprocess.check_output(cmd, shell=True))

        cmd = 'PGPASSWORD=postgres psql -U nico -d soa -t -c"select votacion.nombre from votacion where votacion.id=(select max(id) from votacion);"'
        query_votename = str(subprocess.check_output(cmd, shell=True))

        query = "votename" + query_votename + query_results
        print query

        msg = final_msg(query, '3')
        print "Sending: ", msg
        s.send(msg.encode())
        print "\n"

    if resp[5:11] == 'query4': # query ultima votacion
        cmd =  'PGPASSWORD=postgres psql -U nico -d soa -t -c"SELECT ID From Votacion ORDER BY ID DESC LIMIT 1"'
        query = subprocess.check_output(cmd, shell=True)

        print (query)

        msg = final_msg(str(query[2:-2].decode()), '4')
        print ("Sending: ", msg)
        s.send(msg.encode())
        print ("\n")
 
    if resp[5:11] == 'query5': # query inserta opciones
        data = resp[11:] #data con el nombre de la votacion
        i = "'"+data+"'"
        cmd1 = 'PGPASSWORD=postgres psql -U nico -d soa -t -c "INSERT INTO Opcion ( ID_votacion,opcion ) VALUES ((SELECT ID From Votacion ORDER BY ID DESC LIMIT 1), '+i+' );"'
        query = subprocess.check_output(cmd1, shell=True)

        msg = final_msg('nopcok', '5')
        print ("Sending: ", msg)
        s.send(msg.encode())
        print ("\n")
 
    if resp[5:11] == 'query6':  # query muestra opciones
        cmd = 'PGPASSWORD=postgres psql -U nico -d soa -t -c "select opcion from opcion where ID_VOTACION = (select max(id) from votacion );"'
        query_results = str(subprocess.check_output(cmd, shell=True))

        # query para el nombre de la votacion
        cmd = 'PGPASSWORD=postgres psql -U nico -d soa -t -c "select votacion.nombre from votacion where votacion.id=(select max(id) from votacion);"'
        query_votename = str(subprocess.check_output(cmd, shell=True))

        query = "votename" + query_votename + query_results
        print query

        msg = final_msg(query, '6')
        print "Sending: ", msg
        s.send(msg.encode())
        print "\n"

    if resp[5:11] == 'query7': # query inserta opciones
        data = resp[11:] #data con el nombre de la votacion
        i = "'"+data+"'"
        insvo = 'PGPASSWORD=postgres psql -U nico -d soa -t -c "INSERT INTO Voto (Fecha_v,ID_votacion,ID_opcion) VALUES (current_timestamp,(select max(id) from votacion),select id from from opcion where opcion ='+i+');"'
        subprocess.call(insvo,shell=True)

        msg = final_msg('PASS', '7')
        print ("Sending: ", msg)
        s.send(msg.encode())
        print ("\n")


s.close () 