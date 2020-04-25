from sandra.session.mic import Mic

class SandraSession():

    def __init__(self, handler_director, stt=None, tts=None, mic=None):
        self.handler_director = handler_director
        if handler_director is None or stt is None or tts is None:
            raise Exception("Cannot start session without valid STT or TTS module")
        self.stt = stt
        self.tts = tts
        self.mic = Mic() if mic is None else mic

    def start(self):
        while True:
            utterance = self.stt.listen(mic=self.mic)
            if utterance is not None:
                responses = self.handler_director.handle_with_handler(utterance["message"])
                [self.tts.say(response["response"]) for response in responses]
