#!/bin/bash

# ask the user to enter the filename
echo "enter the filename to read:"
read file_name

# check if the file exists 
if [ -f "$file_name" ]; then
  # File exists, so print its contents
  echo "content >>"
  cat "$file_name"
else
  # an error message
  echo "Error!!! the file '$file_name' does not exist !!!"
fi

