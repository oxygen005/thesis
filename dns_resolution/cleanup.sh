#!/bin/bash

# https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html
if [ ! $# == 2 ]; then
    echo "Usage: $0 massdns.txt output.txt"
    exit
fi

inputfile=$1
outputfile=$2

# https://unix.stackexchange.com
# /questions/76061/can-sed-remove-double-newline-characters
awk {'print $1'} $file | uniq | sed 's/;//g' | sed 's/\.$//' | sed '/^$/d' > $outputfile
