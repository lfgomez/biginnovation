#!/bin/bash

#Variaveis
n=0
data=0
linha=0
NumVar=0
Header1="AAA1"
Tail1="AAA2"
ID="0000"
Type="0000"

#exec 3<>/dev/tcp/localhost/5000
#for (( ;; ))
#do
netcat -u -l -p 5050 | while read LINE; 
		do 
		    if [ $LINE == $Header1 ] || [ $data -eq 1 ]
        							then
								let data=1
								echo "$n $LINE"
								let linha=linha+1
								if [ $LINE == $Tail1 ]
											then
											let data=0
											let linha=0
											if [ ! -f $Type/$ID ]; then echo "ID/I,Type/I,TimeStamp/I,$DullVar">> $Type/$ID; fi
											echo "$ID,$Type,$timestamp,$variaveis">> $Type/$ID
											timestamp=""
											variaveis=""
											DullVar=""
											fi
								if [ $linha -eq 2 ]
											then
											ID=$LINE
											timestamp=`date +%s`
											fi

								if [ $linha -eq 3 ]
											then
											Type=$LINE
											#echo "$ID  $Type"
											mkdir -p $Type >/dev/null
											#echo $Header1 >> $Type/$ID
											#echo $ID >> $Type/$ID
											#echo $Type >>$Type/$ID
											fi
								if [ $linha -eq 4 ]
											then
											NumVar=$LINE
											for i in `seq 1 $NumVar`;
													    do
														    if [ $i -gt 1 ] 
														    then
														    DullVar+=","
														    fi
														    DullVar+="Var$i/I"
													    done
											fi
											
								if [ $linha -gt 4 ]
											then
											#echo $LINE >> $Type/$ID
											if [ $linha -gt 5 ] 
													    then
													    variaveis+=","
													    fi
											variaveis+=$LINE
											fi
											
								fi
		let n=n+1;
		done
#done