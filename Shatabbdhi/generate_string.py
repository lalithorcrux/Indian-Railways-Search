fp=open("Shatabdhi Stations","r")
d=fp.readlines()
string=""
for line in d:
	line=line.rstrip()
	line=line.replace(".","")
	line=line.replace("(","")
	line=line.replace(")","")

	string=string+line+" char(60) default NULL,"

print string	
