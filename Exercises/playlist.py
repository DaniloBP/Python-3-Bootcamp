# SPOTIFY EXERCISE 

playlist = {
	"title"  : "Good Ones",
	"author" : "Danilo Batista",
	"songs"  : []
}


song1 = { "title" : "This is America", "artist" : "Childish Gambino", "date" : "10/25/2018", "duration" : 270}
song2 = dict( title = "Ben", artist = "Michael Jackson", date = "04/14/2018", duration = 214)
song3 = dict( title = "War", artist = "Bob Marley", date = "05/14/2012", duration = 196)
song4 = { "title" : "Sober", "artist" : "Childish Gambino", "date" : "03/04/2018", "duration" : 246}
song3 = dict( title = "Turn Your Lights Down Low", artist = "Bob Marley", date = "10/21/2013", duration = 222)

playlist["songs"].append(song1)
playlist["songs"].append(song2)
playlist["songs"].append(song3)
playlist["songs"].append(song4)


for song in playlist["songs"]:
	print()
	for key, value in song.items():
		print(f"{key} =  {value}")
	print()
