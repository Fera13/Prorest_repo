from multiprocessing.context import assert_spawning
import unittest
from unittest import TestCase
from unittest.mock import Mock
import Database as module_0
mock = Mock()


class test_database(TestCase):
    
    def test_play_songs_order(self):
        database_0 = module_0.Database()
        assert module_0.Database.conInfo == {'user': 'userPro', 'password': 'pass', 'host': '127.0.0.1', 
                                             'port': '3306', 'database': 'Prorest', 'raise_on_warnings': True}
        var_0 = database_0.play_songs_order()
        assert database_0 is not None
        assert var_0 == ["https://www.youtube.com/watch?v=eZEczfSAjVQ", "https://www.youtube.com/watch?v=3TKghKSDnEM", 
                         "https://www.youtube.com/watch?v=cTMOQiY0axo", "https://www.youtube.com/watch?v=twpQogWOgAs", 
                         "https://www.youtube.com/watch?v=uweorwa3q34", "https://www.youtube.com/watch?v=gBmgk8WakJE", 
                         "https://www.youtube.com/watch?v=H4BAEf5V-Yc", "https://www.youtube.com/watch?v=YR3IcPewNlk", 
                         "https://www.youtube.com/watch?v=pHJfHK4jb6E", "https://www.youtube.com/watch?v=znarNyPELcU", 
                         "https://www.youtube.com/watch?v=sJyO-By_9wc", "https://www.youtube.com/watch?v=eJ-LvX9HLrU", 
                         "https://www.youtube.com/watch?v=_1ThytX4ZiA", "https://www.youtube.com/watch?v=SzqPoVNrvMc"]
        database_1 = module_0.Database()
        assert database_1 is not None

    def test_snack_recommendations(self):
        database_0 = module_0.Database()
        assert module_0.Database.conInfo == {"user": "userPro", "password": "pass", 
        "host": "127.0.0.1", "port": "3306", 
        "database": "Prorest", "raise_on_warnings": True}
        var_0 = database_0.snack_recommendations()
        assert database_0 is not None

        var_1 = "      Here are some tips!\n\n"
        my_rows = ["Bananas", "Dates",
                         "Avocados", "Cashews", 
                         "Leafy vegetables", "Berries", 
                         "Walnuts"]

        for snackNames in my_rows:
            var_1 += "  -    " + snackNames + "\n"
        
        assert var_0 == var_1       

        database_1 = module_0.Database()
        assert database_1 is not None
        
    def test_write_important(self):
        assert module_0.Database.conInfo == {'user': 'userPro', 'password': 'pass', 'host': '127.0.0.1', 
                                             'port': '3306', 'database': 'Prorest', 'raise_on_warnings': True}
        conInfo = {'user': 'userPro', 'password': 'pass', 'host': '127.0.0.1', 
                                             'port': '3306', 'database': 'Prorest', 'raise_on_warnings': True}
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
        conInfo = {'user': 'userPro', 'password': 'pass', 'host': '127.0.0.1', 
                                             'port': '3306', 'database': 'Prorest', 'raise_on_warnings': True}
        date = "2022-01-05"
        d = module_0.Database()
        d.read_important(date)
        mock2 = Mock()
        mock2.connector.connect(**conInfo)
        mock2.cursor()
        mock2.execute()
        mock2.fetchall()
        mock2.commit()
        mock2.close()
        mock2.close()
        
        self.assertIsNone(mock2.connector.connect.assert_called_once())
        self.assertIsNone(mock2.cursor.assert_called_once())
        self.assertIsNone(mock2.execute.assert_called())
        self.assertIsNone(mock2.fetchall.assert_called_once())
        self.assertIsNone(mock2.commit.assert_called_once())
        self.assertIsNone(mock2.close.assert_called())
    
    
    def test_check_important_dates(self):
        mock3 = Mock()
        mock3.today()
        mock3.connector.connect()
        mock3.cursor()
        mock3.execute()
        mock3.fetchall()
        mock3.append()
        mock3.close()
        mock3.close()
        
        self.assertIsNone(mock3.today.assert_called_once())
        self.assertIsNone(mock3.connector.connect.assert_called_once())
        self.assertIsNone(mock3.cursor.assert_called_once())
        self.assertIsNone(mock3.execute.assert_called())
        self.assertIsNone(mock3.fetchall.assert_called_once())
        self.assertIsNone(mock3.append.assert_called())
        self.assertIsNone(mock3.close.assert_called())
        
    # @mock.patch("Database.check_important_dates")
    # def test_check_important_dates2(self, mock_check_important_dates2):
        
    #     app = module_0()
    #     expected = ["2022-06-07"]
    #     mock_check_important_dates2.side_effect = ["2022-06-07"]
    #     self.assertListEqual(app.check_important_dates(), expected)
    
    def test_read_references(self):
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
        
    # @mock.patch("Database.read_references")
    # def test_read_references(self, mock_read_references2):
        
    #     app = module_0()
    #     expected = "ref"
    #     mock_read_references2.return_value = "ref"
    #     self.assertEqual(app.read_references(), expected)
    
    def test_read_quotes(self):
        d = module_0.Database()
        d.read_quotes()
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

    # @mock.patch("Database.read_quotes")
    # def test_read_references(self, mock_read_quotes):
        
    #     app = module_0()
    #     expected = "Nothing is impossible!"
    #     mock_read_quotes.side_effect = ["A positive mindset brings positive things!",
    #                                     "When you have a dream, you’ve got to grab it and never let go.",
    #                                     "Nothing is impossible!", "You will always pass failure on your way to success.",
    #                                     "It always seems impossible until it is done.", "Once you replace negative thoughts with positive ones, you’ll start having positive results.",
    #                                     "The only time you fail is when you fall down and stay down.", "If opportunity doesn’t knock, build a door.",
    #                                     "Happiness is an attitude. We either make ourselves miserable, or happy and strong. The amount of work is the same.",
    #                                     "It’s not whether you get knocked down, it’s whether you get up."]
    #     self.assertEqual(app.read_references(), expected)
    
    def test_write_quote(self):
        qoute = "I am alive"
        d = module_0.Database()
        d.write_quote(qoute)
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
        

        
    
        
        
    
if __name__ == '__main__':
    unittest.main()
