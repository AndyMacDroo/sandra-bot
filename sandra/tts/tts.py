from sandra.tts.tts_factory import TTSFactory
import logging

class TTS():

    def __init__(self, engine=TTSFactory.DEFAULT):
        logging.getLogger().debug("Initialising Sandra TTS with engine '%s'" % engine)
        self.engine = TTSFactory().get_instance(engine)

    def say(self, message):
        self.engine.say(message)
