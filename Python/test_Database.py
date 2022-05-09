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
        assert module_0.Database.conInfo == {'user': 'userPro', 'password': 'pass', 'host': '127.0.0.1', 
                                             'port': '3306', 'database': 'Prorest', 'raise_on_warnings': True}
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
    
if __name__ == '__main__':
    unittest.main()
