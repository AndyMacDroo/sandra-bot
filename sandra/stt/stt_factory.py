from sandra.stt.wake_word.wake_word_stt import WakeWordSTT
from sandra.stt.wit.wit_stt import WitSTT


class STTFactory():
    WAKE_WORD = "WAKE_WORD"
    WIT = "WIT"

    def get_instance(self, engine):
        switcher = {
            self.WAKE_WORD: WakeWordSTT(),
            self.WIT:       WitSTT()
        }
        return switcher.get(engine, "Invalid engine")
