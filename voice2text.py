path_to_model_ru = "vosk-model-ru-0.42"
path_to_model_en = "vosk-model-en-us-0.22"


from vosk import Model, KaldiRecognizer
import sys
import os
import wave
from pydub import AudioSegment
import wav_correction

def voiceToText(path_to_file, lang):

    wf = wave.open(path_to_file, "rb")
    if wf.getnchannels() != 1:
        print("I am correcting the wav file channels...")
        wav_correction.channels(path_to_file)
    if wf.getsampwidth() != 2:
        print("I am correcting the sampling and converting it to a 16-bit frequency...")
        wav_correction.sampwidth(path_to_file)
    if wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM, not NONE type.")
        exit(1)



    path_to_module = ""
    if lang == "ru":
        path_to_module = path_to_model_ru
    if lang == "en":
        path_to_module = path_to_model_en
     
    if not os.path.exists(path_to_module):
        print ("Please download the model from https://github.com/alphacep/kaldi-android-demo/releases and unpack as 'model-en' in the current folder.")
        exit (1)

    model = Model(path_to_module)
    
    

    

    rec = KaldiRecognizer(model, wf.getframerate())
    with open("result_text.txt", 'w', encoding='utf-8') as file:
        while True:
            data = wf.readframes(1000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                print(rec.Result())
                file.writelines(f'{rec.Result()}\n')
            else:
                print(rec.PartialResult())
                file.writelines(f'{rec.PartialResult()}\n')
        file.writelines(f'{rec.FinalResult()}\n')
    #print(rec.FinalResult())

    #with open("result_text2.txt", 'w', encoding='utf-8') as file:
    #    file.writelines(f'{rec.FinalResult()}\n')