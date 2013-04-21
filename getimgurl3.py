#!/usr/bin/python3

# INDEX.TAB files list Voyage image data
# construct a URL to the BROWSEable JPG  for sensible[*] images 
# and create a list of [DATE, URL]
# [*] by "sensible" we mean GEOMETRICALLY_CORRECTED and not DARK

# adds TIME and OBJECT name to list

import sys, re, string, time

list_vg1 = []
list_vg2 = []

fileIN = open(sys.argv[1], "r")

line = fileIN.readline()
while line:
	outline = re.split(',',line)
	if (re.match('^\"GEOMETRICALLY',outline[3]) is not None) and (re.match('^\"DARK',outline[6]) is None):
		subdirs = re.split('/',outline[1])
		dateform= re.split('T',outline[9])
		subset = re.sub('[" ]','',outline[0])
		block = subset[6]
		vger = subset[7]
		#print(subset, block, vger)
		if int(block) != 6:
			peer = '_peer_review'
		else:	
			peer = ''
		if int(vger) == 2:
			list_vg2.append([re.sub('[" ]','',dateform[0]),re.sub('[" ]','',dateform[1]),re.sub('["| *\"]','',outline[6]),'http://pds-rings.seti.org/volumes/'+subset+peer+'/BROWSE/'+subdirs[1]+'/'+re.sub('IMG','JPG',re.sub('[" ]','',outline[2]))])
			#print(block+peer)
	line = fileIN.readline()
	
fileIN.close()
list_vg2.sort()
print(list_vg2)
