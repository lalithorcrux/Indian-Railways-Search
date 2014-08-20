fp1=open("final_coming_trains","r")
fp2=open("final_going_trains","r")
wp=open("sql_commands","w")
d=fp1.readlines()
q="INSERT INTO RAJDHANI(Tno,"
values=""
count =0
for line in d:
	if(line[0] >= '0' and line[0] <='9'):
		if(count > 0):
			q=q[:-1]
			values=values[:-1]
			wp.write(q+") "+"VALUES "+"("+values+");\n")
			q="INSERT INTO RAJDHANI(Tno,"
			values=""
		count =1
		line=line[:-1]
#		print line
		values=values+"'"+str(line)+"'"+","
#		print values
	else:
	 	ss=line.split()
	 	station=ss[0]
	 	time=ss[1]
	 	q=q+str(station)+","
	 	values=values+"'"+str(time)+"'"+","
	
d=fp2.readlines()
q="INSERT INTO RAJDHANI(Tno,"
values=""
count =0
for line in d:
	if(line[0] >= '0' and line[0] <='9'):
		if(count > 0):
			q=q[:-1]
			values=values[:-1]
			wp.write(q+") "+"VALUES "+"("+values+");\n")
			q="INSERT INTO RAJDHANI(Tno,"
			values=""
		count =1
		line=line[:-1]
#		print line
		values=values+"'"+str(line)+"'"+","
#		print values
	else:
	 	ss=line.split()
	 	station=ss[0]
	 	time=ss[1]
	 	q=q+str(station)+","
	 	values=values+"'"+str(time)+"'"+","
	 


		
		

