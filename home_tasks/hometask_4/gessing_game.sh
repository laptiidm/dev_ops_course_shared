#!/bin/bash

# first we generate a random number
# RANDOM - built-in variable that generate random number
secret_number=$((1 + RANDOM % 100))
#echo "'$secret_number'" 
attempt=5

echo "hello"
echo "this script defined a secret number, try to gess it"
echo "guess the secret number - you have '$attempt' attempts" 

while [ $attempt -gt 0 ]; do
	# "read -p" it displays a prompt to the user to enter data
	read -p "try to guess, enter your number >> " user_guess

	# comparison with a pattern, checking for only numbers in user input
	if ! [[ "$user_guess" =~ ^[0-9]+$ ]]; then
	echo "please, enter an integer !!!"
	continue
	fi

	if [ "$user_guess" -eq "$secret_number" ]; then
	echo "congratulations, YOU WIN !!!"
	exit 0
	elif [ "$user_guess" -lt "$secret_number" ]; then
	echo "you fell a little short, dude ))"
	else
	echo "you everdid it, dude"
	fi

	attempt=$((attempt - 1))
	echo "you just have $attempt attempts"
done

echo "sorry, you have no more attempts left"
echo "the secret number was >> $secret_number"

