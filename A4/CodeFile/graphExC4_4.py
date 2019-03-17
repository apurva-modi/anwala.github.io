import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('twitterFollowing.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y)
plt.plot(10,92,marker='.', color='red',markersize=12)
plt.annotate('Dr.Nwala\'s Friends: 92', xy=(1, 392))

plt.plot(43,461,marker='.', color='red',markersize=12)
plt.annotate('Median: 461' , xy=(42, 121))

plt.plot(73.5,1255,marker='.', color='red',markersize=12)

plt.annotate('Mean: 1255.0' , xy=(76, 1250.0))

plt.plot(81.5,2625,marker='.', color='red',markersize=12)
plt.annotate('Standard\nDeviation: 2625.42' , xy=(51, 2500.42))

plt.ylim(0, 7000)
plt.xlim(0, 100)

plt.xlabel('All Friends')
plt.ylabel('No. of Friends for Each Friend')
plt.title('Twitter Friends Vs Each Friend count')
plt.legend()
plt.show()
