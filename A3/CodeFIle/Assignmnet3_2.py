#from __future__ import division
import subprocess
import math
import traceback

grep = "grep -Ric 'Crypto' sourceTXT_data > grepCMD_Output.txt"
subprocess.call(grep, shell=True)
count=0
num_words = 0
matchCount= round(0,4) 
corpusCount=round(0,4)
docsWithTerm =round(0,4)
idf=round(0,4) 
tf=round(0,4) 
tfidf=round(0,4)
totalWordsInFile = round(0,4)
tfDict = {}
def countWordsInFile(fileName):
	global num_words
	with open(fileName, 'r') as f:
		for line in f:
			words = line.split()
			num_words += len(words)
	return num_words
	
linksInFile = open('grepCMD_Output.txt','r')
for line in linksInFile:
	line = line.replace('\n', '')
	
	if("':txt'" in line):
		matchCount = round(int(line[(line.rfind("':txt'")+7):]),4)
		corpusCount = corpusCount + 1
		if(matchCount >= 1):
			print(line)
			line  = line[0:line.rfind("':txt'")]
			print (line)
			totalWordsInFile = countWordsInFile(line+"':txt'")
			print ('line',line)
			print('Total Words :',totalWordsInFile)
			print ('matchCount',matchCount)
			docsWithTerm = docsWithTerm + 1
			tf = round((matchCount / totalWordsInFile),4)
			if(tf >= 0.00025):
				tfDict[line] = tf
			print('\n')
	else:
		continue	
try:
	idf = round(math.log(round((corpusCount / docsWithTerm),4)) / math.log(2), 4)
	tfidf = round((tf * idf),4) 
except:
	pass

data = dict()
with open('dict-hash-URL.txt','r') as raw_data:
    for item in raw_data:
    	if "':txt'" in item:
    		key,value = item.split("':txt':",1)
    		key = key[key.rfind('/')+1:] 
    		data[key]=value
    		#print(key)
    	else:
    		pass
 
with open('tfIdf_File.txt','w') as tfIdf_File: 
	tfIdf_File.write('TFIDF    TF    	IDF    	    		URL'+'\n')
	tfIdf_File.write('-----    --    	---    	    		---'+'\n')
	
	for key, value in tfDict.items(): 

		key = key[key.rfind('/')+1:] 
		#print("**************")
		#print(key)
		tfIdfValue = round((float(value) *idf),4)
		tfValue,url = value,data[key]
		#url = data[key]
	
		tfIdf_File.write(str(tfIdfValue)+'   '+str(tfValue)+'   '+str(idf)+'   '+url)
	
