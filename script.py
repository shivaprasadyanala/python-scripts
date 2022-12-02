import os
import mysql.connector

#creating connection
conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='pyscripts',port='3000')

cur = conn.cursor()

#create table dirs
# CREATE TABLE Dirs (
#     Personid int NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     Dirs varchar(255) NOT NULL
#     PRIMARY KEY (Personid)
# );

path = 'D:/study files/python'
dirs = os.listdir(path)
mydirs = []
for d in dirs:
	if os.path.isdir(os.path.join(path,d)):
		mydirs.append(d);
# d = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
# print(d)
print(mydirs)
# file = open('directory_list.txt', 'w') #write to file
# file.write('list of directories in:'+path) 
# for d in mydirs:
#      file.write(d+"\n")
# file.close() #close file
for d in mydirs:
	print(d)
	cur.execute("insert into dirs(dirs) values(%s)",(d,));

conn.commit();
