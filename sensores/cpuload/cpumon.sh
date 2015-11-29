#!/bin/bash

#Programa para monitoramento de Carga em PCs usando GNU/Linux (protótipo de daemon de monitoramento)
#Desenvolvido para o Hackathon Inmetrics 2015
#Responsável: Luis Fernando G Gonzalez (luis.gonzalez@inmetrics.com.br)
#Equipe: Big Inovation

#Esse script necessita do programa mpstat, disponível no pacote sysstat

#Variaveis
idle=0
load=0
Header1="AAA1"
Tail1="AAA2"
ID="1"
Type="1"

#Lendo o valor de Idle usando o mpstat
idle=`mpstat 1 1 | tail -1 | grep -Po 'all.* \K[^ ]+$'`

#Transformando o valor de Idle para Load
#load = `bc -l <<< '100-$idle'`
load=$(echo "100-$idle" | bc)

#load = $(bc <<< "scale=2;100-$idle")

#Criando pacote de dados
echo $Header1 >> cpu.dat
echo $ID >> cpu.dat
echo $Type >> cpu.dat
echo "1" >> cpu.dat
echo $load >> cpu.dat
echo $Tail1 >> cpu.dat