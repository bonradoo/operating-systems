#!/bin/bash

create_number_statistics () {
	if [[ ! -f "$1" || ! -r "$1" ]]
	then
		echo "Nie mozna odczytac pliku zrodlowego: $1">&2
		exit 1
	fi

	if [[ -f "$2" ]]
	then
		if [[ -w "$2" ]]
		then
			echo "Nie mozna zapisac do pliku docelowego: $2">&2
			exit 1
		fi
	else
		touch "$2" || {
			echo "Nie mozna utworzyc pliku docelowego: $2">&2
			exit 1
		}
	fi

	declare -A numbers

	while read -r line
	do
		IFS=$' \t\n' read -ra fields <<< "$line"
		for field in "${fields[@]}"
		do
			if [[ $field =~ ^[0-9]+$ ]]
			then
        		(( numbers[$field]++ ))
      		fi
		done
	done < "$1"

	sorted_numbers=($(printf '%s\n' "${!numbers[@]}"))
  	for number in "${sorted_numbers[@]}"; do
		echo "$number ${numbers[$number]}" >> "$2"
	done
	sort -t " " -k2 -r -n -o $2 $2

}


create_number_statistics $1 $2