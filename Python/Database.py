"""This is the database file which holds the database class."""
from datetime import date, timedelta
import mysql.connector


class Database:
    """This is the class that connects to database and handle sql commands."""

    conInfo = {
        "user": "userPro",
        "password": "pass",
        "host": "127.0.0.1",
        "port": "3306",
        "database": "Prorest",
        "raise_on_warnings": True,
    }

    def __init__(self):
        """Create the init method for database."""
        pass

    def play_songs_order(self) -> list:
        """Get a list of song links from the database and return it."""
        songs = []
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = "SELECT s.yt_link FROM songs s;"
        myCursor.execute(
            sql,
        )
        rows = myCursor.fetchall()
        for links in rows:
            for link in links:
                songs.append(link)
        myCursor.close()
        myCon.close()
        return songs

    def snack_recommendations(self) -> str:
        """Get a string of snacks from the database and return it."""
        snacks = "      Here are some tips!\n\n"
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = "SELECT s.snack_name FROM snacks s;"
        myCursor.execute(
            sql,
        )
        rows = myCursor.fetchall()
        for snackNames in rows:
            for snackName in snackNames:
                snacks += "  -    " + snackName + "\n"
        myCursor.close()
        myCon.close()
        return snacks
        # add a function that is similar but takes id for testing

    def write_important(self, date, time, title, message):
        """Write important dates to the database."""
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = "INSERT INTO important_dates (the_date, the_time, title, msg) VALUES ( %s, %s, %s, %s);"
        args = (date, time, title, message)
        myCursor.execute(sql, args)
        myCon.commit()
        myCursor.close()
        myCon.close()

    def read_wake_up_time(self) -> str:
        """Read the time in the database."""
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = "SELECT my_time FROM wake_time LIMIT 1;"
        myCursor.execute(
            sql,
        )
        rows = myCursor.fetchall()
        for row in rows:
            time = row[0]
        myCursor.close()
        myCon.close()
        return time

    def read_important(self, date) -> list:
        """Read from important dates in the database based on the date."""
        importantInfo = []
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql1 = "SELECT the_time, title, msg FROM important_dates WHERE the_date = %s;"
        args = (date,)
        myCursor.execute(sql1, args)
        rows = myCursor.fetchall()
        for the_dates in rows:
            importantInfo.append(the_dates)
        sql2 = "DELETE FROM important_dates WHERE the_date = %s;"
        args = (date,)
        myCursor.execute(sql2, args)
        myCon.commit()
        myCursor.close()
        myCon.close()
        return importantInfo

    def check_important_dates(self) -> list:
        """Check if there is important dates for tomorrow."""
        importantInfo = []
        date_0 = date.today() + timedelta(days=1)
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql1 = "SELECT the_date FROM important_dates WHERE the_date = %s;"
        args = (date_0,)
        myCursor.execute(sql1, args)
        rows = myCursor.fetchall()
        for the_dates in rows:
            importantInfo.append(the_dates)
        myCursor.close()
        myCon.close()
        return importantInfo

    def read_references(self) -> str:
        """Read from references in the database."""
        all_refs = ""
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = "SELECT sources FROM refs;"
        myCursor.execute(
            sql,
        )
        rows = myCursor.fetchall()
        for row in rows:
            string_1 = f"\n{row[0]}\n"
            all_refs += string_1
            string_1 = ""
        myCursor.close()
        myCon.close()
        return all_refs

    def read_def_quotes(self) -> str:
        """Read from the default quotes in the database."""
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = "SELECT quote FROM def_quotes ORDER BY RAND() LIMIT 1;"
        myCursor.execute(
            sql,
        )
        rows = myCursor.fetchall()
        for row in rows:
            string_0 = row[0]
        myCursor.close()
        myCon.close()
        return string_0

    # add a function that is similar but takes id for testing
    def read_per_quotes(self) -> str:
        """Read from personal quotes in the database."""
        string_0 = ""
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = "SELECT quote FROM per_quotes ORDER BY RAND() LIMIT 1;"
        myCursor.execute(
            sql,
        )
        rows = myCursor.fetchall()
        for row in rows:
            string_0 += row[0]
        myCursor.close()
        myCon.close()
        if string_0 == "":
            string_0 = "Add your first quote ;)"
            return string_0
        else:
            return string_0

    # add a function that is similar but takes id for testing
    def write_per_quote(self, quote_0):
        """Write a quote to the database."""
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        sql = "INSERT INTO per_quotes (quote) VALUES (%s);"
        args = (quote_0,)
        myCursor.execute(sql, args)
        myCon.commit()
        myCursor.close()
        myCon.close()

    def write_wake_up(self, time):
        """Write, delete, and update wake up time to the database."""
        myCon = mysql.connector.connect(**self.conInfo)
        myCursor = myCon.cursor(prepared=True)
        myCursor.execute("INSERT INTO wake_time (my_time) VALUES (%s)", (time,))
        myCursor.execute("DELETE FROM wake_time WHERE my_time != %s;", (time,))
        myCon.commit()
        myCursor.close()
        myCon.close()
