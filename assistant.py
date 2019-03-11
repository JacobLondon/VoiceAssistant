
import speech_recognition as sr
import os, msvcrt, time
from threading import Thread


class Assistant:

    def __init__(self, keyword='hello there'):
        self.keyword = keyword
        self.r = sr.Recognizer()
        self.translate = self.r.recognize_google
        self.listen = self.r.listen

        # wait for key press
        self.rate = 1 / 60
        self.talk_key = b'`'
        self.listening = False
        self.done = False

    def start(self):
        Thread(target=self.await_commands).start()
        self.wait()

    def wait(self):
        while not self.done:
            key = msvcrt.getch()
            if key == self.talk_key:
                self.listening = True
            time.sleep(self.rate)
    
    def await_commands(self):
        while not self.done:

            # wait until key press
            while not self.listening:
                time.sleep(self.rate)

            with sr.Microphone() as source:
                print('listening')
                audio = self.listen(source)
            try:
                text = self.translate(audio).lower().split()
                print(text)

                # check if the user said the keyword/phrase
                if self.keyword == text[:len(self.keyword)]:
                    if text[2] == 'start':
                        process = text[3]
                        print('Starting:', process)
                        os.startfile(process)

                elif text[0] == 'stop':
                    self.done = True
                    return
            except:
                print('Failed to complete task.')

            self.listening = False
            print('waiting')

