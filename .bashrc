#
# ~/.bashrc
#
# Uses archey3, pacman, xterm, mplayer

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=yes'
alias cool='cat ~/Downloads/cool'
alias hello='echo hello $USER watsup!'
alias starwars='telnet towel.blinkenlights.nl'
function music() { mplayer -input file=/tmp/mplayer-control $@ -playlist <(find "$HOME/Music/${@: -1}" -iregex ".*\.\(m4a\|mp3\)" -type f | sort); }

alias archey='archey3'
alias pacman-disowned-dirs="comm -23 <(sudo find / \( -path '/dev' -o -path '/sys' -o -path '/run' -o -path '/tmp' -o -path '/mnt' -o -path '/srv' -o -path '/proc' -o -path '/boot' -o -path '/home' -o -path '/root' -o -path '/var/lib/pacman' -o -path '/var/cache/pacman' -o -path '/var/cache/man' -o -path '/var/db/sudo/$USER' -o -path '/lost+found' \) -prune -o -type d -print | sed 's/\([^/]\)$/\1\//' | sort -u) <(pacman -Qlq | sort -u)"
alias pacman-disowned-files="comm -23 <(sudo find / \( -path '/dev' -o -path '/sys' -o -path '/run' -o -path '/tmp' -o -path '/mnt' -o -path '/srv' -o -path '/proc' -o -path '/boot' -o -path '/home' -o -path '/root' -o -path '/var/lib/pacman' -o -path '/var/cache/pacman' -o -path '/var/cache/man' -o -path '/var/db/sudo/$USER' -o -path '/lost+found' \) -prune -o -type f -print | sort -u) <(pacman -Qlq | sort -u)"

alias poweroff='read -p "Sure?" && poweroff'


test 'xterm' == $TERM && ( transset-df -a 0.6; clear) || ( EDITOR=vim; export EDITOR; archey3;)
test $DISPLAY_ARCHEY && ( archey3 -c magenta;)

#PS1='[\u@\h \W]\$ '

PS1='$ '
#espeak -s 150 "Go get a life and stop messing with bash, you noob!"
export XDG_CONFIG_HOME=$HOME/.config
