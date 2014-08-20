import re
fp=open("v","r")
l=fp.readlines()
a={}	
for line in l:
	line = line.lstrip()
	line = line.rstrip()
	line = line.replace(" ","_")
	if(line in a):
		a[line]=a[line]+1
	else:	
	 	a[line]=1
	
for k in a:
	print k
