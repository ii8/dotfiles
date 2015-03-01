#!/usr/bin/python

import os

ext = "jpg|png|gif|jpe|jpeg|bmp"
directory = os.environ['HOME']+"/.bg"

def menu(directory):
	dirlist = os.listdir(directory)
	dirlist.sort()
	for name in dirlist:
		path = directory + "/" + name
		if os.path.isdir(path):
			print('<menu id="wallset-' + path + '" label="' + name + '" >')
			menu(path)
			print("</menu>")
		else:
			if ext.find(path.lower().split('.')[-1]) >= 0:
				print('<item label="' + name.split('.')[0] + '"><action name="Execute"><execute>pcmanfm -w  "' + path + '"</execute></action></item>')

print("<openbox_pipe_menu>")

menu(directory)

print("</openbox_pipe_menu>")
