import importlib
import logging
from sandra.handler.handler_director import HandlerDirector
from sandra.session.session import SandraSession
from sandra.stt.stt import STT
from sandra.tts.tts import TTS
from module_loader import app_modules

class Sandra():

    def __load_modules(self):
        handlers = []
        for module in app_modules:
            imported_module = importlib.import_module('sandra.modules.%s' % module)
            class_names = [attribute for attribute in dir(imported_module) if
                           not attribute.startswith('__') and not attribute == 'Handler']
            class_ = getattr(imported_module, class_names[0])
            instance = class_()
            handlers.append(instance)
        self.handlers = handlers

    def __init__(self, tts=None, stt=None):
        self.__load_modules()
        self.tts = tts
        self.stt = stt
        self.handler_director = HandlerDirector(handlers=self.handlers)
        self.session = SandraSession(self.handler_director, stt=self.stt, tts=self.tts)

    def start_session(self):
        logging.getLogger().debug("Listening")
        self.session.start()

if __name__ == '__main__':
    sandra = Sandra(tts=TTS(), stt=STT())
    sandra.start_session()