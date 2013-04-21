#!/usr/bin/python3

# get all Voyager 1 and 2 INDEX.TAB files (each 5,6,7,8 block separately - quick hack)
# glue them together with cat afterwards, also grepping out "UNK" (appear in 6-block
# and the columns are different for tht section ...

# of course this will not be portable to other missions

import sys, re, string, json, time
from subprocess import call

i=201

while (i <= 210):
	#url = 'http://pds-rings.seti.org/volumes/VGISS_5xxx_peer_review/VGISS_5'+str(i)+'/INDEX/INDEX.TAB'
	#url = 'http://pds-rings.seti.org/volumes/VGISS_6'+str(i)+'/INDEX/INDEX.TAB'
	url = 'http://pds-rings.seti.org/volumes/VGISS_8xxx_peer_review/VGISS_8'+str(i)+'/INDEX/INDEX.TAB'
	#print(url)
	call(["wget",url])
	i = i+1
