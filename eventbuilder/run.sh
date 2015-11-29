#!/bin/bash

#Programa para copia e analise de dados usando GNU/Linux (protótipo)
#Desenvolvido para o Hackathon Inmetrics 2015
#Responsável: Luis Fernando G Gonzalez (luis.gonzalez@inmetrics.com.br)
#Equipe: Big Inovation

#watch -n5 cp 001/001 001.csv

cp 001/001 001.csv
rm -rf last-001.csv
head -1 001.csv > last-001.csv
tail -100 001.csv >> last-001.csv
root -l -q teste.c
root -l -q last-teste.c > result.txt
cp *.gif /data/www
cp result.txt /data/www

