

xrdb -merge "$HOME/.Xresources"
xcompmgr -cfF -t-15 -l-15 -r10 -D2 -I0.01 -O0.01 &
xset m 3 0
pulseaudio --check || pulseaudio --start &
#sxhkd & exec bspwm
exec openbox-session
