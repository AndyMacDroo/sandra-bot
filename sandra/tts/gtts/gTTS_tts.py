from sandra.tts.tts_engine import TTSEngine
from gtts import gTTS
from tempfile import NamedTemporaryFile
import pygame
import time

class GTTSTTS(TTSEngine):
    def __init__(self):
        pass

    def say(self, message):
        if message is not None:
            print("TTS: %s" % message)
            pygame.mixer.pre_init(25000, -16, 2, 2048)
            pygame.init()
            tts = gTTS(text=message, lang='en', slow=False)
            f = NamedTemporaryFile()
            tts.write_to_fp(f)
            pygame.mixer.music.load(f.name)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() is True:
                time.sleep(0.02)
                continue
            time.sleep(0.02)
            pygame.quit()
            f.close()
