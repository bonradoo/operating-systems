#!/bin/bash
#Z7

Z70 () {
	tab=("$@")
	for ((i=0;i<$#;i++))
	do
		for ((j=0;j<$#-1-$i;j++))
		do
			if [ ${tab[j]} -gt ${tab[$((j+1))]} ]
			then
				let temp=${tab[j]}
				let tab[$j]=${tab[$((j+1))]}
				let tab[$((j+1))]=$temp
			fi
		done
	done
	echo ${tab[*]}
}

Z71 () {
	if [ $# -ne 2 ] || (($1<0)) || (($2<0))
	then
		echo 'Incorrect arguments'
		exit -1
	fi
	declare -A arr
	rows=$1
	cols=$2

	for ((i=1;i<=rows;i++))
	do
		for ((j=1;j<=cols;j++))
		do
			let arr[$i,$j]=$i*$j
		done
	done

	for ((j=1;j<=cols;j++))
	do
		for ((i=1;i<=rows;i++))
		do
			printf "%5s" ${arr[$i,$j]}
		done
		echo
	done

}

Z72 () {
	tab=("$@")
	cal=0

	for ((i=0;i<$#-1;i++))
	do
		a=${tab[i]}
		b=${tab[i+1]}
		sum=$a+$b
		wyn=($sum)/2
		cal=$cal+$wyn
	done
	echo $cal | bc -l
}

echo 'Z7.0'
Z70 $@

echo 'Z7.1'
Z71 $1 $2

echo 'Z7.2'
Z72 $@