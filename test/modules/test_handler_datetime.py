import unittest
from freezegun import freeze_time

from sandra.modules.datetime import DateTimeHandler

class TestHandlerDatetime(unittest.TestCase):

    def test_dateTimeHandler_withNoCommand_returnsEmptyString(self):
        handler = DateTimeHandler()
        actual = handler.handle("")
        self.assertEqual("", actual)

    @freeze_time("2012-01-01")
    def test_dateTimeHandler_withDateCommand_returnsDate(self):
        handler = DateTimeHandler()
        actual = handler.handle("date")
        self.assertEqual("Todays date is January 1st, 2012", actual)

    @freeze_time("2012-01-01")
    def test_dateTimeHandler_withTimeCommand_returnsTime(self):
        handler = DateTimeHandler()
        actual = handler.handle("time")
        self.assertEqual("the time is 12:00 AM", actual)

    @freeze_time("2012-01-01 12:50")
    def test_dateTimeHandler_withDateAndTimeCommand_returnsTime(self):
        handler = DateTimeHandler()
        actual = handler.handle("date and time")
        self.assertEqual("Todays date is January 1st, 2012 and the time is 12:50 PM", actual)