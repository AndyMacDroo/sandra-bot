import unittest
from freezegun import freeze_time

from sandra.modules.joke import JokeHandler

class TestHandlerJoke(unittest.TestCase):

    def test_jokeHandler_withNoCommand_returnsAJoke(self):
        handler = JokeHandler()
        actual = handler.handle("")
        self.assertIsNotNone(actual)
