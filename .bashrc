#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='lsd --classify --group-directories-first'
alias lt='ls --tree'
alias la='ls -a'
alias ll='ls -la'
alias neovim='nvim'
alias vim='nvim'
alias cls='clear'
alias grep='grep --color=auto'
alias install='yay -Sy'

export PATH="/home/$USER/bin:$PATH"
#eval "$(starship init bash)"
# Use bash-completion, if available
[[ $PS1 && -f /usr/share/bash-completion/bash_completion ]] && \
    . /usr/share/bash-completion/bash_completion

# Powerline
powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /usr/share/powerline/bindings/bash/powerline.sh

. "$HOME/.local/bin/env"
