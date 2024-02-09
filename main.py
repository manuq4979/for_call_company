from pydub import AudioSegment
import sys

import voice2text

print(sys.argv[1], sys.argv[2])


def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

def valume_change(sound, dB):
    sound += dB
    
    return sound


def save_result(path_to_file):
    path_to_file = path_to_file.split(".wav")[0]+"_result.wav"
    sound.export(path_to_file, format="wav")




arguments = []
mode = ""
if sys.argv[1].find("lang") != -1:
    lang = sys.argv[1].split("=")[1]
    arguments.append(lang)
    mode = "voiceToText"
    
if sys.argv[1].find("valume") != -1:
    val = sys.argv[1].split("=")[1]
    val = float(val)
    arguments.append(val)
    mode = "valume"
    
if sys.argv[1].find("speed") != -1:
    dB = sys.argv[1].split("=")[1]
    dB = float(dB)
    arguments.append(dB)
    mode = "speed"

path_to_file = sys.argv[2]
arguments.append(path_to_file)

print(arguments)

sound = AudioSegment.from_wav(path_to_file)

if mode == "voiceToText":
    voice2text.voiceToText(path_to_file, arguments[0])
if mode == "valume":
    sound = valume_change(sound, arguments[0])
    save_result(path_to_file)
if mode == "speed":
    sound = speed_change(sound, arguments[0])
    save_result(path_to_file)


# slow_sound = speed_change(sound, 0.75)
# fast_sound = speed_change(sound, 2.0)