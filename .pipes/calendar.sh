#!/bin/sh
#you prob need mono font for this to line up

myp=p
function plstopaskin()
{
	cal | sed 's/ *$//' | sed -n $1$myp
}
OLD_IFS="$IFS"
IFS=

echo "<openbox_pipe_menu>"
echo  "<separator label=\""`date +%A\ \ \ \ \ \ \ \ \ %I\:%M\ %p`\"" />"
echo  "<item label=\""`date +%B\ %d,\ %Y`\"" />"
echo  "<separator />"
echo  "<item label=\""`plstopaskin 2`\"" />"
echo  "<item label=\""`plstopaskin 3`\"" />"
echo  "<item label=\""`plstopaskin 4`\"" />"
echo  "<item label=\""`plstopaskin 5`\"" />"
echo  "<item label=\""`plstopaskin 6`\"" />"
echo  "<item label=\""`plstopaskin 7`\"" />"
echo  "<item label=\""`plstopaskin 8`\"" />"
echo "</openbox_pipe_menu>"


IFS="$OLD_IFS"
