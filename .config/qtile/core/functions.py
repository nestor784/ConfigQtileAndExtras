import os
import subprocess
from libqtile.lazy import lazy

## Lazy functions
@lazy.function
def run_rofi(qtile):
    run = os.path.expanduser("~/.config/qtile/core/functions/run_rofi.sh")
    subprocess.call([run])

@lazy.function
def run_powermenu(qtile):
    run = os.path.expanduser("~/.config/qtile/core/functions/powermenu.sh")
    subprocess.call([run])

@lazy.function
def takescreenshot(qtile):
    run = os.path.expanduser("~/.config/qtile/core/functions/prtsc.sh")
    subprocess.call([run])

@lazy.function
def run_theme_manager(qtile):
    os.system("exec ~/.config/qtile/scripts/theme_selector")

@lazy.function
def up_brightness(qtile):
    os.system("exec brightnessctl set +10%")

@lazy.function
def down_brightness(qtile):
    os.system("exec brightnessctl set 10%-")

@lazy.function
def change_xkb_layout(qtile):
    os.system("exec ~/.config/qtile/scripts/chlanguage.sh")
