#!/bin/bash

#Z5.0

echo "Z1"
grep -Po '(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$' $1


echo "Z2"
grep -Po '(([0-9a-fA-F]{1,4}:){7})[0-9A-Fa-f]{1,4}' $1


echo "Z3"
grep -Po '(?<=\s|^)\/\b.[^\s]{1,}' $1