from sandra.stt.stt_factory import STTFactory
import logging

class STT():

    def __init__(self,
                 wake_word_engine=STTFactory.WAKE_WORD,
                 stt_engine=STTFactory.WIT):
        logging.getLogger().debug("Initialising Sandra STT with wake engine '%s'" % wake_word_engine)
        logging.getLogger().debug("Initialising Sandra STT with STT engine '%s'" % stt_engine)
        self.wake_word_engine = STTFactory().get_instance(wake_word_engine)
        self.stt_engine = STTFactory().get_instance(stt_engine)

    def __is_activated(self, response):
        return response is not None

    def listen(self, mic):
        if self.__is_activated(self.wake_word_engine.listen(mic=mic)):
            stt_message = self.stt_engine.listen(mic=mic)
            return {"message": stt_message}
        else:
            return None
