#!/bin/bash

#Z4.0

#Z1
mkdir -p $2

#Z2
echo "Z2"
find $1 -type f -name "*.txt"

#Z3
echo "Z3"
find $1 -type d -iname "[AaBb]*"

#Z4
echo "Z4"
find $1 -type f -iname "*.sh" -executable

#Z5
echo "Z5"
find $1 -type f -empty -user student

#Z6
echo "Z6"
find $1 -type l

#Z7
echo "Z7"
find $1 -type f -group student -size -1M

#Z8
echo "Z8"
find $1 -type f -executable -perm /2000 -o -executable -perm /4000

#Z9
echo "Z9"
find $1 -type d -perm /1000

#Z10
echo "Z10"
find $1 -type f -mmin -60

#Z11
echo "Z11"
find /dev -type b -or -type c

#Z12
echo "Z12"
find $1 -type d -empty -exec rmdir {} ';'

#Z13
echo "Z13"
find $1 -type f -size +10M -exec mv {} $2 ';'

#Z14
echo "Z14"
find $1 -type d -name "Z*" -exec cp -R {} $2 ';'