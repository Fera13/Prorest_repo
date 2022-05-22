from socket import timeout
import time
import datetime
from datetime import timedelta
from charset_normalizer import detect
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

def viewDateNotification(list_of_dates, ico, displayTime):
    """Creates a notification for important dates. Takes title, date, time, message, icon and the duration of the notification as parameters."""
    notifi_string = "You have these dates tomorrow :\n"
    for element in list_of_dates:
        notifi_string += element[1] + ", time: " + element[0]+ ", msg: " + element[2]+ "\n"
    notification.notify(title = "important dates",
                        message = notifi_string,
                        app_name = "Prorest",
                        app_icon = ico,
                        timeout = displayTime)
    
def viewQuoteNotification(msg, ico, displayTime, sleep_time):
    """Creates Quotes notifications. That it will be displayed in and time until the next notification"""
    notification.notify(title = "FOR YOU",
                        message = msg,
                        app_name = "Prorest",
                        app_icon = ico,
                        timeout = displayTime)
    time.sleep(sleep_time)
    
def calculate_time_difference(old_time, hours):
    """Function to calculate the time difference for sleep hours and wake up time"""
    time_delta = timedelta(hours=hours)
    new_time = old_time - time_delta
    return new_time

def check_date_format(input):
    """Checks if the date entered is the right format with the right values. Returns boolean"""
    try:
        if len(input) == 10:
            datetime.datetime.strptime(input, '%Y-%m-%d')
            return True
        else:
            return False
    except TypeError:
        return False