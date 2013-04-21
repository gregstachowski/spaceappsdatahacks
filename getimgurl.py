#!/usr/bin/python3

# get first sensible[*] image for a given date YYYY-MM-DD from INDEX.TAB
# (INDEX.TAB files list Voyage image data)
# and construct a URL to the BROWSEable JPG 
# [*] by "sensible" we mean GEOMETRICALLY_CORRECTED and not DARK

# horribly ugly, should do a proper search, no time ...

import sys, re, string, time

fileIN = open(sys.argv[1], "r")
indate = sys.argv[2]

line = fileIN.readline()
while re.search(indate, line) is None:
	line = fileIN.readline()

while re.search(indate, line) is not None:
	outline = re.split(',',line)
	if (re.match('^\"GEOMETRICALLY',outline[3]) is not None) and (re.match('^\"DARK',outline[6]) is None):
		subdirs = re.split('/',outline[1])
		print('http://pds-rings.seti.org/volumes/VGISS_5xxx_peer_review'+'/'+re.sub('[" ]','',outline[0])+'/BROWSE/'+subdirs[1]+'/'+re.sub('IMG','JPG',re.sub('[" ]','',outline[2])))
	line = fileIN.readline()
	
fileIN.close()
