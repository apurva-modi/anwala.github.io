import subprocess
from boilerpipe.extract import Extractor
from importlib import reload
import sys
import hashlib
import traceback
import os.path
import time


reload(sys)
sys.getdefaultencoding()

linksDict = {}
linksFile = open('finally1000URIs.txt','r')
for link in linksFile:
	if(link == ''):
		pass
	else:
		try:
			link=link.strip()
			curlCommand = 'curl ' + link
			#link = link.encode('utf-8')
			hash_object = hashlib.md5(link.encode())


			print(hash_object.hexdigest() + '.html')



			htmlFile = os.path.join("sourceHTML_data", hash_object.hexdigest()+ "':html'")
			textFile = os.path.join("sourceTXT_data", hash_object.hexdigest()+ "':txt'")
			#file_to_open = os.path.join(data_folder, "raw_data.txt")

			#htmlFile = hash_object.hexdigest() + ':html'
			#textFile = hash_object.hexdigest() + ':txt'
			
			extractor = Extractor(extractor='ArticleExtractor', url=link)
				#print (str(extractor.getText()))
			
			
			if (len(str(extractor.getText())) > 0):
				#open(htmlFile, "w")
				f = open(htmlFile, "w")
				raw_html = subprocess.call(curlCommand, shell=True, stdout=f)
				#htmlFile.write(str(extractor.getHTML()))
				with open(textFile, 'w') as the_file:
					the_file.write(str(extractor.getText()))
					linksDict[textFile] = link
					print (str(extractor.getText()))
				#linksDict[html] = link
			else:
				print("yes")


		except KeyboardInterrupt:
			exit()		
		except:
			pass


with open('dict-hash-URL.txt', 'w') as file:
	for key,value in linksDict.items():
		file.write('%s:%s\n' % (key, value))



		
		


	

