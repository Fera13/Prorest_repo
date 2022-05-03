import mysql.connector


class Database:
    conInfo = {
        "user": "userPro", "password": "pass", 
        "host": "127.0.0.1", "port": "3306", 
        "database": "Prorest", "raise_on_warnings": True
        }
    def __init__(self):
        pass

    def play_songs_order(self):
        """Get a list of song links from the database and return it"""
        songs = []
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = "SELECT s.yt_link FROM songs s;"
        myCursor.execute(sql, )
        rows = myCursor.fetchall()
        for links in rows:
            for link in links:
                songs.append(link)
        myCursor.close()
        myCon.close()
        return songs
    
    def snack_recommendations(self):
        """Get a list of snacks from the database and return it"""
        snacks = []
        myCon = myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = "SELECT s.snack_name FROM snacks s;"
        myCursor.execute(sql)
        rows = myCursor.fetchall()
        for snackNames in rows:
            for snackName in snackNames:
                snacks.append(snackName)
        myCursor.close()
        myCon.close()
        return snacks