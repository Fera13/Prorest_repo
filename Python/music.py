import vlc
import pafy
import time

url = "https://www.youtube.com/watch?v=WzQBAc8i73E"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(playurl)
media.get_mrl()
player.set_media(media)
player.play()
time.sleep(210)

if n==1:
    videolink = video.getbest()
    print("video is playing")
else:
    videolink =video.getbestaudio()  
    print("audio is playing")


