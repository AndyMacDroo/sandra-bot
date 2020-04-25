from sandra.tts.default.default_tts import DefaultTTS
from sandra.tts.gtts.gTTS_tts import GTTSTTS


class TTSFactory():
    DEFAULT = "DEFAULT"
    GTTS = "GTTS"

    def get_instance(self, engine):
        switcher = {
            self.DEFAULT: DefaultTTS(),
            self.GTTS   : GTTSTTS()
        }
        return switcher.get(engine, "Invalid engine")
