#!/usr/bin/python

import os
import random
import sys
from stat import *

mypath = sys.argv[0]
hidden = 0
term = 'xterm'
fileman = 'pcmanfm'

def getCommand(f):
	ext = f.split('.')[-1]
	ext = ext.lower()
	cmdls = {
		'txt':'leafpad',
		'cfg':'leafpad',
		'conf':'leafpad',
		'mp3':'mplayer -slave -input file=/tmp/mplayer-control -ao pulse',
		'm4a':'mplayer -slave -input file=/tmp/mplayer-control -ao pulse',
		'py' :'geany',
		'c' :'geany',
		'h' :'geany',
		'xcf':'gimp',
		'blend':'blender',
		'obj':'blender',
		'png':'sxiv',
		'jpg':'sxiv',
		'jpeg':'sxiv',
		'bmp':'sxiv',
		'gif':'sxiv'
	}
	if ext in cmdls:
		return cmdls[ext]
	else:
		return 'leafpad'

def ls(dircontent):
	dirs = []
	files = []
	for item in dircontent:
		if os.path.isdir(currentpath + '/' + item):
			dirs.append(item)
		else:
			files.append(item)
	dirs.sort()
	files.sort()
	return dirs, files

def placer(string):
	return string.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '\\\"').replace('&apos;', '\\\'')

def replacer(string):
	return string.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')

def menu(dirs, files):
	curpath = replacer(currentpath)
	print('<openbox_pipe_menu>')

	if len(curpath) > 1:
		print('<menu execute="' + mypath + ' '  + '/ " id="root-' + str(random.randrange(1,999,1)).zfill(2) + '" label="Root"/>')
	if not hidden:
		print('<menu execute="' + mypath + ' \'' + curpath + '/\' hidden' + '" id="hidden-' + str(random.randrange(1,999,1)).zfill(2) + '" label="Hidden"/>')

	print('<item label="Files"><action name="execute"><execute>'+fileman+' "' + curpath + '"</execute></action></item>')
	print('<item label="Shell"><action name="execute"><execute>'+term+' -e "cd ' + curpath + ' &amp;&amp; /bin/bash "</execute></action></item>')
	print('<separator />')

	for thisdir in dirs:
		thisdir = replacer(thisdir)
		menuid = str(random.randrange(1,999,1)).zfill(2)
		print('  <menu execute="' + mypath + ' \'' + curpath + '/' + thisdir + '\'" id="' + thisdir + '-' + menuid + '" label="' + thisdir + '"/>')

	for thisfile in files:
		thisfile = replacer(thisfile)
		print('<item label="' + thisfile + '">')
		print('<action name="execute">')
		print('<command>')
		try:
			if S_IXUSR & os.stat(placer(curpath + '/' + thisfile))[ST_MODE]:
				print(curpath + '/' + thisfile)
			else:
				print(getCommand(thisfile) + ' "' + curpath + '/' + thisfile + '"')
		except OSError:
			print(getCommand(thisfile) + ' "' + curpath + '/' + thisfile + '"')

		print('</command>')
		print('</action>')
		print('</item>')
	print('</openbox_pipe_menu>')

if len(sys.argv) > 1:
	currentpath = ' '.join(sys.argv[1:2])
	if len(sys.argv) > 2:
		hidden = 1
else:
	currentpath = os.environ['HOME']

try:
	if hidden:
		content = [x for x in os.listdir(currentpath) if x[0] == '.']
	else:
		content = [x for x in os.listdir(currentpath) if x[0] != '.']

	if not [x for x in os.listdir(currentpath) if x[0] == '.']:
		hidden = 1#dont show hidden menu option if there are none

	parts = ls(content)
	menu(parts[0], parts[1])
except OSError as e:
	print('<openbox_pipe_menu>')
	print('<separator label="' + e.strerror + '" />')
	print('</openbox_pipe_menu>')
