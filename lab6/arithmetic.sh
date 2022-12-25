#!/bin/bash
#Z6

Z60 () {
	let top=$1+$2
	let bot=$1-$2
	if [ $bot -eq 0 ]
	then
		echo 'Mianownik nie moze byc rowny 0'
		exit -1
	fi
	let res=$top/$bot
	echo $res
}

Z61 () {
	if [ $# -eq 2 ]
	then
		let m=$1
		let b=$2
		if [ $b -lt $m ]
		then
			let m=$b
		fi
		while [ $m -ne 0 ]
		do
			let x=`expr $1%$m`
			let y=`expr $2%$m`
		
			if [ $x -eq 0 -a $y -eq 0 ]
			then
				echo $m
				break
			fi
			m=`expr $m - 1`
		done
	else
		echo 'Niewlasciwa liczba argumentow'
		exit -1
	fi

}

Z62 () {
	if [ $# -eq 2 ]
	then
		let a=$1
		let b=$2
		while [ $a -ne $b ]
		do
			if [ $a -lt $b ]
			then
				let b=$b-$a
			else
				let a=$a-$b
			fi
		done
		echo $a
	else
		echo 'Niewlasciwa liczba argumentow'
		exit -1
	fi
}

Z63 () {
	for i do
		sum=$(expr $sum + $i)
	done
	echo $sum
}
<<a
echo 'Z6.0 Dzielenie'
Z60 $1 $2
echo
a

<<b
echo 'Z6.1 Rek NWD'
Z61 $1 $2
echo
b

<<c
echo 'Z6.2 Ite NWD'
Z62 $1 $2
echo
c

<<d
echo 'Z6.3 Suma argumentow'
Z63 $@
d