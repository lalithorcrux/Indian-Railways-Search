fp=open("Janshatabdhi_Coming_Trains_Ordered","r")
d=fp.readlines()
wp=open("final_coming_trains","w")	
string=""	
for line in d:
	if(line[0] >= '0' and line[0] <='9'):
		kk=line.split()
		tno=kk[0]
		tno=tno.replace("*","")
		wp.write(tno+"\n")
#		print tno
	else:	
	 	dk=line.split()
	 	if "(Dep)" in dk:
			ind=dk.index("(Dep)")
		if "(Arr)" in dk:	
		 	ind=dk.index("(Arr)")
	 	string=dk[0]
		for i in range(1,ind):
			string=string+" "+str(dk[i])
		string=string.replace(" ","_")
		string=string.replace(".","")
		string=string.replace("(","")
		string=string.replace(")","")
#		print string+" "+dk[ind+1] 
		wp.write(string+" "+dk[ind+1]+"\n") 
		 
			 

