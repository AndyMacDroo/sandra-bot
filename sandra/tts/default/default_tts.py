import pyttsx3

from sandra.tts.tts_engine import TTSEngine


class DefaultTTS(TTSEngine):
    def __init__(self):
        self.engine = pyttsx3.init()

    def say(self, message):
        if message is not None:
            self.engine.say(message)
            self.engine.runAndWait()
