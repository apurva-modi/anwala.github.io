import csv
import math
from astropy.table import Table
import numpy as np

friend_Dict= {}
total_Count = 0
friend_List = []
friend_Count = 0
friend_Mean = 0
friend_Median = 0
friend_SD = 0
count=1
friend_count = 0
def mean():
	global friend_Mean
	friend_Mean = round((total_Count / friend_Count),2)
	return friend_Mean

def median():
	global friend_Median
	
	mid = 0
	friend_List.sort(key=int)

	mid = len(friend_List) / 2
	if(mid == 0):
		friend_Median = friend_List[mid]
	else:
		mid = mid +1	
		friend_Median = friend_List[mid]
	return friend_Median

def SD():
	global friend_SD
	global friend_Mean
	SD_Sum = 0
	for num in friend_List:
		SD_Sum = SD_Sum + ((int(num) - int(friend_Mean)) *  (int(num) - int(friend_Mean)))

	#print('SD_Sum',SD_Sum)

	friend_SD = round(math.sqrt(SD_Sum / friend_Count),2)
	return friend_SD

with open('acnwala-friendscount.csv') as csvfile:
	total_Count = 0
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		if  "FRIENDCOUNT" in row[1]:
			continue
		else:
			friend_List.append(row[1])
			total_Count = total_Count + int(row[1])
			friend_Count = friend_Count + 1
	print (total_Count)

friend_List.sort(key=int)
f = open('fb-Friends.txt','w')
for num in friend_List:
	print (num)
	f.write(str(count)+","+str(num))
	f.write('\n')
	count = count + 1
	friend_count = friend_count + int(num)
f.close()  
	
mean = [str(mean())]
median = [str(median())]
SD = [str(SD())]
tableList = Table([mean, median, SD], names=('MEAN', 'MEDIAN', 'STANDARD DEVIATION'))
print (tableList)
