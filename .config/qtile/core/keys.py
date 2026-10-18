from libqtile import qtile
from libqtile.config import Key
from libqtile.lazy import lazy

from . import functions as lf

class Keys:
    mod = "mod4"
    terminal = "alacritty"

    def keymappings(self):
        return [
            Key([self.mod], "h", lazy.layout.left(), desc="Move focus to left"),
            Key([self.mod], "l", lazy.layout.right(), desc="Move focus to right"),
            Key([self.mod], "j", lazy.layout.down(), desc="Move focus down"),
            Key([self.mod], "k", lazy.layout.up(), desc="Move focus up"),
            Key([self.mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
            Key([self.mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
            Key([self.mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
            Key([self.mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
            Key([self.mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
            Key([self.mod, "control"], "h", lazy.layout.decrease_ratio(), desc="Grow window to the left"),
            Key([self.mod, "control"], "l", lazy.layout.increase_ratio(), desc="Grow window to the right"),
            Key([self.mod, "control"], "j", lazy.layout.shrink(), desc="Grow window down"),
            Key([self.mod, "control"], "k", lazy.layout.grow(), desc="Grow window up"),
            Key([self.mod], "f", lazy.window.toggle_floating(), desc="Toggle floating window"),
            Key([self.mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
            Key([self.mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
            Key(
                [self.mod, "shift"],
                "Return",
                lazy.layout.toggle_split(),
                desc="Toggle between split and unsplit sides of stack",
            ),
            Key(
                [self.mod, "shift"],
                "Backspace",
                lazy.layout.rotate(),
                desc="Toggle between split and unsplit sides of stack",
            ),
            Key([self.mod], "Return", lazy.spawn(self.terminal), desc="Launch terminal"),
            Key([self.mod], "s" , lf.run_rofi , desc="Launch rofi"),
            Key([self.mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
            Key([self.mod], "w", lazy.window.kill(), desc="Kill focused window"),
            Key([self.mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
            Key([self.mod, "control"], "q", lf.run_powermenu ,desc="Run powermenu"),
            Key([],"XF86Poweroff",lf.run_powermenu,desc="Run powermenu"),
            Key([],"XF86AudioRaiseVolume",lazy.widget["volume"].increase_vol(), desc="Increase volume"),
            Key([],"XF86AudioLowerVolume",lazy.widget["volume"].decrease_vol(), desc="Decrease volume"),
            Key([],"XF86MonBrightnessUp",lf.up_brightness, desc="Increase brightness"),
            Key([],"XF86MonBrightnessDown",lf.down_brightness, desc="Decrease brightness"),
            Key([],"Print",lf.takescreenshot, desc="Take a screenshot"),
            Key([self.mod, "control"],"n",lf.change_xkb_layout, desc="Toggle en-us and latam keyboard"),
        ]

    def init_keyextend(self,i):
        return [
                Key(
                    [self.mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                ),
                Key(
                    [self.mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                ),
            ]


