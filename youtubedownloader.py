import pytube
link = input("Paste the link here: ")               #provide your YouTube link here
yt = pytube.YouTube(link)         
stream = yt.streams.get_highest_resolution()
stream.download('provide a path')       
''' in the () provide the location of the folder 
in which you want to download or else 
it'll download in the same folder in which your code exists. 
It'll take some time to download, 
depending upon the length and max resolution of the video''' 
