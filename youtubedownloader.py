import pytube
link = "https://youtu.be/zEngh-u4CX0?feature=shared" 
yt = pytube.YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()