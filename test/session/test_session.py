import unittest
from unittest.mock import MagicMock

from sandra.session.session import SandraSession


class TestSession(unittest.TestCase):

    def test_sandraSession_noHandlerDirector_raisesException(self):
        with self.assertRaises(Exception) as context:
            SandraSession(handler_director=None)

    def test_sandraSession_noTTSModule_raisesException(self):
        mock_handler_director = MagicMock()
        with self.assertRaises(Exception) as context:
            SandraSession(handler_director=mock_handler_director, stt=MagicMock(), mic=MagicMock())

    def test_sandraSession_noSTTModule_raisesException(self):
        mock_handler_director = MagicMock()
        with self.assertRaises(Exception) as context:
            SandraSession(handler_director=mock_handler_director, tts=MagicMock(), mic=MagicMock())

    def test_sandraSession_withDependencies_initialisesInstance(self):
        mock_handler_director = MagicMock()
        SandraSession(handler_director=mock_handler_director, tts=MagicMock(), stt=MagicMock(), mic=MagicMock())
