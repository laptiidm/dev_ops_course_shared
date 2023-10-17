#!/bin/bash

echo 'Exercise 3: Conditional Statements'
# Prompt the user to enter the file name
echo "enter the name of the file to check:"

#echo "\n" - i can not manage with it ((

# Read the user's input into a variable
read filename

# Check if the file exists in the current directory
if [ -e "$filename" ]; then
    echo "The file $filename exists in the current directory."
else
    echo "The file '$filename' does not exist in the current directory."
fi

#It uses the "-e" test condition to check if the file exists in the current directory/
#i can use or not use the single quotes defining variable`s name ....
