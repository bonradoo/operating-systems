#!/bin/bash

#Z3.0
#1
file $1

#2
wc -l $1

#3
wc -m $1

#4
du -h $1

#5
wc -l <(grep $2 $1)

#6
wc -l <(grep -v $2 $1)

#7
tail -n 1 <(head -n 5 $1)
