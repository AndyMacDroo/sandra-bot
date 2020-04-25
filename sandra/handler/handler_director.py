import re
import logging

class HandlerDirector():

    def __init__(self, handlers=None):
        self.handlers = [] if handlers is None else handlers
        logging.getLogger().debug("Handler director initialised with handlers %s" % str(self.handlers))

    def __matches(self, pattern, element):
        return re.match(pattern, element)

    def __trigger_handler(self, handler, command):
        return handler.handle(command)

    def handle_with_handler(self, command=None):
        responses = []
        [responses.append(
            {
                "handler": handler.__class__.__name__,
                "response": self.__trigger_handler(handler, command)
            })
            for handler in self.handlers if self.__matches(handler.HANDLER_PATTERN, command)]
        return responses
