#!/bin/bash

# check if the argument is passed
if [ $# -ne 1 ]; then
	echo "using >> <path_to_file>"
	exit 1
fi

# define a variable
file=$1

# check if the file exists
if [ ! -f "$file" ]; then
	echo "'$file' does not exist"
	exit 1
fi

# use the command substitution construction
# assign the result of the command to a variable
# print the value of the variable to standard output
line_count=$(wc -l < "$file")
	echo "number of lines in '$file' : '$line_count'"
exit 0







