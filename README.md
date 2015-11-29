#Software Desenvolvido para o Hackathon Inmetrics-Fiap 2015
#Equipe: Big Inovation

IoT Device prototype

Low level data format:

Fixed Header

32 bits ID

32 bits Type

Number Of Variables

Data_0

Data_1

Data_2

Data_n

Fixed Header

Method to analyse in the server:

Ignore the headers, get the ID as a File name, appending data, and Type as a Folder.
Include a Linux time stamp on the saved package.
