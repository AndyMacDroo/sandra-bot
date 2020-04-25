import pyaudio
import struct
import wave
import time
import math
import os

SHORT_NORMALIZE = (1.0/32768.0)
SAMPLE_RATE=16000
INPUT_CHUNK=512
OUTPUT_CHUNK=1024
DEVICE_INDEX = 7
swidth = 2
Threshold = 10
CHANNELS = 1
FORMAT = pyaudio.paInt16
RECORDING_NOTIFICATION_WAV_FILE = 'assets/chirp.wav'
TMP_RECORDING_LOCATION="tmp/"
TIMEOUT_LENGTH = 1

class Mic:

    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(
            rate=SAMPLE_RATE,
            channels=1,
            format=FORMAT,
            input=True,
            frames_per_buffer=INPUT_CHUNK,
            input_device_index=DEVICE_INDEX)

    @staticmethod
    def rms(frame):
        count = len(frame) / swidth
        format = "%dh" % (count)
        shorts = struct.unpack(format, frame)

        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)
        return rms * 1000

    def get_next_audio_frame(self):
        data = self.audio_stream.read(INPUT_CHUNK, exception_on_overflow=False)
        data = struct.unpack_from("h" * INPUT_CHUNK, data)
        return data

    def __play_recording_notification(self):
        wf = wave.open(RECORDING_NOTIFICATION_WAV_FILE, 'rb')
        stream = self.pa.open(format=self.pa.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(OUTPUT_CHUNK)
        while data != b'':
            stream.write(data)
            data = wf.readframes(OUTPUT_CHUNK)
        stream.close()

    def write(self, recording):
        n_files = len(os.listdir(TMP_RECORDING_LOCATION))
        filename = os.path.join(TMP_RECORDING_LOCATION, '{}.wav'.format(n_files))
        wf = wave.open(filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.pa.get_sample_size(FORMAT))
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(recording)
        wf.close()
        return n_files

    def record(self):
        self.__play_recording_notification()
        rec = []
        current = time.time()
        end = time.time() + TIMEOUT_LENGTH

        while current <= end:

            data = self.audio_stream.read(INPUT_CHUNK, exception_on_overflow=False)
            if self.rms(data) >= Threshold: end = time.time() + TIMEOUT_LENGTH
            current = time.time()
            rec.append(data)
        filename = self.write(b''.join(rec))
        return "tmp/%s.wav" % filename
