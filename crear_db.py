import subprocess
#------------------- CREAR TABLAS --------------------------
#crearuser = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "CREATE TABLE Usuario ( ID SERIAL PRIMARY KEY NOT NULL, Nombre VARCHAR(20),Contra VARCHAR(20));"'
#subprocess.call(crearuser,shell=True)
#crearest = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "CREATE TABLE Estado ( ID_usuario Integer, ID_votacion Integer);"'
#subprocess.call(crearest,shell=True)
#crearvotac = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "CREATE TABLE Votacion ( ID SERIAL PRIMARY KEY NOT NULL, nombre VARCHAR(20),Fecha_v TIMESTAMP);"'
#subprocess.call(crearvotac,shell=True)
#crearvota = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "CREATE TABLE Voto ( Fecha_v TIMESTAMP ,ID_votacion Integer,ID_opcion Integer);"'
#subprocess.call(crearvota,shell=True)
#crearop = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "CREATE TABLE Opcion ( id_op Integer,ID_votacion Integer,opcion VARCHAR(20) );"'
#subprocess.call(crearop,shell=True)
#--------------------- INSERTAR INFORMACION-------------------------------
a = ["'admin'","'informatica'"]
b = ["'admin'","'degenerado1'","'ACAB'"]
c = ["'informatica'","'industrial'","'obras'"]
e = ["'V_paro'","'V_paro'","'V_paro'"]
f = ["1","2","3"]
g = ["1","2","3"]
h = "'FUnar a Karol'"
m="holi"
j= "'"+m+"'"
#insadm1 = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "INSERT INTO Usuario (Nombre,Contra) VALUES ('+a[0]+','+a[1]+');"'
#subprocess.call(insadm1,shell=True)
#insadm2 = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "INSERT INTO Usuario (Nombre, contrasena,carrera) VALUES ('+a[1]+','+b[1]+','+c[1]+');"'
#subprocess.call(insadm2,shell=True)
#insvot1 = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "INSERT INTO Votacion (nombre,Fecha_v) VALUES ('+h+',current_timestamp);"'
#subprocess.call(insvot1,shell=True)
#insvo = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "INSERT INTO Voto (Fecha_v,ID_votacion,ID_opcion) VALUES (current_timestamp,5,1);"'
#subprocess.call(insvo,shell=True)
#----------------------- QUERIES A TABLAS --------------------------------
#select1 = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "SELECT * From Usuario"'
#subprocess.call(select1,shell=True)
#select2 = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "SELECT * From Estado"'
#subprocess.call(select2,shell=True)'''
#select3 = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "SELECT * From Votacion"'
#subprocess.call(select3,shell=True)
#select4 = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "SELECT * From Voto "'
#subprocess.call(select4,shell=True)
#select5 = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "SELECT * From Opcion "'
#subprocess.call(select5,shell=True)
#select7 = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "SELECT Nombre From Usuario WHERE Nombre='+j+'"'
#subprocess.call(select7,shell=True)
#select9 = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "SELECT nombre,COUNT(ID_opcion),ID_opcion From Votacion INNER JOIN Voto on ID_votacion=ID WHERE ID_votacion=(SELECT ID From Votacion ORDER BY ID DESC LIMIT 1) GROUP BY votacion.nombre, ID_opcion ORDER BY COUNT(ID_opcion) DESC"'
#subprocess.call(select9,shell=True)
#select10 = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "SELECT ID From Votacion ORDER BY ID DESC LIMIT 1"'
#subprocess.call(select10,shell=True)
#----------------------ELIMINAR TABLAS ---------------------------------------
'''deluser = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "DROP TABLE IF EXISTS Usuario;"'
subprocess.call(deluser,shell=True)
delest = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "DROP TABLE IF EXISTS Estado;"'
subprocess.call(delest,shell=True)
delvotac = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "DROP TABLE IF EXISTS Votacion;"'
subprocess.call(delvotac,shell=True)
delvot = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "DROP TABLE IF EXISTS Voto;"'
subprocess.call(delvot,shell=True)
delop = 'PGPASSWORD=informatica psql -U informatica -d postgres -c "DROP TABLE IF EXISTS Opcion;"'
subprocess.call(delop,shell=True)'''
print("operacion exitosa")

#ALTER TABLE table_name
#ALTER COLUMN column_name [SET DATA] TYPE new_data_type;


