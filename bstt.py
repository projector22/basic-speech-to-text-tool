##
# Author: Gareth Palmer
# Licence: MIT
# Date Started: 2022-05-16
# Version 1.0.0
##

import argparse
# from email.mime import audio
import speech_recognition as sr

ap = argparse.ArgumentParser()
ap.add_argument("-f", required=False, help="Name the path to the file to convert")
ap.add_argument("-t", required=False, action='store_true', help="Perform a run on a text file")
arg = vars(ap.parse_args())

if (arg['t'] == True):
    from os import path
    file = 'bin/test.wav'
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), file)
elif (arg['f'] != None):
    file = arg['f']
    pass
else:
    print("No valid file chosen. Please parse a file using the -f argument.")

r = sr.Recognizer()
try:
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
except ValueError:
    import sys
    print("Audio file could not be read as PCM WAV, AIFF/AIFF-C, or Native FLAC; check if file is corrupted or in another format")
    sys.exit()

##
# Link: https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py
##

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    # print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    print("Analyzing...")
    output = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
print('Complete')
file = open('output.txt', 'w')
file.write(output)
file.close()
print("View the transcript here:", path.join(path.dirname(path.realpath(__file__)), 'output.txt'))
