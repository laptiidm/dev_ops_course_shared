#!/bin/bash

# check if all validated arguments are passed
if [ $# -ne 3 ]; then
	echo " !the lack of arguments! use >> $0 <name_or_directory> <source_dir> <target_dir>"
	exit 1
fi

# cli-arguments
file_or_dir="$1"
source_dir="$2"
target_dir="$3"

# checking if the file or directory that needs to be copied exists
if [ ! -e "$source_dir/$file_or_dir" ]; then
	echo "file '$file_or_dir' does not exist in '$source_dir' !!!"
	exit 1
fi

# checking if the target directory is exists
if [ ! -e "$target_dir" ]; then
	echo "'$target_dir' does not exist !!!"
	exit 1
fi 

# perform the copy after determining whether we are dealing with a directory or a file
if [ -d "$source_dir/$file_or_dir" ]; then
        cp -r "$source_dir/$file_or_dir" "$target_dir"
else
        cp "$source_dir/$file_or_dir" "$target_dir"
fi








