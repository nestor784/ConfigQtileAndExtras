#!/usr/bin/env bash
## Author : Aditya Shakya (adi1090x)
## Github : @adi1090x
#
## Rofi   : Power Menu
uptime="`uptime -p | sed -e 's/up //g'`"
host="$(uname -n)"
# Options
shutdown=' Shutdown'
reboot='󰜉 Reboot'
lock=' Lock'
suspend=' Suspend'
logout='󰍃 Logout'
yes='Yes'
no='No'

# Rofi CMD
rofi_cmd() {
	rofi -dmenu \
		-theme ~/.config/qtile/scripts/window_style.rasi \
		-p "$host" \
		-mesg "Uptime: $uptime"
}

# Confirmation CMD
confirm_cmd() {
	rofi -dmenu \
		-theme ~/.config/qtile/scripts/window_style.rasi \
		-p 'Confirmation' \
		-mesg 'Are you Sure?' 
}

# Ask for confirmation
confirm_exit() {
	echo -e "$yes\n$no" | confirm_cmd
}

# Pass variables to rofi dmenu
run_rofi() {
	echo -e "$lock\n$suspend\n$logout\n$reboot\n$shutdown" | rofi_cmd
}

# Execute Command
run_cmd() {
	selected="$(confirm_exit)"
	if [[ "$selected" == "$yes" ]]; then
		if [[ $1 == '--shutdown' ]]; then
			systemctl poweroff
		elif [[ $1 == '--reboot' ]]; then
			systemctl reboot
		elif [[ $1 == '--suspend' ]]; then
			amixer set Master mute
			systemctl suspend
		elif [[ $1 == '--logout' ]]; then
			qtile run-cmd qtile cmd-obj -o cmd -f shutdown
		fi
	else
		exit 0
	fi
}

# Actions
chosen="$(run_rofi)"
case ${chosen} in
    $shutdown)
		run_cmd --shutdown
        ;;
    $reboot)
		run_cmd --reboot
        ;;
    $lock)
		if [[ -x '/usr/bin/betterlockscreen' ]]; then
			betterlockscreen -l
		elif [[ -x '/usr/bin/i3lock' ]]; then
			i3lock
		elif [[ -x '/usr/bin/slock' ]]; then
			slock
		fi
        ;;
    $suspend)
		run_cmd --suspend
        ;;
    $logout)
		run_cmd --logout
        ;;
esac
