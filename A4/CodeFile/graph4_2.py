import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('twitterFollowers-Friends.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y)
plt.plot(65,250,marker='.', color='red',markersize=12)
plt.annotate('Dr.Nwala\'s Followers:250' , xy=(2, 620))

plt.plot(117,560,marker='.', color='red',markersize=12)
plt.annotate('Median:560' , xy=(120, 150))

plt.plot(185,1461.0,marker='.', color='red',markersize=12)
plt.annotate('Mean:1461.0' , xy=(190, 1260))


plt.plot(225, 3634.72,marker='.', color='red',markersize=12)
plt.annotate('Standard\nDeviation:3634.72' , xy=(140, 4000))

plt.xlim(0, 300)
plt.ylim(0, 10000)

plt.xlabel('All Followers')
plt.ylabel('No. of Friends for Each Follower')
plt.title('Twitter Followers Vs Each Follower\'s Friend count')
plt.legend()
plt.show()