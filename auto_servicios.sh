#!/bin/bash

#echo "Iniciando servicio postgres"
#sudo service postgresql start

echo "Iniciando servicio de consultas"
python2 consultas_servicio.py &

echo "Iniciando servicio de conteo"
python2 contar_votos_servicio.py &

echo "Iniciando servicio de autenticacion"
python2 autenticar_servicio.py &

echo "Iniciando servicio de materia"
python2 crear_materia_servicio.py &
python2 crear_opciones_servicio.py &

echo "Iniciando servicio de votacion"
python2 votar_servicio.py &

echo "Iniciando servicio de opciones"
python2 crear_opciones_servicio.py &