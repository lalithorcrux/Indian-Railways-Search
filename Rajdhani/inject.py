#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect(host="localhost", # your host, usually localhost
		                     user="santosh", # your username
				                           passwd="linux", # your password
							                         db="rail") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
fp=open("sql_commands","r")
d=fp.readlines()
cur = db.cursor()
for line in d:	
	cur.execute(line);
db.commit()
	

# print all the first cell of all the rows
#for row in cur.fetchall() :
#   print row[0]

