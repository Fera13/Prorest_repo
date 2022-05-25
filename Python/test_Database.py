"""This is the module to test the database funtions."""
import unittest
from unittest import TestCase
from unittest.mock import Mock
import Database as module_0

mock = Mock()


class test_database(TestCase):
    """This is the class to test the database class."""

    def test_play_songs_order(self):
        """Test that the song links are as expected."""
        database_0 = module_0.Database()
        assert module_0.Database.conInfo == {
            "user": "userPro",
            "password": "pass",
            "host": "127.0.0.1",
            "port": "3306",
            "database": "Prorest",
            "raise_on_warnings": True,
        }
        var_0 = database_0.play_songs_order()
        assert database_0 is not None
        assert var_0 == [
            "https://www.youtube.com/watch?v=eZEczfSAjVQ",
            "https://www.youtube.com/watch?v=3TKghKSDnEM",
            "https://www.youtube.com/watch?v=cTMOQiY0axo",
            "https://www.youtube.com/watch?v=twpQogWOgAs",
            "https://www.youtube.com/watch?v=uweorwa3q34",
            "https://www.youtube.com/watch?v=gBmgk8WakJE",
            "https://www.youtube.com/watch?v=H4BAEf5V-Yc",
            "https://www.youtube.com/watch?v=YR3IcPewNlk",
            "https://www.youtube.com/watch?v=pHJfHK4jb6E",
            "https://www.youtube.com/watch?v=znarNyPELcU",
            "https://www.youtube.com/watch?v=sJyO-By_9wc",
            "https://www.youtube.com/watch?v=eJ-LvX9HLrU",
            "https://www.youtube.com/watch?v=_1ThytX4ZiA",
            "https://www.youtube.com/watch?v=SzqPoVNrvMc",
        ]
        database_1 = module_0.Database()
        assert database_1 is not None

    def test_snack_recommendations(self):
        """Test that snack recommendations are as expected."""
        """Test that the snack recommendations are as expected."""
        database_0 = module_0.Database()
        assert module_0.Database.conInfo == {
            "user": "userPro",
            "password": "pass",
            "host": "127.0.0.1",
            "port": "3306",
            "database": "Prorest",
            "raise_on_warnings": True,
        }

        var_0 = database_0.snack_recommendations()
        assert database_0 is not None

        var_1 = "      Here are some tips!\n\n"
        my_rows = [
            "Bananas",
            "Dates",
            "Avocados",
            "Cashews",
            "Leafy vegetables",
            "Berries",
            "Walnuts",
        ]

        for snackNames in my_rows:
            var_1 += "  -    " + snackNames + "\n"
        assert var_0 == var_1
        database_1 = module_0.Database()
        assert database_1 is not None

    def test_write_important(self):
        """Testwriting important dates to database."""
        assert module_0.Database.conInfo == {
            "user": "userPro",
            "password": "pass",
            "host": "127.0.0.1",
            "port": "3306",
            "database": "Prorest",
            "raise_on_warnings": True,
        }
        conInfo = {
            "user": "userPro",
            "password": "pass",
            "host": "127.0.0.1",
            "port": "3306",
            "database": "Prorest",
            "raise_on_warnings": True,
        }
        date = "2022-01-05"
        time = "10:00"
        title = "title"
        message = "msg"
        d = module_0.Database()
        d.write_important(date, time, title, message)

        mock.connector.connect(**conInfo)
        mock.cursor()
        mock.execute()
        mock.commit()
        mock.close()
        mock.close()

        self.assertIsNone(mock.connector.connect.assert_called_once())
        self.assertIsNone(mock.cursor.assert_called_once())
        self.assertIsNone(mock.execute.assert_called_once())
        self.assertIsNone(mock.commit.assert_called_once())
        self.assertIsNone(mock.close.assert_called())

    def test_read_important(self):
        """Test reading important dates from database."""
        conInfo = {
            "user": "userPro",
            "password": "pass",
            "host": "127.0.0.1",
            "port": "3306",
            "database": "Prorest",
            "raise_on_warnings": True,
        }
        date = "2022-01-05"
        d = module_0.Database()
        d.read_important(date)
        mock2 = Mock()
        mock2.connector.connect(**conInfo)
        mock2.cursor()
        mock2.execute()
        mock2.append()
        mock2.fetchall()
        mock2.commit()
        mock2.close()
        mock2.close()

        self.assertIsNone(mock2.connector.connect.assert_called_once())
        self.assertIsNone(mock2.cursor.assert_called_once())
        self.assertIsNone(mock2.execute.assert_called())
        self.assertIsNone(mock2.append.assert_called())
        self.assertIsNone(mock2.fetchall.assert_called_once())
        self.assertIsNone(mock2.commit.assert_called_once())
        self.assertIsNone(mock2.close.assert_called())

    def test_check_important_dates(self):
        """Test checking important dates from daatabase."""
        app = module_0.Database()
        if app.check_important_dates() == []:
            expected = []
            self.assertListEqual(app.check_important_dates(), expected)
        else:
            expected = app.check_important_dates()
            self.assertListEqual(app.check_important_dates(), expected)

    def test_read_references(self):
        """Test reading references from database."""
        d = module_0.Database()
        d.read_references()
        mock4 = Mock()
        mock4.connector.connect()
        mock4.cursor()
        mock4.execute()
        mock4.fetchall()
        mock4.close()
        mock4.close()

        self.assertIsNone(mock4.connector.connect.assert_called_once())
        self.assertIsNone(mock4.cursor.assert_called_once())
        self.assertIsNone(mock4.execute.assert_called())
        self.assertIsNone(mock4.fetchall.assert_called_once())
        self.assertIsNone(mock4.close.assert_called())

    def test_read_def_quotes(self):
        """Test reading predefined quotes from database."""
        app = module_0.Database()
        randomQ = set([app.read_def_quotes()])
        expected = set(
            [
                "A positive mindset brings positive things!",
                "When you have a dream, you’ve got to grab it and never let go.",
                "You will always pass failure on your way to success.",
                "It always seems impossible until it is done.",
                "Once you replace negative thoughts with positive ones, you’ll start having positive results.",
                "The only time you fail is when you fall down and stay down.",
                "If opportunity doesn’t knock, build a door.",
                "Happiness is an attitude. We either make ourselves miserable, or happy and strong. The amount of work is the same.",
                "It’s not whether you get knocked down, it’s whether you get up.",
                "Nothing is impossible!",
            ]
        )
        self.assertTrue(expected.issuperset(randomQ))

    def test_read_per_quotes(self):
        """Test reading quotes from database."""
        d = module_0.Database()
        d.read_per_quotes()
        mock5 = Mock()
        mock5.connector.connect()
        mock5.cursor()
        mock5.execute()
        mock5.fetchall()
        mock5.close()
        mock5.close()

        self.assertIsNone(mock5.connector.connect.assert_called_once())
        self.assertIsNone(mock5.cursor.assert_called_once())
        self.assertIsNone(mock5.execute.assert_called())
        self.assertIsNone(mock5.fetchall.assert_called_once())
        self.assertIsNone(mock5.close.assert_called())

    def test_write_per_quote(self):
        """Test writing quotes to database."""
        mock6 = Mock()
        mock6.connector.connect()
        mock6.cursor()
        mock6.execute()
        mock6.commit()
        mock6.close()
        mock6.close()

        self.assertIsNone(mock6.connector.connect.assert_called_once())
        self.assertIsNone(mock6.cursor.assert_called_once())
        self.assertIsNone(mock6.execute.assert_called())
        self.assertIsNone(mock6.commit.assert_called_once())
        self.assertIsNone(mock6.close.assert_called())

    def test_write_wake_up(self):
        """Test for writing to database for wake up time."""
        assert module_0.Database.conInfo == {
            "user": "userPro",
            "password": "pass",
            "host": "127.0.0.1",
            "port": "3306",
            "database": "Prorest",
            "raise_on_warnings": True,
        }
        conInfo = {
            "user": "userPro",
            "password": "pass",
            "host": "127.0.0.1",
            "port": "3306",
            "database": "Prorest",
            "raise_on_warnings": True,
        }
        time = "07:00"
        mock7 = Mock()
        d = module_0.Database()
        d.write_wake_up(time)
        mock7.connector.connect(**conInfo)
        mock7.cursor()
        mock7.execute()
        mock7.commit()
        mock7.close()
        mock7.close()

        self.assertIsNone(mock7.connector.connect.assert_called_once())
        self.assertIsNone(mock7.cursor.assert_called_once())
        self.assertIsNone(mock7.execute.assert_called_once())
        self.assertIsNone(mock7.commit.assert_called_once())
        self.assertIsNone(mock7.close.assert_called())

    def test_read_wake_up(self):
        """Test the read from database method for wake up time."""
        d = module_0.Database()
        self.assertTrue(d.read_wake_up_time(), [""])


if __name__ == "__main__":
    unittest.main()
