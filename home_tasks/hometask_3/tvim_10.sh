#!/bin/bash

# !!!
# the script will only work if the necessary tool is installed on the system
# "sudo apt-get install inotify-tools"
# !!!

# we specify directory for monitoring for any user
watch_dir="$HOME/watch"

# then we create monitoring directory if it does not exist
if [ ! -e "$HOME/watch" ]; then
	mkdir -p "$watch_dir"
fi

# there we create func that handle new files in monitoring directory
# with local variable
process_new_file() {
	local new_file="$1"
# display file content
	echo "content >>"
	cat "$new_file"
# rename file by adding .back extension
	mv "$new_file" "$new_file.back"
}

# directory tracking to watch for new files
# read names of these files
# to give this names into function
inotifywait -m -e create --format "%f" "$watch_dir" | while read -r new_file
	do
	full_path="$watch_dir/$new_file"

# if our file is just simple file >> run function
if [ -f "$full_path" ]; then
	process_new_file "$full_path"
fi
done














