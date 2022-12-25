#!/bin/bash

#Z8.0

Z80 () {
	if [[ ! -r $1 ]]
	then
		echo 'error, cant read'
		exit -1
	elif [[ ! -f $2 ]]
	then
			echo "creating file $2"
		touch $2
	elif [[ ! -f $3 ]]
	then
		echo "creating file $3"
		touch $3
	elif [[ ! -w $2 ]] | [[ ! -w $3 ]]
	then
		echo "no write permission to $2 or $3"
		exit -1
	fi

	echo -ne '' > $2
	echo -ne '' > $3

	while read -r line
	do
		if (( $((RANDOM%2)) == 0 ))
		then
			echo "$line" >> $2
		else
			echo "$line" >> $3
		fi
	done <$1
}

Z81 () {
	if [[ ! -d $1 ]]
	then
		echo "directory doesnt exist"
		exit -1
	elif [[ ! -w $1 ]]
	then
		echo "no write permission for $1"
		exit -1
	elif [[ ! -r $2 ]]
	then
		echo "no write permission for $2"
		exit -1
	fi

	while read -r line
	do
		mkdir $1/$line
		for ((i=0;i<10;i++))
		do
			touch $1/$line/F$i
		done
	done<$2
}

echo "Z8.0 rozdzielanie pliku do dwoch innych"
Z80 $1 $2 $3

#echo "Z8.1 struktura podkatalogow i plikow"
#Z81 $1 $2
