#!/usr/bin/python3

# very messy conversion of Horizons spacecraft ephemeris file
# to more usable format (exporting date, X and Y only)

import sys, re, string, json, time

fileIN = open(sys.argv[1], "r")

list = []

# data block marked by line containing '$$SOE' at beginning
# and line containing '$$EOE' at end

line = fileIN.readline()
while re.match('^\$\$SOE', line) is None:
	line = fileIN.readline()

line1 = fileIN.readline()
while re.match('^\$\$EOE', line1) is None:
	# read position line
	line2 = re.split(' *',fileIN.readline())
	# parse login here
	#
	dateline = re.split(' *',line1)
	#print(time.strftime('%Y-%m-%d',time.strptime(dateline[3],'%Y-%b-%d')),float(line2[2]),float(line2[3]))
	date = time.strftime('%Y-%m-%d',time.strptime(dateline[3],'%Y-%b-%d'))
	x = float(line2[1])
	y = float(line2[2])
	list.append([date,x,y])
	#
	# read NEXT date line
	line1 = fileIN.readline()
	
fileIN.close()
print(list)
