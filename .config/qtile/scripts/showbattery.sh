#!/usr/bin/env bash

dunstify -u low -t 2000 -a "battery" $(cat /sys/class/power_supply/BAT1/capacity)

