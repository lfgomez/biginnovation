#!/bin/bash

#Programa para monitoramento da temperatura do processador usando GNU/Linux (protótipo de daemon de monitoramento)
#Desenvolvido para o Hackathon Inmetrics 2015
#Responsável: Luis Fernando G Gonzalez (luis.gonzalez@inmetrics.com.br)
#Equipe: Big Inovation

#Esse script necessita do programa sensor, disponível no pacote lm-sensores

#Variaveis
nucleos=0
Header1="AAA1"
Tail1="AAA2"
ID="2"
Type="2"
h=1
t=1

#Determinando quantos sensores de temperatura a máquina possui no processador (geralmente um para cada núcleo físico)
nucleos=`sensors | grep "Core" | sed 's/.*:\s*+\(.*\)°C .*(.*/\1/' | wc -l`

#Criando pacote de dados
echo $Header1 >> cputemp.dat
echo $ID >> cputemp.dat
echo $Type >> cputemp.dat
echo $nucleos >> cputemp.dat
for i in `seq 1 $nucleos`;
			  do
			    echo `sensors | grep "Core" | sed 's/.*:\s*+\(.*\)°C .*(.*/\1/' | head -$i | tail -$t` >> cputemp.dat  #Lendo os valores de temperatura
			    if [ $i -gt 1 ]; then let t=t+1; fi
			  done
echo $Tail1 >> cputemp.dat