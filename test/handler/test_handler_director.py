import unittest
from unittest.mock import MagicMock

from sandra.handler.handler_director import HandlerDirector


class TestHandlerDirector(unittest.TestCase):

    @staticmethod
    def __get_mock_handler(name=None, return_value=None, match_pattern=None):
        mock_handler = MagicMock()
        mock_handler.HANDLER_PATTERN = "THIS_WILL_MATCH" if match_pattern is None else match_pattern
        mock_handler.handle.return_value = "MockReturn" if return_value is None else return_value
        mock_handler.__class__.__name__ = "MockHandler" if name is None else name
        return mock_handler

    def test_handlerDirector_noMatchingHandler_returnsEmptyList(self):
        handler_director = HandlerDirector()
        actual = handler_director.handle_with_handler("Test")
        self.assertEqual([], actual)

    def test_handlerDirector_withMatchingHandler_returnsResponseListWithHandlerClassName(self):
        handler_director = HandlerDirector(
            handlers=[self.__get_mock_handler("MockHandler", "MockResponse", "THIS_WILL_MATCH")])
        actual = handler_director.handle_with_handler("THIS_WILL_MATCH")
        self.assertEqual([{'handler': 'MockHandler', 'response': 'MockResponse'}], actual)

    def test_handlerDirector_withMultipleMatchingHandlers_returnsMultipleResponsesWithHandlerClassName(self):
        handler_director = HandlerDirector(
            handlers=[self.__get_mock_handler("MockHandler", "MockResponse", "THIS_WILL_MATCH"),
                      self.__get_mock_handler("AnotherMockHandler", "AnotherResponse", "THIS_WILL(.*?)_MATCH")]
        )
        actual = handler_director.handle_with_handler("THIS_WILL_MATCH")
        self.assertEqual([{'handler': 'MockHandler', 'response': 'MockResponse'},
                          {'handler': 'AnotherMockHandler', 'response': 'AnotherResponse'}], actual)

    def test_handlerDirector_withHandlersNotAllMatch_returnsMultipleResponsesOnlyThoseMatching(self):
        handler_director = HandlerDirector(
            handlers=[self.__get_mock_handler("MockHandler", "MockResponse", "THIS_WILL_MATCH"),
                      self.__get_mock_handler("NonMatchingMockHandler", "MockResponse", "THIS_WONT_MATCH"),
                      self.__get_mock_handler("AnotherMockHandler", "AnotherResponse", "THIS_WILL(.*?)_MATCH")]
        )
        actual = handler_director.handle_with_handler("THIS_WILL_MATCH")
        self.assertEqual([{'handler': 'MockHandler', 'response': 'MockResponse'},
                          {'handler': 'AnotherMockHandler', 'response': 'AnotherResponse'}], actual)
