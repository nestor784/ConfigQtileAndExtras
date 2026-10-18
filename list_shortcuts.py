#!/usr/bin/python
import os
import sys
import subprocess

def chunks(array, size_chunk):
    for i in range(0,len(array),size_chunk):
        yield array[i:i+size_chunk]

def translate(text):
    text_translated ={
            "Print":" ",
            "mod4":"󰘳 ",
            "control":"󰘴 ",
            "Backspace":"󰌍 ",
            "shift":"󰘲 ",
            "Tab":"󰌒 ",
            "Return":"󰌑 ",
            "space":"󱁐 ",
            "F1":"󱊫",
            "F2":"󱊬",
            "F3":"󱊭",
            "F4":"󱊮",
            "F5":"󱊯",
            "F6":"󱊰",
            "F7":"󱊱",
            "F8":"󱊲",
            "F9":"󱊳",
            "F10":"󱊴",
            "XF86AudioRaiseVolume":"󰝝",
            "XF86AudioLowerVolume":"󰝞",
            "XF86MonBrightnessUp":"󰃠 ",
            "XF86MonBrightnessDown":"󰃞 ",
            } 
    if not text in text_translated:
        return text
    return text_translated[text]

def list_shortcuts():
    sys.path.insert(0,"/home/nestor784/.config/qtile/")

    from core.keys import Keys
    kb = Keys()
    keys = kb.keymappings()
    kb_chunks = list(chunks(keys,40))
    pretty_chunks = []
    for chunk in kb_chunks:
        kb_map = ""
        for key in chunk:
            mod = "".join([translate(u) for u in  key.modifiers])
            if not  mod == "":
                mod = f"{mod}"
            info = key.desc
            line=f"{mod}{translate(key.key)}\t{info}" 
            kb_map=f"{kb_map}\n{line}"
        pretty_chunks.append(kb_map)
    return pretty_chunks

def show_shortcuts():
    run = os.path.expanduser("~/.config/qtile/scripts/show_shortcuts.sh")
    chunks = list_shortcuts()
    for text in chunks:
        subprocess.call(['dunstify','--appname','Shortcuts',text,'-u','NORMAL','-t','60000'])

#list_shortcuts()
show_shortcuts()
