import requests
import sys
import time

uri_t = "http://memgator.cs.odu.edu/timemap/json/" 
mementoList = []
plotMementosDict = {}
count = 1
headers = {'user-agent': 'my-app/0.0.1'}
f = open('finally1000URIs.txt','r')
fw = open('MemeFile.txt','w')
fw.write("Count,URI,Mementos")
fw.write('\n')
for line in f:
	if(line == ''):
		pass
	else:	
		response = requests.get(uri_t + line.strip(),headers=headers)
		print("...",response.status_code)
		if(response.status_code == 200):
			memento = response.headers['X-Memento-Count']
			mementoList.append(memento)
		else:
			mementoList.append(0)
		 
			

for value in mementoList:
	if(str(value) in plotMementosDict):
		uriValue = plotMementosDict.get(str(value))
		plotMementosDict[str(value)] = uriValue + 1
	else:
		uriValue = 0
		plotMementosDict[str(value)] = uriValue + 1
	
print("plotMementosDict : ",plotMementosDict)

for mementoValue in plotMementosDict:
	print('{:>8}  {:>8}'.format(str(plotMementosDict[mementoValue]),mementoValue))
	fw.write(str(count)+","+str(plotMementosDict[mementoValue])+","+
	str(mementoValue)) 
	fw.write("\n") 	
	count = count + 1
