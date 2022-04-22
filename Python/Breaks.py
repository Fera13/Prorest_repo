import time
from plyer import notification

if __name__ == "__main__":
#def work_break(button):
    button = True
    while button:
        notification.notify(title = "It's time for a small break!",
                            message = "Why don't you stretch a bit, move your body and rest your eyes :)",
                            app_name = "Prorest",
                            app_icon = "Meh.ico",
                            timeout = 60)
        time.sleep(1800)