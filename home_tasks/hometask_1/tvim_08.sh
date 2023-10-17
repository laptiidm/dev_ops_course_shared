#!/bin/bash

# create an array with fruits
fruits=("Apple" "Pear" "Banana" "Orange" "Grapes")

# iterate through the array and print each fruit on a separate line
echo "List of fruits:"
for fruit in "${fruits[@]}"; do
  echo "$fruit"
done

