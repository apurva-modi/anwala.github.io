import tweepy
import time
import csv
import math
from astropy.table import Table

#My twitter Account keys
ckey = 'mtDSeNYtJUZkKfspxTFmk7Nn8'
csecret = 'iYg5kksoIQKGsXVwGZ7bYpH0cFlxonNPg9hyhDKdGoP89bic6G'
atoken = '1094978973245812738-msYR1atvDnyfTTO46shWdnp5SIJcAA'
asecret = 'EMdqw7fA4IfkDYzKBqNQfoe5sAwz7dgCcRTWkpZOteUKd'
#Login Verifiavtion 
auth = tweepy.auth.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth,wait_on_rate_limit=True)
if(api.verify_credentials):
    print ('Logged in successfully')

total_count = 0
listDict = {}
twitter_handle='acnwala'
friend_Mean = 0
friend_Median = 0
friend_SD = 0
friend_List = []
count = 1
friend_count = 0


def mean():
    global friend_Mean
    friend_Mean = round((friend_count / total_count),2)
    return friend_Mean


def median():  
    global friend_Median 
    mid = 0 
    friend_List.sort(key=int)
    avg = len(friend_List) % 2
    if(avg == 0):
        mid = len(friend_List) / 2
        friend_Median = friend_List[mid]
    else:
        mid = len(friend_List) / 2
        mid = mid +1    
        friend_Median = friend_List[mid]
    return friend_Median


def SD():
    global friend_SD
    global friend_Mean
    stdDeviationSum = 0
    for num in friend_List:
        stdDeviationSum = stdDeviationSum + ((int(num) - int(friend_Mean)) *  (int(num) - int(friend_Mean)))
        # print('stdDeviationSum',stdDeviationSum)  
        friend_SD = round(math.sqrt(stdDeviationSum / total_count),2)
    return friend_SD

for follower in tweepy.Cursor(api.friends, screen_name=twitter_handle).items(): 
    total_count = total_count + 1
    listDict[follower.screen_name] = follower.friends_count
    friend_List.append(follower.friends_count)

friend_List.sort(key=int)
f = open('twitterFollowing.txt','w')
for friendCount in friend_List:
    f.write(str(count)+","+str(friendCount))
    f.write('\n')
    count = count + 1
    friend_count = friend_count + friendCount
f.close()    

mean = [str(mean())]
median = [str(median())]
SD = [str(SD())]
tableList = Table([mean, median, SD], names=('MEAN', 'MEDIAN', 'STANDARD DEVIATION'))
print (tableList)


  