fp=open("coming-rails","r")
d=fp.readlines()
w=open("Shatabdhi Coming Trains ordered ","w")	
count =0
for line in d:
	l=line.split()
	if(len(l)):
		if(l[0][0] >= '0' and l[0][0] <= '9' ):
			count=0
			line=line.lstrip()
			w.write(line)
		else:	
		 	line=line.rstrip()
			line=line.lstrip()
		 	count=count+1
			line=line+"-"+str(count)+"\n"	 
			w.write(line)
