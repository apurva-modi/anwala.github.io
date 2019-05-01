import docclass
from subprocess import check_output
import io


cl = docclass.naivebayes(docclass.getwords)
#remove previous db file

check_output(['rm', 'apurv.db'])


cl.setdb('apurv.db')
docclass.eTrain(cl)

print("*** Testing for SPAM ***")

for i in range(1,11):
		filename = 'Dataset/Testing/spam' + str(i) +'.txt'
  
		with io.open(filename, 'r', encoding='utf-8') as testFile:
			print(filename, cl.classify(testFile.read()))
  
print("*** Testing for NOT A SPAM ***")
for i in range(1,11):
		filename = 'Dataset/Testing/notaspam' + str(i) +'.txt'
  
		with io.open(filename, 'r', encoding='utf-8') as testFile1:
			print(filename, cl.classify(testFile1.read()))