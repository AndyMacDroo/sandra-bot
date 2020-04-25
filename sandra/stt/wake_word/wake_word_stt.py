from sandra.stt.stt_engine import STTEngine
import pvporcupine
from datetime import datetime

handle = pvporcupine.create(keywords=['picovoice', 'computer'])

class WakeWordSTT(STTEngine):
    def __init__(self):
        pass

    def listen(self, mic, previous_frames=None):
        keyword_index = handle.process(mic.get_next_audio_frame())
        if keyword_index >= 0:
            print('[%s] detected keyword' % str(datetime.now()))
            return "WAKE WORD DETECTED"
        else:
            return None
