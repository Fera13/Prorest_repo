import time
import pafy
import vlc
from plyer import notification

def isTimeFormat(input):
    try:
        if len(input) == 5:
            time.strptime(input, '%H:%M')
            return True
        else:
            return False
    except ValueError:
        return False

def play_music(link):
    video = pafy.new(link)
    length = video.length
    best = video.getbestaudio()
    playurl = best.url
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(playurl)
    media.get_mrl()
    player.set_media(media)
    player.play()
    time.sleep(length)
    player.stop()
    
def viewNotification(starter, msg, ico, displayTime, sleepTime):
    notification.notify(title = starter,
                        message = msg,
                        app_name = "Prorest",
                        app_icon = ico,
                        timeout = displayTime)
    time.sleep(sleepTime)