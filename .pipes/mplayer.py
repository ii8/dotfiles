#!/usr/bin/python

#How to make work:
# depends on files.py
# make sure you create fifo /tmp/mplayer-control in autostart

import os
from sys import argv

home = os.environ['HOME']
def play(what):
	return 'bash -c \'mplayer -slave -input file=/tmp/mplayer-control -ao pulse -playlist &lt;(find "'+home+'/Music/'+what+'" -iregex ".*\.\(m4a\|mp3\)" -type f | sort)\''

def cmd(name, wat):
	return '<item label="'+name+'"><action name="execute"><command>bash -c \'echo "'+wat+'" &gt; /tmp/mplayer-control\'</command></action></item>'

def menu():
	print('<openbox_pipe_menu>')
	print('<menu execute="'+home+'/.pipes/files.py '+home+'/Music" id="mplayer-play" label="Play"/>')
	print('<menu execute="'+home+'/.pipes/mplayer.py list" id="mplayer-playlist" label="Playlist"/>')

	print(cmd('Pause', 'pause'))
	print(cmd('Stop', 'stop'))
	print(cmd('Next', 'pt_step 1'))
	print(cmd('Prev', 'pt_step -1'))
	#print(cmd('Louder', 'volume 5'))
	#print(cmd('Quieter', 'volume -5'))
	print(cmd('Faster', 'speed_incr 0.05'))
	print(cmd('Slower', 'speed_incr -0.05'))

	print('</openbox_pipe_menu>')

def playlist():
	print('<openbox_pipe_menu>')

	ls = os.listdir(home+'/Music')
	for lol in ls:
		if os.path.isdir(home+'/Music/'+lol):
			print('<item label="'+lol+'"><action name="execute"><command>'+play(lol)+'</command></action></item>')

	print('</openbox_pipe_menu>')

if len(argv) > 1:
	playlist()
else:
	menu()

