"""Different operations to check time and send create notifications."""

import time
import datetime
from datetime import timedelta
import pafy
import vlc
from plyer import notification


def checkTimeFormat(input):
    """Check if the time entered is the right format with the right values."""
    try:
        if len(input) == 5:
            time.strptime(input, "%H:%M")
            return True
        return False
    except ValueError:
        return False


def play_music(link):
    """Take a youtube link and play it as sound in vlc player."""
    video = pafy.new(link)
    best = video.getbestaudio()
    playurl = best.url
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(playurl)
    media.get_mrl()
    player.set_media(media)
    player.play()
    time.sleep(60)
    player.stop()


def viewNotification(starter, msg, ico, displayTime, sleepTime):
    """Create notification. Takes title sentence, message, time and sleep."""
    notification.notify(
        title=starter,
        message=msg,
        app_name="Prorest",
        app_icon=ico,
        timeout=displayTime,
    )
    time.sleep(sleepTime)


def viewDateNotification(list_of_dates, ico, displayTime):
    """Create notification. Take title, date, time, message, icon, duration."""
    notifi_string = "You have these dates tomorrow :\n"
    for element in list_of_dates:
        notifi_string += (
            element[1] + ", time: " + element[0] + ", msg: " + element[2] + "\n"
        )
    notification.notify(
        title="important dates",
        message=notifi_string,
        app_name="Prorest",
        app_icon=ico,
        timeout=displayTime,
    )


def viewQuoteNotification(msg, ico, displayTime, sleep_time):
    """Create Quote notifications. Takes quote, icon, duration and time."""
    notification.notify(
        title="FOR YOU",
        message=msg,
        app_name="Prorest",
        app_icon=ico,
        timeout=displayTime,
    )
    time.sleep(sleep_time)


def calculate_time_difference(old_time, hours):
    """Calculate the time difference for sleep hours and wake up time."""
    time_delta = timedelta(hours=hours)
    new_time = old_time - time_delta
    return new_time


def check_date_format(input):
    """Check if input is the right format and right values. Returns boolean."""
    try:
        if len(input) == 10:
            datetime.datetime.strptime(input, "%Y-%m-%d")
            return True
        return False
    except TypeError:
        return False
