from sandra.handler.handler import Handler
from pyjokes import get_joke, get_jokes

class JokeHandler(Handler):
    HANDLER_PATTERN = "(.*?)joke(.*?)"

    def __init__(self):
        super().__init__()

    def handle(self, command):
        return get_joke(category='all')
