a={}
fp=open("going-rails","r")
d=fp.readlines()

for k in d:
	s=k.split()
	if(len(s) > 0):
		if(s[0][0] >='0' and s[0][0]<= '9'):
			continue
		if("(Dep)" in s):
			s.remove("(Dep)")
		if("(Arr)" in s):
			s.remove("(Arr)")
		while (s[-1:][0] <= '9' and s[-1:][0] >='0'  ):
			s.pop()
		for kk in s:
			print kk,
		print	


				

			
		  

