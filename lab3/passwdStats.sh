#!/bin/bash

#Z3.1
#1
mkdir $1

#2
grep "$(whoami)" /etc/passwd

#3
sort -r <(cat /etc/passwd | cut -f 1,6,7 -d ":") -o $1/F1.csv

#4
rev <(cat /etc/passwd | cut -f 7 -d ":") > $1/F2.csv
sort -u $1/F2.csv -o $1/F2.csv
echo "$(rev $1/F2.csv)" > $1/F2.csv

#5
cat /etc/passwd	|cut -f 1 -d ":" | tr [:lower:] [:upper:] > $1/F3.csv

#6
echo "$(grep student /etc/passwd -C 4)" > $1/F4.csv

#7
diff /etc/passwd $1/F4.csv > $1/differences.txt