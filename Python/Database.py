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
        """Get a string of snacks from the database and return it"""
        snacks = "      Here are some tips!\n\n"
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = "SELECT s.snack_name FROM snacks s;"
        myCursor.execute(sql, )
        rows = myCursor.fetchall()
        for snackNames in rows:
            for snackName in snackNames:
                snacks += "  -    " + snackName + "\n"
        myCursor.close()
        myCon.close()
        return snacks
    
    def write_important(self, date, time, title, message):
        """Writing important dates to the database"""
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = f"INSERT INTO important_dates (id, the_date, the_time, title, msg) VALUES (1, {date}, {time}, {title}, {message});"
        myCursor.execute(sql)
        myCursor.close()
        myCon.close()
    
    
    def read_important(self, date):
        """Reading from important dates in the database based on the date"""
        importantInfo = []
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql1 = f"SELECT the_date, the_time, title, msg FROM important_dates WHERE the_date = {date};"
        myCursor.execute(sql1)
        rows = myCursor.fetchall()
        for the_dates, in rows:
            for the_date in the_dates:
                importantInfo.append(the_date)
        sql2 = f"DELETE FROM important_dates WHERE the_date = {date};"
        myCursor.execute(sql2)
        myCursor.close()
        myCon.close()
        return importantInfo
