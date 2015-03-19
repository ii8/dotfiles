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
	ret = '<item label="'+name+'">'
	if(wat == 'pause'):
		ret += '<action name="execute"><command>python '+home+'/.pipes/mplayer.py pause</command></action>'

	ret += '<action name="execute"><command>bash -c \'echo "'+wat+'" &gt; /tmp/mplayer-control\'</command></action></item>'
	return ret

def menu():
	print('<openbox_pipe_menu>')
	print('<menu execute="'+home+'/.pipes/files.py '+home+'/Music" id="mplayer-play" label="Play"/>')
	print('<menu execute="'+home+'/.pipes/mplayer.py list" id="mplayer-playlist" label="Playlist"/>')

	if(os.path.isfile('/tmp/mplayer-paused')):
		print(cmd('Play', 'pause'))
	else:
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
	if(argv[1] == 'list'):
		playlist()
	elif(argv[1] == 'pause'):
		if(os.path.isfile('/tmp/mplayer-paused')):
			os.remove('/tmp/mplayer-paused')
		else:
			open('/tmp/mplayer-paused', 'a').close()

else:
	menu()

