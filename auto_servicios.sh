#!/bin/bash

echo "Iniciando servicio postgres"
sudo service postgresql start

echo "Iniciando el Bus"
./bus2019 &

echo "Iniciando servicio de consultas"
python2 consultas_servicio.py &

echo "Iniciando servicio de conteo"
python2 contar_votos_servicio.py &