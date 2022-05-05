from socket import timeout
import time
import pafy
import vlc
from plyer import notification

def checkTimeFormat(input):
    """Checks if the time entered is the right format with the right values. Returns boolean"""
    try:
        if len(input) == 5:
            time.strptime(input, '%H:%M')
            return True
        else:
            return False
    except ValueError:
        return False

def play_music(link):
    """Takes a youtube link and plays it as sound in vlc player"""
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
    """Creates notifications. Takes title sentence, message, time that it will be displayed in and time until the next notification"""
    notification.notify(title = starter,
                        message = msg,
                        app_name = "Prorest",
                        app_icon = ico,
                        timeout = displayTime)
    time.sleep(sleepTime)

def viewDateNotification(starter, date, clock, msg, ico, displayTime):
    """Creates a notification for important dates. Takes title, date, time, message, icon and the duration of the notification as parameters."""
    date += ", "
    date += clock + "\n"
    date += msg
    notification.notify(title = starter,
                        message = date,
                        app_icon = ico,
                        timeout = displayTime)