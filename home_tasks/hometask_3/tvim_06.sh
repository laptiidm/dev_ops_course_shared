#!/bin/bash

# prompt the user to type text
echo "type your text, please:"
read input_sentence

# divide the sentence into words and store them in an array
words=($input_sentence)

# reverse the array of words
reversed_words=()
for ((i=${#words[@]}-1; i>=0; i--)); do
    reversed_words+=("${words[i]}")
done

# combine the inverted words back into a sentence
reversed_sentence="${reversed_words[*]}"

# Выведите перевернутое предложение
echo "your reversed sentence is over here >> '$reversed_sentence'"

