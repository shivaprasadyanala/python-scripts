import os
from cassandra.cluster import Cluster

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

cluster = Cluster(['cassandra'], port=9042)
session = cluster.connect('store',wait_for_all_pools=False)
session.execute('USE store')
rows = session.execute('SELECT * FROM users')
for row in rows:
    print(row.userid,row.name,row.age)