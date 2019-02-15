"""
Libraries:
    PyAudio
    SpeechRecognition
"""

import speech_recognition as sr
import os, msvcrt, time
from threading import Thread

r = sr.Recognizer()

done = False
listening = False
rate = 1 / 60
keyword = 'ok google'.split()
talk_key = b'`'

def wait():
    global done, listening
    while not done:
        key = msvcrt.getch()
        if key == talk_key:
            listening = True
        time.sleep(rate)

def await_commands():
    global done, listening
    while not done:

        # wait until key press
        while not listening:
            time.sleep(rate)

        with sr.Microphone() as source:
            print('listening')
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower().split()

            if all(keyword[i] == text[i] for i in range(len(keyword))):
                if text[2] == 'start':
                    process = text[3]
                    print('Starting:', process)
                    os.startfile(process)

            elif text[2] == 'stop':
                done = True
        except:
            print('Failed to complete task.')

        listening = False
        print('waiting')

if __name__ == '__main__':
    Thread(target=await_commands).start()
    wait()