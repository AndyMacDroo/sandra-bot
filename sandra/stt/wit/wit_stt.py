from sandra.config.config import Config
from sandra.stt.stt_engine import STTEngine
from wit import Wit
import os

class WitSTT(STTEngine):
    def __init__(self):
        self.client = Wit(Config().get_wit_ai_api_key())

    def listen(self, mic, previous_frames=None):
        filename = mic.record()
        with open(filename, 'rb') as f:
            resp = self.client.speech(f, None, {'Content-Type': 'audio/wav'})
        # print('STT: ' + str(resp))
        os.remove(filename)
        return resp["_text"] if resp is not None else None
