import time
from plyer import notification

def work_break(button):
    while True:
        if button:
            notification.notify(title = "It's time for a small break!",
                                message = "Why don't you stretch a bit, move your body and rest your eyes :)",
                                app_name = "Prorest",
                                app_icon = "Meh.ico",
                                timeout = 10)
            time.sleep(10)
        else:
            break