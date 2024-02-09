import soundfile
from pydub import AudioSegment



def sampwidth(path_to_file):
    data, samplerate = soundfile.read(path_to_file)
    soundfile.write(path_to_file, data, samplerate, subtype='PCM_16')

def channels(path_to_file):
    sound = AudioSegment.from_wav(path_to_file)
    sound = sound.set_channels(1)
    sound.export(path_to_file, format="wav")