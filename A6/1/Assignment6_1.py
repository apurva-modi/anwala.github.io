from operator import itemgetter

matchingUsers = []
apurvAge = 23
apurvOccupation = 'student'
apurvGender = 'M' 
userMoviesDict = {}
userMovieRatingDict = {}
finalTopThree = {}
finalBottomThree = {}
userMovieRatingsList = []
movieRatingsList = []
matches = ''
bottomCount = 0
topCount = 0
listSize = 0

with open('u.user', 'r') as f1:
	for line in f1:
		userId,age,gender,occupation,zipcode = line.split('|')
		# if((int(age) < int(apurvAge) and int(age) > int((apurvAge - 3))) and (gender == apurvGender) and (occupation == apurvOccupation)):
		if((int(age) == apurvAge) and (gender == apurvGender) and (occupation == apurvOccupation)):	
			matchingUsers.append(userId)

print (matchingUsers)       	

with open('u.data', 'r') as f2:
	for line in f2:
		userId,movieId,rating,mseconds = line.split('	')
		if(userId in matchingUsers):
			if(userId in userMoviesDict):
				userMoviesDict[userId] = userMoviesDict[userId] + ":" + movieId + "|" + rating 
			else :
				userMoviesDict[userId] = movieId + "|" + rating 

print('--------')
for key, value in userMoviesDict.items():
	# print(key,userMoviesDict[key])
	userMovieRatingsList = userMoviesDict[key].split(":")
	for movieRating in userMovieRatingsList:
		movie,rating = movieRating.split("|")
		userMovieRatingDict[movie] = rating
		# print(movie,rating)

	sortedRatings = sorted(userMovieRatingDict.items(), key=lambda value: value[1])
	# print("Length :",len(sortedRatings))
	bottomCount = 0
	topCount = 0
	listSize = 0
	bottomMovieData = ""
	topMovieData = ""
	for data in sortedRatings:
		listSize = listSize + 1
		if(bottomCount < 3):
			if(bottomMovieData == ""):
				bottomMovieData = str(data)
			else :
				bottomMovieData = bottomMovieData + ":" + str(data)
			bottomCount = bottomCount + 1
		if(listSize > len(sortedRatings) - 3):
			if(topMovieData == ""):
				topMovieData = str(data)
			else :
				topMovieData = topMovieData + ":" + str(data)

	finalBottomThree[key] = bottomMovieData
	finalTopThree[key] = topMovieData
	print('--------------')	
	print(finalTopThree)
	print(finalBottomThree)
	print('\n')
print (" ******* TOP FAVORITE  MOVIES ******* ")
print ("User" + "  " + "Movie Title" + "  " + "Rating")
print ("----" + "  " + "-----------" + "  " + "------")
for key, value in finalTopThree.items():	
	movieTuple = finalTopThree[key].split(":")
	for movie in movieTuple:
		movieId,rating = str(movie).split(",")
		movieId = movieId.replace("(","").replace("'","")
		with open('u.item', 'r') as file:
			for line in file:
				mid,movieTitle = line.split("|")[0:2]
				if(mid == movieId):
					print (key,"  "+ movieTitle+"  "+rating.replace(")","").replace("'",""))

print('\n')

print (" ******* LEAST FAVORITE MOVIES ******* ")
print ("User" + "  " + "Movie Title" + "  " + "Rating")
print ("----" + "  " + "-----------" + "  " + "------")
for key, value in finalBottomThree.items():	
	movieTuple = finalBottomThree[key].split(":")
	for movie in movieTuple:
		movieId,rating = str(movie).split(",")
		movieId = movieId.replace("(","").replace("'","")
		with open('u.item', 'r') as file:
			for line in file:
				mid,movieTitle = line.split("|")[0:2]
				if(mid == movieId):
					print (key,"  "+ movieTitle+"  "+rating.replace(")","").replace("'",""))
