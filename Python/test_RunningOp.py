import unittest
import RunningOp


class test_RunninOp(unittest.TestCase):
    def test_isTimeFormat(self):
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        var_0 = RunningOp.isTimeFormat(dict_0)
        assert var_0 is False
        assert RunningOp.notification is not None
        
        try:
            bool_1 = None
            var_1 = RunningOp.isTimeFormat(bool_1)
        except BaseException:
            pass
        
    def test_play_music(self):
        try:
            tuple_0 = ()
            str_0 = '~\r},"'
            var_0 = RunningOp.isTimeFormat(str_0)
            assert var_0 is False
            assert RunningOp.notification is not None
            int_0 = -926
            dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, int_0: int_0}
            var_1 = RunningOp.isTimeFormat(dict_0)
            assert var_1 is False
            str_1 = '\x0b1\x0bqn ;'
            dict_1 = None
            set_0 = {str_1, dict_1, str_1}
            var_2 = RunningOp.play_music(set_0)
        except BaseException:
            pass
        
        try:
            bytes_3 = b'\xebJ\xfa\xf8\x10\xcf;\x1d\\\xe0M\xab\x06R\x8b\x9f\x04|'
            var_0 = RunningOp.play_music(bytes_3)
        except BaseException:
            pass


    def test_viewNotification(self):
        float_0 = 2355.033989
        str_0 = '1-`'
        complex_0 = None
        tuple_0 = ()
        bool_0 = False
        var_0 = RunningOp.viewNotification(float_0, str_0, complex_0, tuple_0, bool_0)
        
if __name__ == '__main__':
    unittest.main()
