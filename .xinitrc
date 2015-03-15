

xrdb -merge "$HOME/.config/x/.xresources"
xcompmgr -cfF -t-15 -l-15 -r10 -D2 -I0.01 -O0.01 &
xset m 3 0
xset r rate 200 20
xmodmap "$HOME/.config/x/.xmodmap"

pulseaudio --check || pulseaudio --start &
#sxhkd & exec bspwm
exec openbox-session
