#!/bin/sh
if [[ $1 =~ ^(-t|--text) ]]
then
	text="$2"
fi
dunstify "$text" -u NORMAL -t 60000
