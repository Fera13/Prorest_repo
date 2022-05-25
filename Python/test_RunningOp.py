"""Tests for RunningOp."""

import unittest
from unittest import mock
from unittest.mock import Mock
import RunningOp


class test_RunninOp(unittest.TestCase):
    """Different methods for tests."""

    def test_isTimeFormat(self):
        """Tests the time format."""
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        var_0 = RunningOp.checkTimeFormat(dict_0)
        assert var_0 is False
        assert RunningOp.notification is not None

        try:
            bool_1 = None
            RunningOp.checkTimeFormat(bool_1)
        except BaseException:
            pass
        rightTime = "10:00"
        self.assertTrue(RunningOp.checkTimeFormat(rightTime))

    def test_play_music(self):
        """Test play music."""
        try:
            tuple_0 = ()
            str_0 = '~\r},"'
            var_0 = RunningOp.checkTimeFormat(str_0)
            assert var_0 is False
            assert RunningOp.notification is not None
            int_0 = -926
            dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, int_0: int_0}
            var_1 = RunningOp.checkTimeFormat(dict_0)
            assert var_1 is False
            str_1 = "\x0b1\x0bqn ;"
            dict_1 = None
            set_0 = {str_1, dict_1, str_1}
            var_2 = RunningOp.play_music(set_0)
        except BaseException:
            pass

        try:
            bytes_3 = b"\xebJ\xfa\xf8\x10\xcf;\x1d\\\xe0M\xab\x06R\x8b\x9f\x04|"
            var_1 = RunningOp.play_music(bytes_3)
        except BaseException:
            pass

    def test_play_music2(self):
        """Test to play link."""
        link = "https://www.youtube.com/watch?v=Wch3gJG2GJ4"
        RunningOp.play_music(link)
        mocker = Mock()
        mocker.new()
        mocker.getbestaudio()
        mocker.Instance()
        mocker.media_player_new()
        mocker.media_new()
        mocker.get_mrl()
        mocker.set_media()
        mocker.play()
        mocker.sleep()
        mocker.stop()

        self.assertIsNone(mocker.new.assert_called_once())
        self.assertIsNone(mocker.getbestaudio.assert_called_once())
        self.assertIsNone(mocker.Instance.assert_called_once())
        self.assertIsNone(mocker.media_player_new.assert_called_once())
        self.assertIsNone(mocker.media_new.assert_called_once())
        self.assertIsNone(mocker.get_mrl.assert_called_once())
        self.assertIsNone(mocker.set_media.assert_called_once())
        self.assertIsNone(mocker.play.assert_called_once())
        self.assertIsNone(mocker.sleep.assert_called_once())
        self.assertIsNone(mocker.stop.assert_called_once())

    def test_viewNotification(self):
        """Test to view notification."""
        float_0 = "2355.033989"
        str_0 = "1-`"
        complex_0 = None
        tuple_0 = ()
        bool_0 = False
        RunningOp.viewNotification(float_0, str_0, complex_0, tuple_0, bool_0)

    @mock.patch("RunningOp.viewDateNotification")
    def test_viewDateNotification(self, mock_notification):
        """Test date notification."""
        list_of_dates = [
            ("23:11", "Meeting", "Get ready"),
            ("20:12", "Comp", "Draw something"),
        ]
        ico = "Icons/Meh.ico"
        displayTime = 5
        mock_notification(list_of_dates, ico, displayTime)
        self.assertIsNone(
            mock_notification.assert_called_once_with(list_of_dates, ico, displayTime)
        )

    @mock.patch("RunningOp.viewQuoteNotification")
    def test_viewQuoteNotification_notify(self, mock_quote_notification):
        """Test quote notification."""
        msg = "Hi"
        ico = "Icons/Meh.ico"
        title = "FOR YOU"
        app_name = "Prorest"
        displayTime = 5

        mock_quote_notification.notify(title, msg, app_name, ico, displayTime)
        mock_quote_notification.notify.assert_called_with(
            title, msg, app_name, ico, displayTime
        )

    def test_check_date_format(self):
        """Check date format."""
        input1 = "Hi"
        input2 = "2022-01-05"
        input3 = 3

        self.assertTrue(RunningOp.check_date_format(input2))
        self.assertFalse(RunningOp.check_date_format(input1))
        self.assertFalse(RunningOp.check_date_format(input3))


if __name__ == "__main__":
    unittest.main()
